# connect_server.py
# Code adapted from "Computer Networking A Top-Down Approach, 7th Edition by
# James Kurose", pg. 166 AND https://realpython.com/python-sockets/#tcp-sockets
from socket import *

# PARAMETERS
serverName = 'gaia.cs.umass.edu'
serverPort = 80
request = "GET /wireshark-labs/INTRO-wireshark-file1.html " \
          "HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

# CREATE socket and connect to server
clientSocket = socket(AF_INET, SOCK_STREAM)  # TCP connection
clientSocket.connect((serverName, serverPort))

# SEND request to server
clientSocket.send(request.encode())

# GET response from server and print
response = clientSocket.recv(1024)
print("From Server: ", response.decode())

# CLOSE connection
clientSocket.close()
