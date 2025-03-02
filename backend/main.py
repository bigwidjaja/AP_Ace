from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    print("Home route accessed!")
    return "Hello, World! Your Flask app is running."

@app.route('/api/hello')
def hello():
    print("API hello route accessed!")
    return jsonify({"message": "Hello from Flask!"})

@app.route('/api/getClass', methods=['POST'])
def getClass():
    userClass = request.json
    print(userClass)
    return jsonify("Good")

if __name__ == '__main__':
    print("Starting Flask server on http://localhost:5001")
    app.run(debug=True, host='0.0.0.0', port=5001)
