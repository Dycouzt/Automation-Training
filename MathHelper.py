"""
Goal: Client sends two numbers, server adds them and sends back the result.
- Client sends: "4,5"
- Server sends: "Result: 9"
"""

import socket

def addition(num1, num2):
    result = int(num1) + int(num2)
    return f"Result: {result}"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 3333))
server.listen(1)

print("Server listening on port 3333...")

conn, addr = server.accept()
print(f"Connection established with {addr}")

try:
    data = conn.recv(1024).decode()
    if data:
        num1, num2 = data.split(",")
        print(f"Received from {addr}: {num1}, {num2}")
        response = addition(num1, num2)
        conn.send(response.encode())
finally:
    conn.close()
    print("Connection closed.")