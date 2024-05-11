from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

from endpoints import chats_bp

app = Flask(__name__)

# Allow CORS for local development
cors = CORS(app,
    resources={
        r"/*": {
            "origins": [
                "http://localhost:*",
                "https://ceedgpt.netlify.app/"
            ]
        }
    })

# Register endpoints
app.register_blueprint(chats_bp)

if __name__ == '__main__':
    app.run(debug=True)
