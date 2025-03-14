from flask import Flask, jsonify, render_template
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

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), host='0.0.0.0')
