from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import api.van_ban_den.van_ban_den_api

@app.route('/')
def hello_world():
    return 'Hello World!'
