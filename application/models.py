import flask
from application import db
import mongo
#from Task import Task
from werkzeug.security import generate_password_hash, check_password_hash

class User(mongo.Document):
    user_id     =   db.IntField( unique=True )
    first_name  =   db.StringField( max_length=50 )
    last_name   =   db.StringField( max_length=50 )
    email       =   db.StringField( max_length=30, unique=True )
    password    =   db.StringField( )
    position    =   db.StringField( )

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)

class Course(mongo.Document):
    courseID    =   db.StringField( max_length=10, unique=True )
    title       =   db.StringField( max_length=100 )
    description =   db.StringField( max_length=255 )
    credits     =   db.IntField()
    term        =   db.StringField( max_length=25 )

class Enrollment(mongo.Document):
    user_id     =   db.IntField()
    taskID      =   db.IntField( max_length=10 )



class comment(mongo.Document):
    commentID   =   db.IntField( unique=True )
    taskID      =   db.IntField()
    user_ID     =   db.IntField()
    time        =   db.DateTimeField()
    comment     =   db.StringField( max_length=255 )

