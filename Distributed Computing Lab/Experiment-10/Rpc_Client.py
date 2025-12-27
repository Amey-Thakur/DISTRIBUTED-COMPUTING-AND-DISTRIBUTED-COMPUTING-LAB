# Name: Amey Mahendra Thakur
# Course: Distributed Computing Lab (CSL802)
# Roll No: 50 | Batch: B3
# Date of Experiment: March 31, 2022
# Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
# Description: Experiment 10 - Implementation of Name Resolution and RPC (Client side).
# This script interacts with the RPC server to resolve resource names and retrieve data.

import time
import socket
import sys
import re

def main():
    print("="*60)
    print(" DISTRIBUTED NAME RESOLUTION & RPC CLIENT ")
    print("="*60)
    
    print("\n[+] Initializing Client Components...")
    time.sleep(1)

    s = socket.socket()
    shost = socket.gethostname()
    ip = socket.gethostbyname(shost)
    
    print(f"[*] Local Hostname: {shost} ({ip})")
    
    # 1. Connection Phase
    try:
        host = input("[?] Enter Server IP Address (or hostname): ")
        name = input("[?] Enter your Client Name: ")
        port = 1234
        
        print(f"\n[*] Attempting connection to {host}:{port}...")
        time.sleep(1)
        
        s.connect((host, port))
        print("[+] Connection Successful!")

        # 2. Handshake Phase
        s.send(name.encode())
        server_admin = s.recv(1024).decode()
        print(f"\n[!] Connected to Administrator: {server_admin}")
        print("[!] Enter 'exit' to terminate the session.")

        # 3. Command Interaction Loop
        while True:
            # Receive server menu or last command result
            server_response = s.recv(1024).decode()
            print(f"\n[SERVER]: {server_response}")

            # Check for file transfer initiation from server
            if re.search("^sending-file", server_response):
                _, filename = server_response.split(':')
                print(f"[*] Preparing to receive file: {filename}")
                
                # Send acknowledgment to start stream
                s.send("ready".encode())
                file_data = s.recv(4096).decode() # Buffer increased for file data
                
                # Save received data to local file
                with open(f"received_{filename}", "w") as f:
                    f.write(file_data)
                print(f"[SUCCESS] Resource '{filename}' resolved and saved locally.")
                
                # Wait for next input
                user_msg = input("\n[ME]: ")
            else:
                user_msg = input("\n[ME]: ")

            if user_msg.lower() == 'exit' or user_msg.lower() == '[e]':
                s.send("[e]".encode())
                break
            
            s.send(user_msg.encode())

    except ConnectionRefusedError:
        print("[!] Error: Connection refused. Ensure the server is running.")
    except Exception as e:
        print(f"[!] Critical error occurred: {e}")
    finally:
        print("\n[*] Closing connection. Session finalized.")
        s.close()
        print("="*60)

if __name__ == "__main__":
    main()
