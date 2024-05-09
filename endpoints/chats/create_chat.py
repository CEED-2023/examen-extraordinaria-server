from flask import Blueprint, jsonify, request
from .chat_storage import chats  # Import chats from chat_storage module

create_chat_bp = Blueprint('create_chat', __name__)

# Endpoint to create a new chat
@create_chat_bp.route('/chat/new', methods=['POST'])
def create_chat():
    data = request.json
    if not data or 'messages' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    new_chat = {
        'id': len(chats) + 1,
        'title': f'Chat {len(chats) + 1}',
        'messages': data['messages']
    }
    chats.append(new_chat)
    return jsonify(new_chat), 201
