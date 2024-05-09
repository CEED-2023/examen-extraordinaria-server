from flask import Blueprint, jsonify
from .chat_storage import chats  # Import chats from chat_storage module

get_chats_bp = Blueprint('get_chats', __name__)

# Endpoint to return a list of chat titles with ids
@get_chats_bp.route('/chats', methods=['GET'])
def get_chats():
    chat_list = [{'id': chat['id'], 'title': chat['title']} for chat in chats]
    return jsonify(chat_list)
