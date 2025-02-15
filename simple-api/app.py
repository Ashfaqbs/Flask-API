# app.py
from flask import Flask,jsonify
#Flask  is the core of the Flask web framework. It creates the web application.
# jsonify is a function that converts a Python dictionary into a JSON response.
# Initialize the Flask application
app = Flask(__name__)
# Initializes a Flask application. The __name__ tells Flask whether this is the main program or if it's imported as a module.

# Define the API endpoint with a path variable
@app.route('/message/<message>', methods=['GET'])
def get_message(message):
    """
    This function receives a message via the path variable
    and returns it as part of a JSON response.
    """
    return jsonify({"message": message})

# http://localhost:5000/message/hello

# {
#   "message": "hello"
# }

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
    

# run 
# pip install -r requirements.txt
# python app.py
