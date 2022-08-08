from flask import Flask
# from config import Config
from flask_pymongo import PyMongo
#from db import db
from flask_restx import Api

app = Flask(__name__)

# db = MongoEngine()
#db.init_app(app)
api = Api()
api.init_app(app)

@app.route("/test")
def test():
    mongo.db.collection.insert_one({"name": "John"})
    return "Connected to the data base!"

from application import routes

