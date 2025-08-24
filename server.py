import socket
import threading

HOST = "0.0.0.0"
PORT = 55556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []  

def broadcast(message, sender_socket=None):
    for client_socket, _ in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode("utf-8"))
            except:
                remove_client(client_socket)

def remove_client(client_socket):
    for c, nickname in clients:
        if c == client_socket:
            clients.remove((c, nickname))
            c.close()
            broadcast(f"🚪 {nickname} has left the chat.")
            break

def handle_client(client_socket, nickname):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                full_message = f"{nickname}: {message}"  
                print(full_message)
                broadcast(full_message, client_socket)
            else:
                remove_client(client_socket)
                break
        except:
            remove_client(client_socket)
            break

print(f"✅ Server listening on {HOST}:{PORT}")

while True:
    client_socket, addr = server.accept()
    print(f"🔗 Connected with {addr}")

    nickname = client_socket.recv(1024).decode("utf-8")
    clients.append((client_socket, nickname))

    print(f"👤 Nickname set: {nickname}")
    broadcast(f"🎉 {nickname} joined the chat!")

    thread = threading.Thread(target=handle_client, args=(client_socket, nickname))
    thread.start()
