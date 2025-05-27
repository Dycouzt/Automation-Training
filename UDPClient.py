# This script shows how a UDP one-way connection works in python.
import socket

udp_client_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client_s.sendto(b"Hello from UDP client!", ('localhost', 12345))  # Send to server

udp_client_s.close()