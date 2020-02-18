from flask import Flask
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
socketio = SocketIO(app)


@socketio.on('connect')
def test_connect():
    pass


@socketio.on('disconnect')
def test_disconnect():
    pass


@socketio.on('move')
def move(json):
    pass


if __name__ == '__main__':
    socketio.run(app)
    