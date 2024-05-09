from flask import Blueprint
from .chats.get_chats import get_chats_bp
from .chats.get_chat import get_chat_bp
from .chats.create_chat import create_chat_bp

from .completions.completions import completions_bp

# Register blueprints for chats endpoints
chats_bp = Blueprint('chats', __name__)
chats_bp.register_blueprint(get_chats_bp)
chats_bp.register_blueprint(get_chat_bp)
chats_bp.register_blueprint(create_chat_bp)

chats_bp.register_blueprint(completions_bp)
