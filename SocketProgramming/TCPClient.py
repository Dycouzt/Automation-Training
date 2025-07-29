import socket

message = input("Message: ")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_client:
        tcp_client.connect(('localhost', 9999))

        tcp_client.send(message.encode())
        print(f"message sent!")

        data = tcp_client.recv(1024)
        print(f"Received from server: {data}")

except ConnectionRefusedError:
    print("Connection refused!")
    
except OSError:
    print("Invalid Argument! ")