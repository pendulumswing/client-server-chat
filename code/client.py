from socket import *
import sys
import random

serverName = "127.0.0.1"

# Create random number within valid port range
serverPort = 3580

# USER PORT if provided at command line
if len(sys.argv) > 1:
    serverPort = int(sys.argv[1])

# CREATE socket and connect to server
clientSocket = socket(AF_INET, SOCK_STREAM)  # TCP connection
clientSocket.connect((serverName, serverPort))

request = input("Enter message to send...\n>")

# SEND request to server
clientSocket.send(request.encode())

# GET response from server and print
response = clientSocket.recv(1024)
print("From Server: ", response.decode())

# # CLOSE connection
# clientSocket.close()