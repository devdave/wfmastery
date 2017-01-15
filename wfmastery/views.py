#pylint: disable=R0201

from wfmastery import App
from wfmastery import db

from flask import render_template
from flask import g
# from flask import
from flask.views import MethodView



class EquipmentAPI(MethodView):

    def get(self, record_id):
        if record_id is None:
            records = db.manifest()
        else:
            #try to get record
            record = db.fetch(record_id)
            #let exceptions blow all the way up



    def post(self):
        #updating a record

        try:
            record = db.update(request.form)
        except InputError as ex:
            #or trying to
            pass

    def put(self, record_id):
        #wanted to use HTTP PATCH but I guess that's not happening
        #update a record
        pass

    def delete(self, record_id):
        #I wonder what this does
        pass


equipment_view = EquipmentAPI.as_view("records")
App.add_url_rule("/records/",
                 defaults=dict(record_id=None),
                 view_func=equipment_view,
                 methods=["GET"])

App.add_url_rule("/records/",
                 view_func=equipment_view,
                 methods=["POST"])

App.add_url_rule("/records/<int:record_id>",
                 view_func=equipment_view,
                 methods=["GET", "PUT", "DELETE"])



#Product
@App.route("/")
def index():
    with g.db_scope() as session:
        count = session.query(db.Equipment).count().scalar()

    return "Hello world - {}".format(count)
    # return render_template("views/index.html")
