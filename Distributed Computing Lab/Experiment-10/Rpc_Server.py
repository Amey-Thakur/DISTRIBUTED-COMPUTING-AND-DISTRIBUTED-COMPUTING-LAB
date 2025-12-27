# Name: Amey Mahendra Thakur
# Course: Distributed Computing Lab (CSL802)
# Roll No: 50 | Batch: B3
# Date of Experiment: March 31, 2022
# Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
# Description: Experiment 10 - Implementation of Name Resolution and RPC (Server side).
# This script facilitates a chat-based interface where the client can request file status, directory paths, and data.

import time
import socket
import sys
import os
import os.path

def main():
    print("="*60)
    print(" DISTRIBUTED NAME RESOLUTION & RPC SERVER ")
    print("="*60)
    
    print("\n[+] Initializing Server Components...")
    time.sleep(1)

    # 1. Socket Setup
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        port = 1234
        
        s.bind((host, port))
        print(f"[*] Server Identity: {host} ({ip})")
        print(f"[*] Listening on Port: {port}")
        
        name = input("\n[?] Enter Administrator Name: ")
                   
        s.listen(1)
        print("\n[*] Waiting for incoming client connection...")
        
        conn, addr = s.accept()
        print(f"[+] Connection established with {addr[0]} (Port: {addr[1]})")

        # 2. Handshake Phase
        client_name = conn.recv(1024).decode()
        print(f"\n[!] Client '{client_name}' has joined the session.")
        conn.send(name.encode())

        # 3. Command Menu Transmission
        commands_menu = '''
    =========================================
    AVAILABLE RPC COMMANDS:
    1. request-file-status:<filename>
    2. request-file-dir:<filename>
    3. request-file-data:<filename>
    =========================================
    '''
        conn.send(commands_menu.encode())

        # 4. Main Service Loop
        while True:
            try:
                data = conn.recv(1024).decode()
                
                if not data or data == "[e]":
                    print(f"\n[*] Client '{client_name}' requested termination.")
                    break

                print(f"\n[CLIENT]: {data}")
                
                # Command Parsing
                if ":" not in data:
                    conn.send("Error: Invalid command format. Use 'command:filename'".encode())
                    continue

                command, filename = data.split(':', 1)
                data_path = "data/"
                filepath = os.path.join(data_path, filename)

                # RPC Logic: Name & Resource Resolution
                if command == "request-file-status":
                    status = os.path.exists(filepath)
                    response = f"[STATUS] {filename} exists." if status else f"[ERROR] {filename} not found."
                    conn.send(response.encode())

                elif command == "request-file-dir":
                    if os.path.exists(filepath):
                        abs_path = os.path.abspath(filepath)
                        conn.send(f"[DIRECTORY] {abs_path}".encode())
                    else:
                        conn.send(f"[ERROR] {filename} does not exist.".encode())

                elif command == "request-file-data":
                    if os.path.exists(filepath):
                        # Inform client to prepare for data stream
                        conn.send(f"sending-file:{filename}".encode())
                        ack = conn.recv(1024).decode()
                        
                        if ack == "ready":
                            with open(filepath, "r") as f:
                                file_content = f.read()
                                conn.send(file_content.encode())
                            print(f"[*] Successfully transferred {filename} contents.")
                    else:
                        conn.send(f"[ERROR] {filename} does not exist.".encode())
                
                else:
                    conn.send("[ERROR] Unknown RPC Command.".encode())

            except Exception as e:
                print(f"[!] Processing Error: {e}")
                break

    except Exception as e:
        print(f"[!] Server Failure: {e}")
    finally:
        print("\n[*] Shutting down server. Cleaning resources...")
        s.close()
        print("="*60)

if __name__ == "__main__":
    main()
