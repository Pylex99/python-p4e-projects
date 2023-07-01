# The purpose of this program is to retrieve the content of a web page specified by the user through a URL, count the number of received bytes from the server, and display the count on the console. It uses a socket connection to connect to the host at port 80 (HTTP) and sends a GET request to retrieve the web page content.

import socket

url = input("Enter - ")  # Prompt the user to enter a URL
try:
    word = url.split("/")  # Split the URL by "/"
    host = word[2]  # Extract the host from the URL
    print("The host: ", host)

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
    mysock.connect((host, 80))  # Connect to the host on port 80 (HTTP)
    cmd = ("GET " + url + " HTTP/1.0\r\n\r\n").encode()  # Create a GET request for the specified URL
    mysock.send(cmd)  # Send the GET request

except:
    print("Not a URL")

count = 0  # Initialize a variable to count the received data bytes

while True:
    data = mysock.recv(512)  # Receive up to 512 bytes of data
    for c in data:
        count += 1  # Increment the count for each received byte
    if len(data) < 1 or count > 3000:  # If no more data is received or the count exceeds 3000 bytes
        break  # Exit the loop

print(count)  # Print the total count of received bytes
mysock.close()  # Close the socket
