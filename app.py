from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

active_users = 0

@socketio.on('connect')
def handle_connect():
    global active_users
    active_users += 1
    emit("user_count", active_users, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    global active_users
    active_users -= 1
    emit("user_count", active_users, broadcast=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    return jsonify({"message": "Received!", "data": data})

if __name__ == '__main__':
    app.run(debug=True)

