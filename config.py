import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = "hello_world"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "test.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

# Calls the Config object out of the dictionary when "default" is called.
#

config = {"default": Config}