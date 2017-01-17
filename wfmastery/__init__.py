from flask import Flask
from flask import request
from flask import g

from wfmastery import db

import os


App = Flask(__name__, static_folder="../static")


def setup_db():
    if getattr(g, "_database_", None) is None:
        engine, NewTRX = db.quick_start(os.environ.get("DB_PATH"))
        setattr(g, "_db_engine_", engine)
        # g._db_engine_ = engine #pylint: disable=W0212
        setattr(g, "_session_maker_", NewTRX)

def new_db_session():
    if hasattr(g, "_database_") is False:
        setup_db()

    if hasattr(g, "db_scope"):
        g.db_scope.remove()
        del g.db_scope

    g.db_scope = lambda: db.scope(lambda: db.scoped_session(g._session_maker_)) #pylint: disable=W0212




def close_db_session(response):

    if hasattr(g, "db_scope"):
        delattr(g, "db_scope")

    return response



def cleanup_db(exception=None):
    if hasattr(g, "_db_engine_"):
        delattr(g, "_db_engine_")

    if hasattr(g, "_session_maker_"):
        delattr(g, "_session_maker_")


App.before_first_request(setup_db)
App.before_request(new_db_session)
App.after_request(close_db_session)
App.teardown_appcontext(cleanup_db)

from . import views
from . import cmds

