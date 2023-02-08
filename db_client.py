from flask_pymongo import PyMongo
from app import app;

app.config["MONGO_URI"] = "mongodb://localhost:27017/quan_ly_van_ban_db"

mongodb_client = PyMongo(app)
db = mongodb_client.db


