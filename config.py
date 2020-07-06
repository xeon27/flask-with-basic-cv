import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'maybe-you-are-right'
    IMAGE_FOLDER = 'app/static/images/'