import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Document):
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

class Course(db.Document):
    courseID    =   db.StringField( max_length=10, unique=True )
    title       =   db.StringField( max_length=100 )
    description =   db.StringField( max_length=255 )
    credits     =   db.IntField()
    term        =   db.StringField( max_length=25 )

class Enrollment(db.Document):
    user_id     =   db.IntField()
    courseID    =   db.StringField( max_length=10 )

class Task(db.Document):
    taskID      =   db.IntField( unique=True )
    title       =   db.StringField( max_length=100 )
    description =   db.StringField(max_length=255)
    phases      =   db.IntField()
    deadline    =   db.DateField()
    fileLink    =   db.URLField()
    complete    =   db.BooleanField()

class comment(db.Document):
    commentID   =   db.IntField( unique=True )
    taskID      =   db.IntField()
    user_ID     =   db.IntField()
    time        =   db.DateTimeField()
    comment     =   db.StringField( max_length=255 )

