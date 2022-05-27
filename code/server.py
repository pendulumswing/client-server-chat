from socket import *
import sys
import random

DEBUG = False

# Seed RNG
# random.seed()

# PARAMETERS
serverName = "127.0.0.1"

# Create random number within valid port range
# serverPort = random.randrange(1024, 49151, 1)
serverPort = 3580

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
    print(f'Server listening on: {serverName} on port: {serverPort}')

    # CREATE connection socket if requested by client
    connectionSocket, addr = serverSocket.accept()
    with connectionSocket:
        print(f"Connected by {addr}")
        print("Waiting for message...")
        message = ""
        response = ""
        first = True  # To track if first time receiving a message
        while True:
            response = ""  # RESET response

            # GET request from client and PRINT
            message = connectionSocket.recv(1024).decode()
            if not message:
                print(f"No message received")
                break
            if message == "/q":
                break
            print(f"{message}")

            # DISPLAY prompt if FIRST time receiving a message
            if first:
                print("Type /q to quit")
                print("Enter message to send...")
                first = False

            # PROMPT message to send from SERVER
            while response == "":
                response = input(">")

            # SEND response to client
            connectionSocket.send(response.encode())

        # CLOSE connection and loop
        print("SERVER: Closing Connection") if DEBUG else 0
        connectionSocket.close()
