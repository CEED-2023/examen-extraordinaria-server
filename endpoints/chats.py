from flask import Blueprint, jsonify, request

chats_bp = Blueprint('chats', __name__)

# In-memory database to store chats
chats = []

# Endpoint to return a list of chat titles with ids
@chats_bp.route('/chats', methods=['GET'])
def get_chats():
    chat_list = [{'id': chat['id'], 'title': chat['title']} for chat in chats]
    return jsonify(chat_list)

# Endpoint to return the list of messages for a specific chat
@chats_bp.route('/chat/<int:chat_id>', methods=['GET'])
def get_chat(chat_id):
    chat = next((chat for chat in chats if chat['id'] == chat_id), None)
    if chat:
        return jsonify(chat['messages'])
    else:
        return jsonify({'error': 'Chat not found'}), 404

# Endpoint to create a new chat
@chats_bp.route('/chat/new', methods=['POST'])
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
