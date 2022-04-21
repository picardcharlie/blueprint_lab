# python -m pytest tests/

import pytest
from app import create_app
from app.models import db, User

@pytest.fixture(scope='session')
def new_app():
    #setup
    app = create_app("testing")
    assert 'data_test.sqlite' in app.config['SQLALCHEMY_DATABASE_URI']
    test_client = app.test_client()

    ctx = app.app_context()
    ctx.push()
    db.create_all()

    #start test
    yield test_client

    #cleanse the data
    db.session.remove()
    db.drop_all()
    ctx.pop()


