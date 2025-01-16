from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_connection


app = Flask(__name__)

CORS(app)


if __name__ == '__main__':
    app.run(debug=True) 
