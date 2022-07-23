import os

class Config(object):
    SECRET_KV = os.environ.get('SECRET_KEY') or "secret_string"

    MONGODB_SETTINGS = { 'db': 'UTA_Enrollment',
                         'host':'mongodb://localhost:27017/UTA_Enrollment'}

