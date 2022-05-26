# get_large_file.py
# Code adapted from "Computer Networking A Top-Down Approach, 7th Edition by
# James Kurose", pg. 166 AND https://realpython.com/python-sockets/#tcp-sockets
from socket import *

# PARAMETERS
serverName = 'gaia.cs.umass.edu'
serverPort = 80
request = "GET /wireshark-labs/HTTP-wireshark-file3.html " \
          "HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

# CREATE socket and CONNECT
clientSocket = socket(AF_INET, SOCK_STREAM)  # TCP connection
clientSocket.connect((serverName, serverPort))

# SEND request
clientSocket.send(request.encode())

# LOOP over RESPONSE data in chunks until no data left
while True:
    response = clientSocket.recv(1024)
    if not len(response) > 0:
        break
    print(response.decode())

# CLOSE connection
clientSocket.close()
