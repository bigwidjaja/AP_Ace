from flask import Flask, request, jsonify
from flask_cors import CORS
from create_database import generate_data_store

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

    class_name = userClass[0]
    unit_name = userClass[1]
    print(f"Class Name: {class_name}, Unit Name: {unit_name}")

    try:
        num_chunks = generate_data_store()
        return jsonify({"message": "Data processed successfully", "chunks_saved": num_chunks}), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500
    

if __name__ == '__main__':
    print("Starting Flask server on http://localhost:5001")
    app.run(debug=True, host='0.0.0.0', port=5001)
