# This script shows how a UDP one-way connection works in python.
import socket
import time


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as ping_client:
    for i in range(5):
        msg = b"ping"
        start = time.time()
        ping_client.sendto(msg, ('localhost', 12345))
        data, addr = ping_client.recvfrom(1024)
        end = time.time()
        print(f"[{i+1}] Received: {data.decode()} - RTT: {(end - start)*1000:.2f} ms")
        time.sleep(1)
