from app import create_app
from app.models import db, User, Post
from flask_migrate import Migrate

app = create_app('default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Post=Post)