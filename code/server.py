from socket import *
import sys
import random

# Seed RNG
random.seed()

# PARAMETERS
serverName = "127.0.0.1"

# Create random number within valid port range
# serverPort = random.randrange(1024, 49151, 1)
serverPort = 3580
response = "hello to you sir"

# USER PORT if provided at command line
if len(sys.argv) > 1:
    serverPort = int(sys.argv[1])

# CREATE listening socket and BIND to serverPort - TCP connection
# 'with' statement for socket connection:
# SOURCE: https://realpython.com/python-sockets/#tcp-sockets
with socket(AF_INET, SOCK_STREAM) as serverSocket:
    # ALLOW port to be reused immediately
    # SOURCE: https://bit.ly/3NXGZeQ
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # BIND socket and LISTEN
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print(f'The server is listening on: {serverName} on port: {serverPort}')

    # CREATE connection socket if requested by client
    connectionSocket, addr = serverSocket.accept()
    with connectionSocket:
        print("Waiting for message...")
        message = ""
        while True:
            # GET request from client and PRINT
            message = connectionSocket.recv(1024).decode()
            if not message:
                break
            print(message)

            response = input("Enter message to send...\n>")

            # SEND response to client and PRINT
            connectionSocket.sendall(response.encode())

            print("message sent")

            # CLOSE connection and loop
            connectionSocket.close()
            break
