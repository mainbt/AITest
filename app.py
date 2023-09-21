import numpy as np
import streamlit as st
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def home():
    #data = request.files['file']
    result = {"result": "helu"}
    return jsonify(result)

if __name__ == '__main__':
    app.run()