from flask import Flask

app = Flask(__name__)

import api.van_ban_den.van_ban_den_api

@app.route('/')
def hello_world():
    return 'Hello World!'
