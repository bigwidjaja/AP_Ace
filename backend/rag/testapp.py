from flask import Flask, request, jsonify
from flask_cors import CORS
from create_database import generate_data_store
import read_file
import subprocess

app = Flask(__name__)
CORS(app) 

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
    class_name = userClass[0]
    unit_name = userClass[1] 
    print(f"Class Name: {class_name}, Unit Name: {unit_name}")
    
    try:
        read_file.process_class(class_name) 
        return jsonify({"message": "Data processed successfully"}), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500
    


    

if __name__ == '__main__':
    subprocess.run(["python3", "readfile.py"])
    subprocess.run(["python3", "create_database.py"])
    subprocess.run(["python3", "query_data.py"])
    print("Starting Flask server on http://localhost:5001")
    app.run(debug=True, host='0.0.0.0', port=5001)

    