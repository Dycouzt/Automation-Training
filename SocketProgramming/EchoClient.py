"""
This script shows how socket programming works in python. Creates a server and a client. This is the client script.
It encodes and sends a message to the server.
"""
import socket


import socket

# Create the client socket (IPv4 + TCP)
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
socket_client.connect(('localhost', 9999))  # Use connect, not bind

# Encode and send the message to the server
socket_client.send("Hello server!".encode())

# Receive the echo from the server
data = socket_client.recv(1024).decode()
print(f"Received from server: {data}")

# Close the client socket
socket_client.close()
