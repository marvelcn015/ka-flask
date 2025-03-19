from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    print("GET /")
    return render_template('index.html')

@app.route('/status', methods = ['GET'])
def status():
    return jsonify({"status" : "running", "version" : "1.0"})

@app.route('/submit', methods = ['POST'])
def submit():
    data = request.json
    name = data.get("name")
    if not name:
        return jsonify({"message" : "offer name!"}), 400
    return jsonify({"message" : f"receive name {name}"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), host='0.0.0.0')
