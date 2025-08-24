import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

SERVER_HOST = "192.168.29.77"
SERVER_PORT = 55556

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

root = tk.Tk()
root.withdraw()
nickname = simpledialog.askstring("Nickname", "Please choose a nickname:")

try:
    client.connect((SERVER_HOST, SERVER_PORT))
    client.send(nickname.encode("utf-8"))
except Exception as e:
    print(f"❌ Connection failed: {e}")
    exit(0)

window = tk.Tk()
window.title(f"Chat App - {nickname}")
window.geometry("500x500")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD)
chat_area.config(state=tk.DISABLED)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry_field = tk.Entry(window)
entry_field.pack(padx=10, pady=5, fill=tk.X)

def send_message():
    msg = entry_field.get()
    entry_field.delete(0, tk.END)
    if msg:
        try:
            client.send(msg.encode("utf-8"))
            chat_area.config(state=tk.NORMAL)
            chat_area.insert(tk.END, f"You: {msg}\n")
            chat_area.config(state=tk.DISABLED)
            chat_area.see(tk.END)
        except:
            client.close()
            window.destroy()

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(padx=10, pady=5)

def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode("utf-8")
            chat_area.config(state=tk.NORMAL)
            chat_area.insert(tk.END, msg + "\n")
            chat_area.config(state=tk.DISABLED)
            chat_area.see(tk.END)
        except:
            client.close()
            break

receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()

# ---------------------------
# Run GUI Loop
# ---------------------------
window.mainloop()
