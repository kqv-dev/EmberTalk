from flask import Flask
from flask_socketio import SocketIO
import random
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Create an instance

@app.route('/')
def get_messages():
    return 'Hello, Flask!'

def send_random_numbers():
    while True:
        number = random.randint(1, 100)
        socketio.emit('message', {'value': number})  # Use the instance
        time.sleep(2)

@socketio.on('connect')  # Use the instance
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    # Start the background thread to emit random numbers
    thread = threading.Thread(target=send_random_numbers)
    thread.daemon = True
    thread.start()
    socketio.run(app, debug=True)  # Use the instance