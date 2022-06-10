
from flask import Blueprint

auth_app = Blueprint('auth', __name__)


from .services import *
from .controller import *
from hooks import app_init


@app_init.connect
def setup(app, **kwargs):
    print('-'*20 + 'Auth' + '-' * 20 )
    db.create_all()
    # add_user('admin','mehdi','root','roo@email.com')
