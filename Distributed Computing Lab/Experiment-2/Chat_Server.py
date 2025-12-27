# Name: Amey Mahendra Thakur
# Course: Distributed Computing Lab (CSL802)
# Roll No: 50 | Batch: B3
# Date of Experiment: January 20, 2022
# Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
# Description: Experiment 2 - Implementation of Group Communication (Chat Application) using Socket Programming (Server-side)

import socket
import sys
import time

def start_server():
    """
    Initializes the server socket, binds to a local host and port, 
    and facilitates synchronous communication with a client.
    """
    # 1. Instantiate the socket object using IPv4 and TCP protocols
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Retrieve local machine metadata
    host_name = socket.gethostname()
    server_ip = socket.gethostbyname(host_name)
    port = 8080

    print("--- [DISTRIBUTED COMPUTING CHAT SERVER] ---")
    
    # 3. Bind the socket to the network interface and designated port
    try:
        server_socket.bind((host_name, port))
        print(f"[*] Successfully bound to {host_name} on Port: {port}")
        print(f"[*] Server IP Address: {server_ip}")
    except socket.error as err:
        print(f"[!] Binding failed: {err}")
        sys.exit()

    # 4. Input server-side identity
    user_name = input('[?] Enter your identification name: ')

    # 5. Listen for incoming connection requests (Backlog of 1)
    server_socket.listen(1)
    print(f"[*] Server is now listening for incoming connections...")

    # 6. Accept a connection from a client
    connection, address = server_socket.accept()
    print(f"[+] Connection established with: {address[0]} at Port: {address[1]}")

    # 7. Initial Handshake: Exchange identification names
    try:
        # Receive client name
        client_identity = (connection.recv(1024)).decode()
        print(f"[!] {client_identity} has joined the session.")
        
        # Send server name
        connection.send(user_name.encode())

        # 8. Communication Loop: Synchronous Message Exchange
        while True:
            # Outbound Message
            outbound_msg = input(f"[{user_name}] : ")
            connection.send(outbound_msg.encode())
            
            # exit condition (optional logic can be added here)
            if outbound_msg.lower() == 'exit':
                break

            # Inbound Message
            inbound_msg = connection.recv(1024).decode()
            if not inbound_msg:
                break
            print(f"[{client_identity}] : {inbound_msg}")

    except Exception as e:
        print(f"[!] Communication Error: {e}")
    finally:
        print("[*] Terminating Server Session...")
        connection.close()
        server_socket.close()

if __name__ == "__main__":
    start_server()
