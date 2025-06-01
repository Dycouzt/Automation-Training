"""
Goal: Server replies differently depending on what the client says.
- Client sends one word: "hi", "bye", or "name".
Server replies:
- "hi" → "Hello!"
- "bye" → "Goodbye!"
- "name" → "I'm Python Server!"
"""
import socket
responsive_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
responsive_s.bind(('localhost', 2222))
responsive_s.listen(1)
print("Listening for connections on port 2222...")
conn, addr = responsive_s.accept()
print(f"Connection established with {addr}")
data = conn.recv(1024).decode().lower().strip()

if data == "hi":
    conn.send("Hello! ".encode())
elif data == "name":
    conn.send("My name is 'Responsive Server'!".encode())
elif data == "bye":
    conn.send("Goodbye! ".encode())
else:
    conn.send("Hell nah dawg".encode())

conn.close()
responsive_s.close()
print("Session Finished! ")

"""
Updated version:
import socket

responses = {
    "hi": "Hello!",
    "name": "My name is 'Responsive Server'!",
    "bye": "Goodbye!"
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(('localhost', 2222))
    server.listen(1)
    print("Listening for connections on port 2222...")
    
    conn, addr = server.accept()
    with conn:
        print(f"Connection established with {addr}")
        data = conn.recv(1024).decode().lower().strip()
        reply = responses.get(data, "Hell nah dawg")
        conn.send(reply.encode())

print("Session Finished!")
"""