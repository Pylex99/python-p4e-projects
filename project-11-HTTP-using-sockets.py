# Program establishes a socket connection to a server, sends a GET request for a specific file, receives and prints the response data from the server, and then closes the socket connection.


import socket  # Import the socket module

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
mysock.connect(('data.pr4e.org', 80))  # Connect to the specified server and port

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()  # Create a GET request
mysock.send(cmd)  # Send the request to the server

while True:
    data = mysock.recv(512)  # Receive data from the server, maximum 512 bytes at a time
    if len(data) < 1:  # If no data is received, break the loop
        break
    print(data.decode(), end='')  # Print the received data

mysock.close()  # Close the socket connection
