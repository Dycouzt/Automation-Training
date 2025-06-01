"""
The challenges are based on socket programming and networking.
"""
import socket

# Using 'with' helps cleanup and close everything when finished. Easier than manually closing, just as using files.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_s:
    server_s.bind(('localhost', 9999))
    server_s.listen(1)
    print("Server listening on port 9999...")

    conn, addr = server_s.accept()
    with conn:
        print(f"Connected by {addr}")
        conn.send("Hello Client!".encode())
