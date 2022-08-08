from flask import Flask
from flask_pymongo import pymongo
from application import app
from flask_pymongo import PyMongo

CONNECTION_STRING = "mongodb+srv://mdoneadmin:KnzpLMfrOWC8bTJ8@cluster0.tr9gahr.mongodb.net/MDone_Enrollment"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongodb_atlas')
user_collection = pymongo.collection.Collection(db, 'user')
task_collection = pymongo.collection.Collection(db, 'task')
enrollment_collection = pymongo.collection.Collection(db, 'enrollment')
course_collection = pymongo.collection.Collection(db, 'course')

app.config["MONGO_URI"] = "mongodb+srv://mdoneadmin:KnzpLMfrOWC8bTJ8@cluster0.tr9gahr.mongodb.net/MDone_Enrollment"
mongo = PyMongo(app)
