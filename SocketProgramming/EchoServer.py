"""
This script shows how socket programming works in python. Creates a server and a client. This is the server script,
it decodes and echoes back the message the client sent.
"""

import socket

# 1. Create a socket (IPv4 + TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind to localhost on port 12345
server_socket.bind(('localhost', 12345))

# 3. Start listening for connections
server_socket.listen(1)
print("Server is listening on port 12345...")

# 4. Accept a connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# 5. Receive data (up to 1024 bytes)
data = conn.recv(1024).decode()
print(f"Received from client: {data}")

# 6. Send back the same message prefixed with "Echo: "
response = f"Echo: {data}"
conn.send(response.encode())

# 7. Close connection
conn.close()
server_socket.close()
print("Server closed.")


