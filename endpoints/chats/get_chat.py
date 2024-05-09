from flask import Blueprint, jsonify
from .chat_storage import chats  # Import chats from chat_storage module

get_chat_bp = Blueprint('get_chat', __name__)

# Endpoint to return the list of messages for a specific chat
@get_chat_bp.route('/chat/<int:chat_id>', methods=['GET'])
def get_chat(chat_id):
    chat = next((chat for chat in chats if chat['id'] == chat_id), None)
    if chat:
        return jsonify(chat['messages'])
    else:
        return jsonify({'error': 'Chat not found'}), 404
