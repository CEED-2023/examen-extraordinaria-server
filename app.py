from flask import Flask
from endpoints import chats_bp

app = Flask(__name__)

# Register blueprint for chats endpoints
app.register_blueprint(chats_bp)

if __name__ == '__main__':
    app.run(debug=True)
