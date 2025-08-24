from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Received Message: {msg}")
    send(msg, broadcast=True)  # Broadcasts to all clients

if __name__ == '__main__':
    # Replace 0.0.0.0 with your local IP if you want to connect phone
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)