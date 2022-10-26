# Programming Project: Client-Server Chat (Portfolio Assignment)

A simple client-server program using python sockets that emulates a simple chat client.


    
## To Run

Uses Python version 3.9.12. There are two files:

    `server.py`
    `client.py`

Both programs need to be run separately, with the `server.py` program being run first. Since they are connected over a socket, they will need to identify the same host address and port number. By default, both programs use localhost (127.0.0.1) as the host IP address, and 3580 as the port number. If desired, an alternate port number can be used by listing it as the next argument in the command line. 


    # Default port 3580
    python server.py
    python client.py
    
    # User-specified port
    python server.py <port_number>
    python client.py <port_number>

Once both programs are running, with separate consoles, the client will be the first to prompt the user for a message to send to the server. Upon entering a message, the message will be sent through the socket connection to the server and displayed on the server console. From there the server will prompt the user to enter a message to send to the client, after which the message is sent to the client and the process repeats. This will continue until the command to close the connection (`/q`) is entered as a message on either the client or the server.

Each program closes the connection if the user types the quit command (/q), prior to sending the message to their respective counterpart. Additionally, to prevent hanging, there is a while loop that will only continue after the message to send is of non-zero length (i.e. not equal to an empty string “”). 

## Example Exchange

#### Server

1. The server creates a socket and binds to ‘**localhost**’ and port **xxxx**
2. The server then **listens** for a connection
3. When connected, the server calls `recv` to receive data
    1. The server **prints** the data, then **prompts** for a reply
    2. If the reply is `/q`, the server **quits**
    3. Otherwise, the server sends the reply
    4. Back to **step 3**
4. Sockets are closed (can use `with` in python3)

#### Client

1. The client creates a socket and connects to ‘**localhost**’ and port **xxxx**
2. When connected, the client **prompts for a message to send**
    1. If the message is `/q`, the client **quits**
    2. Otherwise, the client **sends** the message
    3. The client calls `recv` to receive data
    4. The client **prints** the data
    5. Back to **step 2**
3. Sockets are **closed** (can use `with` in python3)


## Example screenshots:
![](screen_shots/Screen%20Shot%202022-05-27%20at%201.24.23%20PM.png)
Server (left) and Client (right) - demonstrating behavior seen in project description screen shots

![](screen_shots/Screen%20Shot%202022-05-27%20at%2011.12.17%20AM.png)

Server (left) and Client (right) - Server using quit command to close connection
