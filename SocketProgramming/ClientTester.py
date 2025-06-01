import socket

def chat_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(('localhost', 12345))

        while True:
            # Receive message from server
            data = client.recv(1024).decode().strip()
            if not data or data.lower() == 'x':
                print("Server ended the chat.")
                break
            print(f"Server: {data}")

            # Send reply
            msg = input("You: ")
            client.send(msg.encode())
            if msg.lower() == 'x':
                print("You ended the chat.")
                break

if __name__ == "__main__":
    chat_client()