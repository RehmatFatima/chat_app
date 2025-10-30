from flask import Flask, render_template
from flask_socketio import SocketIO, send
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# Simple bot replies
bot_replies = [
    "Hey there! 👋",
    "How's your day going?",
    "That sounds interesting!",
    "Can you tell me more?",
    "Haha, good one 😂",
    "I'm just a bot, but I'm learning fast!",
    "Let's keep chatting 💬"
]

@socketio.on('message')
def handle_message(data):
    username = data['username']
    message = data['message']
    print(f"{username}: {message}")

    # Broadcast user's message
    send({'username': username, 'message': message}, broadcast=True)

    # Make the bot reply (only if it's not the bot itself)
    if username.lower() != "chatbot":
        bot_msg = random.choice(bot_replies)
        socketio.sleep(1)  # small delay to make it feel natural
        send({'username': "ChatBot 🤖", 'message': bot_msg}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
