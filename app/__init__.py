# Why do I keep forgetting what a dunder does?  Let's look it up!
# In this sense (__init__.py) it is called when a "package" (the directory it's in)
# and label and variables inside of the package.

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config
import datetime

from . import auth
from . import blog
from . import main

bootstrap = Bootstrap()
#db = SQLAlchemy()

# make the factory function that will accept different configs to produce different apps.
def create_app(config_name = "default"):
    app = Flask(__name__)

    # import config settings
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #initilize extensions
    bootstrap.init_app(app)

    from app.models import db
    db.init_app(app)

    # register blueprints
    from .auth import auth
    app.register_blueprint(auth)

    from .blog import blog
    app.register_blueprint(blog)

    from .main import main
    app.register_blueprint(main)

    return app