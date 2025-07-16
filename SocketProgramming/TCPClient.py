import socket

message = input("Message: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_client:
    tcp_client.connect(('localhost', 9999))
    tcp_client.send(message.encode())

    print(f"{message} sent!")

    conn, addr = tcp_client.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024).decode()
    print(f"{data} received from {addr}! ")

    conn.close()
    tcp_client.close()
    print("Server Closed! ")

