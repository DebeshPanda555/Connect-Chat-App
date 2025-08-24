# client.py
import socket
import threading

SERVER_HOST = '127.0.0.1'  # change to server's LAN IP for multi-device
SERVER_PORT = 55556

nickname = input("Choose a nickname: ").strip() or "Guest"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_HOST, SERVER_PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                print("Disconnected from server.")
                break
            if message == "NICK":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Connection error.")
            client.close()
            break

def send():
    while True:
        try:
            text = input()
            if text.lower() in {"quit", "exit"}:
                client.close()
                break
            message = f"{nickname}: {text}"
            client.send(message.encode('utf-8'))
        except:
            break

if __name__ == "__main__":
    threading.Thread(target=receive, daemon=True).start()
    send()