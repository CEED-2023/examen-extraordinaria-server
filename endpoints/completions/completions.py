from flask import Blueprint, jsonify, request
from .invoke_LLM import invoke_LLM

completions_bp = Blueprint('completions', __name__)

# Endpoint to generate a response
@completions_bp.route('/chat/completions', methods=['POST'])
def completions():
    data = request.json

    if not data or 'messages' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    messages = data['messages']

    # Process messages using the specified model and return a response
    try:
        response = process_messages(messages)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': response})


def process_messages(messages):
    if messages and isinstance(messages, list):
        return invoke_LLM(messages)
    else:
        return {'error': 'No message provided or invalid message format'}
