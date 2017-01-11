"""
    on the list to do, tell pylint not everything needs a docstring
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("views/index.html")


