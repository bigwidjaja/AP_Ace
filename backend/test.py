from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/artistswhocansing', methods=['GET', 'POST'])
def getHello():
    example = request.json
    print("Example received")
    print(example)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
