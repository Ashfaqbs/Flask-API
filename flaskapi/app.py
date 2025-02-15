from flask import Flask, request, jsonify
import logging
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)
Config.init_app(app)

# Logging setup
logger = logging.getLogger(__name__)

# API Routes
@app.route('/api/message', methods=['GET'])
def get_message():
    message = request.args.get('message', 'This is a default message.')
    return jsonify({'message': message})

# http://localhost:3031/api/message?message=hello
# {
#     "message": "hello"
# }

# http://localhost:3031/api/message

# {
#     "message": "This is a default message."
# }

@app.route('/api/header-message', methods=['GET'])
def get_message_with_header():
    custom_header = request.headers.get('X-Custom-Header', 'No Custom Header Provided')
    return jsonify({'message': f'Custom header value: {custom_header}'})

# 
#  http://localhost:3031/api/header-message
#  X-Custom-Header:MyHeaderValue
# {
#     "message": "Custom header value: MyHeaderValue"
# }



@app.route('/api/message', methods=['POST'])
def post_message():
    data = request.get_json()
    logger.info(f"Received JSON: {data}")
    return jsonify({'message': 'JSON received successfully', 'data': data}), 201

# req 
# http://localhost:3031/api/message

# {
#   "name": "John",
#   "message": "Hello, World!"
# }

# resp 

# {
#     "data": {
#         "message": "Hello, World!",
#         "name": "John"
#     },
#     "message": "JSON received successfully"
# }



@app.route('/api/message/<id>', methods=['PUT'])
def put_message(id):
    logger.info(f"PUT request with id: {id}")
    return jsonify({'message': f'Updated resource with id: {id}'}), 200

# req
# http://localhost:3031/api/message/123

# resp
# {
#     "message": "Updated resource with id: 123"
# }


@app.route('/api/message/<id>', methods=['DELETE'])
def delete_message(id):
    logger.info(f"DELETE request with id: {id}")
    return jsonify({'message': f'Deleted resource with id: {id}'}), 200
# req
# http://localhost:3031/api/message/123

# resp
# {
#     "message": "Deleted resource with id: 123"
# }

# Run the app
if __name__ == '__main__':
    app.run(port=app.config['PORT'], debug=True)

# Run the app with the following command: python app.py
