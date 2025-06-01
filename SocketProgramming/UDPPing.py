"""
The goal is to create a simple UDP based ping script.
- UDP client sends “ping” to server.
- Server replies with “pong”.
- Try sending it multiple times and print a timestamp.
"""
import socket


def ping_pong():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as ping_server:
        ping_server.bind(('localhost', 12345))
        print("UDP Server listening on port 12345...")

        while True:
            data, addr = ping_server.recvfrom(1024)

            if data.decode().lower().strip() == "ping":
                ping_server.sendto(b"pong", addr)
            else:
                ping_server.sendto(b"Hell Nah dawg! ", addr)
                break


if __name__ == "__main__":
    ping_pong()

