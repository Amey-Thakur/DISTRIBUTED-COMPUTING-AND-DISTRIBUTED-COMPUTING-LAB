# Name: Amey Mahendra Thakur
# Course: Distributed Computing Lab (CSL802)
# Roll No: 50 | Batch: B3
# Date of Experiment: January 20, 2022
# Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
# Description: Experiment 2 - Implementation of Group Communication (Chat Application) using Socket Programming (Client-side)

import socket
import sys
import time

def start_client():
    """
    Initializes the client socket, connects to a specified server IP,
    and facilitates synchronous communication with the server.
    """
    # 1. Instantiate the socket object using IPv4 and TCP protocols
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print("--- [DISTRIBUTED COMPUTING CHAT CLIENT] ---")

    # 2. Configuration for connection
    try:
        target_ip = input('[?] Enter Server IP address to connect: ')
        target_port = 8080
        user_name = input('[?] Enter your identification name: ')

        # 3. Establish connection to the remote server
        print(f"[*] Attempting connection to {target_ip}:{target_port}...")
        client_socket.connect((target_ip, target_port))
        print("[+] Connection Successful.")

        # 4. Initial Handshake: Exchange identification names
        # Send client's name to server
        client_socket.send(user_name.encode())
        
        # Receive server's name
        server_identity = (client_socket.recv(1024)).decode()
        print(f"[!] Connected to Server: {server_identity}")

        # 5. Communication Loop: Synchronous Message Exchange
        while True:
            # Inbound Message (Server speaks first in this synchronous model)
            inbound_msg = (client_socket.recv(1024)).decode()
            if not inbound_msg or inbound_msg.lower() == 'exit':
                print(f"[*] {server_identity} has terminated the connection.")
                break
            print(f"[{server_identity}] : {inbound_msg}")
            
            # Outbound Message
            outbound_msg = input(f"[{user_name}] : ")
            client_socket.send(outbound_msg.encode())
            
            if outbound_msg.lower() == 'exit':
                break

    except socket.error as err:
        print(f"[!] Connection failed: {err}")
    except Exception as e:
        print(f"[!] An error occurred: {e}")
    finally:
        print("[*] Closing client session...")
        client_socket.close()

if __name__ == "__main__":
    start_client()