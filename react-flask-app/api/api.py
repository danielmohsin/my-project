import time
import random
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='../build', static_url_path='/')
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/api/time')
def get_current_time():
    return jsonify({'unix_time': int(time.time())})  # Return Unix time as an integer

@app.route('/api/random')
def random_number():
    random_int = random.randint(1, 100)  # Generate a random integer between 1 and 100
    return jsonify({'random_int': random_int})

if __name__ == '__main__':
    app.run(debug=True)

