from socket import *
import sys

DEBUG = False

serverName = "127.0.0.1"

# Create random number within valid port range
serverPort = 3580

# USER PORT if provided at command line
if len(sys.argv) > 1:
    serverPort = int(sys.argv[1])

# CREATE socket and connect to server
clientSocket = socket(AF_INET, SOCK_STREAM)  # TCP connection
clientSocket.connect((serverName, serverPort))

with clientSocket:
    request = ""
    print("Enter message to send...")

    while True:
        request = ""  # RESET request

        # PROMPT message to send from CLIENT
        while request == "":
            request = input(">")

        # SEND request to server
        clientSocket.send(request.encode())

        # GET response from server and print
        response = clientSocket.recv(1024).decode()
        if not response:
            print(f"No message received") if DEBUG else 0
            break
        if response == "/q":
            # print(f"response is equal to '/q'")
            break
        # print(f"response: '{response}' responseLen: {len(response)}")

        print(f"{response}")


    # CLOSE connection
    print("CLIENT: Closing Connection") if DEBUG else 0
    clientSocket.close()