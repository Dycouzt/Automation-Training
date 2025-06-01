"""
- Create a simple turn-based chat system using TCP.
- Allow the client and server to take turns sending messages (use a while loop).
"""
import socket

def chat_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(('localhost', 12345))
        server.listen(1)
        print("Server listening on port 12345...")

        conn, addr = server.accept()
        print(f"Connected by {addr}")

        with conn:
            conn.send("Hello! I'm a Chat Server!\n".encode())
            conn.send("Enter 'x' to exit.\n".encode())

            while True:
                # Receive message from client
                client_msg = conn.recv(1024).decode().strip().lower()
                if not client_msg or client_msg == 'x':
                    print("Client ended the chat.")
                    break
                print(f"Client: {client_msg}")

                # Server replies
                server_msg = input("You: ")
                if server_msg.lower() == 'x':
                    conn.send("x".encode())
                    print("You ended the chat.")
                    break
                conn.send(server_msg.encode())

if __name__ == "__main__":
    chat_server()