from flask import Flask
from flask import request
from flask import g

from wfmastery import db

import os


App = Flask(__name__, static_folder="../static")

@App.before_first_request
def app_setup_db():
    if getattr(g, "_database_", None) is None:
        engine, NewTRX = db.boostrap(App.config["DB_PATH"], True, False) #pylint: disable=W0621

        g._database_ = engine #pylint: disable=W0212
        g._new_trx_ = NewTRX #pylint: disable=W0212
        g.db_scope = lambda: db.scope(NewTRX) #pylint: disable=W0212

@App.before_request
def app_setup_db():
    if getattr(g, "_database_", None) is None:
        engine, NewTRX = db.boostrap(App.config["DB_PATH"], True, False) #pylint: disable=W0621

        g._database_ = engine #pylint: disable=W0212
        g._new_trx_ = NewTRX #pylint: disable=W0212
        g.db_scope = lambda: db.scope(NewTRX) #pylint: disable=W0212


def setup_db():
    db_path = os.environ.get("DB_PATH", None)
    assert db_path is not None, "Missing environment DB_PATH"
    assert db_path.endswith(".sqlite3"), "{} MUST end with .sqlite3".format(db_path)
    db_path = os.path.abspath(db_path)
    assert os.path.exists(db_path), "Unable to find {}".format(db_path)

    db_path = "sqlite:///{}".format(db_path)
    App.config["DB_PATH"] = db_path

    #acid test to make sure it works
    # _, NewTRX = db.boostrap(db_path, True, False)
    # with db.scope(NewTRX) as session:
    #     print("Equipment count: {}".format(session.query(db.Equipment).count()))

setup_db()

from wfmastery import views
