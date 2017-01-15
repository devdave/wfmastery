"""
    on the list to do, tell pylint not everything needs a docstring
"""


from app import App
import db






if __name__ == '__main__':
    db.boostrap("sqlite:///test.db", True)
    # App.run()
