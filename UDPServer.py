# This script demonstrates how a UDP server-client connection works.
import socket

udp_server_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_s.bind(('localhost', 12345))  # Bind to localhost and port
print("UDP Server listening on port 12345...")

data, addr = udp_server_s.recvfrom(1024)  # Receive data and address
print(f"Received from {addr}: {data.decode()}")

udp_server_s.close()
