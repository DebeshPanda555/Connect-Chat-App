Python Multi-Client Chat Application
This project is a versatile, real-time chat application built in Python. It features a robust server that supports multiple types of clients: a terminal-based client for command-line enthusiasts, a graphical user interface (GUI) client for a more traditional desktop experience, and a web-based client for accessibility from any browser.

🌟 Core Features
Multi-Client Support: Connect to the same chat server using a terminal, a dedicated GUI application, or a web browser.

Real-Time Communication: Utilizes Python's socket library for instant message delivery.

Centralized Server: A single threaded server (server.py) manages all connections and message broadcasting.

Private Messaging: Send direct messages to specific users.

User List: View a list of all users currently online in the chat room.

Colored Terminal Output: The terminal client (client.py) uses ANSI escape codes to color-code usernames for better readability.

📂 Project Structure
server.py: The main chat server that handles all incoming connections and messages.

client.py: A command-line client for interacting with the chat server.

gui_client.py: A graphical client built with Tkinter.

web_server.py: A Flask and SocketIO server to host the web-based chat interface.

templates/chat.html: (Assumed) The HTML file for the web client, used by web_server.py.

🛠️ Getting Started
Follow these instructions to get the chat application running on your local machine.

Prerequisites
You will need Python 3.x installed. You will also need to install Flask and Flask-SocketIO for the web client.

pip install Flask Flask-SocketIO

Installation
Clone the repository or download the files into a single directory.

If you are running the web_server.py, make sure you have a templates folder with a chat.html file inside it.

⚙️ How to Use
There are two main components to run: the Chat Server and one or more Clients. The Web Server is an optional, separate component.

Part 1: The Core Chat (Terminal and GUI)
1. Start the Main Chat Server
First, run the main server. This will listen for connections from the terminal and GUI clients.

python server.py

You should see the output: ✅ Server listening on 0.0.0.0:55556

2. Connect with a Client (Choose one or both)
Option A: Terminal Client

Open a new terminal and run client.py. You will be prompted to choose a nickname.

python client.py

Option B: GUI Client

Open another new terminal and run gui_client.py. A pop-up window will ask for your nickname.

python gui_client.py

Note: You can run multiple instances of client.py and gui_client.py to simulate a chat room with many users.

Part 2: The Web Chat
The web chat operates independently with its own server.

1. Start the Web Server
In a new terminal, run the Flask-based web server.

python web_server.py

This will start a web server, typically on port 5000.

2. Connect from a Browser
Open your web browser and navigate to http://localhost:5000 or http://127.0.0.1:5000. You will see the web chat interface and can start sending messages.

📜 Available Commands (Terminal & GUI)
/users: Lists all users currently connected to the chat server.

/msg <nickname> <message>: Sends a private message to the specified user.

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request
