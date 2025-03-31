from flask import Flask, request, jsonify, render_template, session
# from flask_socketio import SocketIO, emit
# from dotenv import load_dotenv
# load_dotenv()
import os
import requests
import json
# from keys import endpoint
headers = {'Content-type': 'application/json'}


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'FALLBACK_KEY')
# socketio = SocketIO(app, cors_allowed_origins="*")



endpoint = os.getenv('TRIGGER_ENDPOINT')

# @socketio.on('connect')
# def handle_connect():
#     global active_users
#     active_users += 1
#     emit("user_count", active_users, broadcast=True)

# @socketio.on('disconnect')
# def handle_disconnect():
#     global active_users
#     active_users -= 1
#     emit("user_count", active_users, broadcast=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    response = requests.post(endpoint, data=data, headers=headers)
    return jsonify({"message": "Received!", "data": response})


if __name__ == '__main__':
    app.run(debug=True)

