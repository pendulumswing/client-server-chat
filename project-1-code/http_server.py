# http_server.py
# Code adapted from "Computer Networking A Top-Down Approach, 7th Edition by
# James Kurose", pg. 168 AND https://realpython.com/python-sockets/#tcp-sockets
from socket import *
import sys
import random

# Seed RNG
random.seed()

# PARAMETERS
serverName = "127.0.0.1"

# Create random number within valid port range
serverPort = random.randrange(1024, 49151, 1)
data = "HTTP/1.1 200 OK\r\n" \
       "Content-Type: text/html; charset=UTF-8\r\n\r\n" \
       "<html>Congratulations!  You've downloaded the first Wireshark lab " \
       "file!</html>\r\n"

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
    print('The server is listening on port: ', serverPort)

    # CREATE connection socket if requested by client
    connectionSocket, addr = serverSocket.accept()
    with connectionSocket:
        while True:
            # GET request from client and PRINT
            message = connectionSocket.recv(1024).decode()
            if not message:
                break
            print("Received: ", message)

            # SEND response to client and PRINT
            print("Sending>>>>>>>>>", data, "<<<<<<<<<")
            connectionSocket.sendall(data.encode())

            # CLOSE connection and loop
            connectionSocket.close()
            break
