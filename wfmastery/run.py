"""
    on the list to do, tell pylint not everything needs a docstring
"""

import sys
import os

from flask import request
from flask import g

from wfmastery import App
import db








if __name__ == '__main__':

    db_path = os.environ.get("DB_PATH", None)
    assert db_path is not None
    assert db_path.endswith(".sqlite3"), db_path
    db_path = os.path.abspath(db_path)
    assert os.path.exists(db_path), db_path

    db_path = "sqlite:///{}".format(db_path)
    App.config["DB_PATH"] = db_path

    #acid test to make sure it works
    engine, NewTRX = db.boostrap(db_path, True, False)
    print(engine.query(db.f.count(db.Equipment)))

    App.run()

