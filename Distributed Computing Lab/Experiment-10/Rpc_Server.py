import time, socket, sys
import os.path
import os

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))
           
s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
conn.send(name.encode())

# commands=["request-file-status","request-file-dir","request-file-data"]

comands = '''COMMANDS: 
                    request-file-status:
                    request-file-dir:
                    request-file-data:
                '''
conn.send(comands.encode())                
while True:
    message = conn.recv(1024)
    message = message.decode()
    if message == "[e]":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break
    # conn.send(message.encode()) 
    

    buffer = message.split(':')
    cmnd = buffer[0]
    filename = buffer[1]
    # print(filename)

    if cmnd == "request-file-status":
        print("Command accepted")
        path="data/"
        filepath=path+filename
        status = os.path.exists(filepath)
        print(status)
        if status:
            response = filename + "  exists"
        else:
            response = filename + "  does not exist"

        conn.send(response.encode())

    elif cmnd == "request-file-dir":
        print("Command accepted")
        cwd = os.getcwd()
        path = "/data/"
        filepath=cwd+path+filename
        status = os.path.exists(filepath)
        print(status)
        if status:
            response = filepath
        else:
            response = filename + "  does not exist"

        conn.send(response.encode())

    elif cmnd == "request-file-data":
        print("Command accepted")
        path = "data/"
        filepath=path+filename
        status = os.path.exists(filepath)
        print(status)
        if status:
            file = open(filepath, "r")
            file_data = file.read()
            response = "sending-file:"+filename
            conn.send(response.encode())
            message = conn.recv(1024)
            message = message.decode()
            if message == "ready":
                response = file_data
                conn.send(response.encode())
            else:
                pass
        else:
            response = filename + "  does not exist"
            conn.send(response.encode())
        


    # print(s_name, ":", message)
