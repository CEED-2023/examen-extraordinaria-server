from flask import Blueprint, jsonify, request

completions_bp = Blueprint('completions', __name__)

# Endpoint to generate a response
@completions_bp.route('/chat/completions', methods=['POST'])
def completions():
    data = request.json

    if not data or 'messages' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    messages = data['messages']

    # Process messages using the specified model and return a response
    response = process_messages(messages)

    return jsonify({'message': response})


def process_messages(model, messages, temperature):
    # This is a placeholder function.
    # You would use the specified model to generate a response based on the given messages.
    # For demonstration purposes, it simply echoes back the first message.

    if messages:
        first_message = messages[0]
        role = first_message.get('role', 'user')
        content = first_message.get('content', '')

        if role == 'user':
            return {'role': 'assistant', 'content': f'\n\n{content}'}

    return {'error': 'No message provided or invalid message format'}
