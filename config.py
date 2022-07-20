import os

class Config(object):
    SECRET_KV = os.environ.get('SECRET_KEY') or "secret_string"
