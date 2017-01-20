#pylint: disable=R0201

from wfmastery import App
from . import db
from .crud import CrudAPI
from wfmastery import crud

from flask import render_template
from flask import g
from flask import request
from flask import url_for
from flask import redirect
# from flask import
from flask.views import MethodView





class Equipment(CrudAPI):

    def populate(self):

        self.record_cls = db.Equipment
        self.identity = "equipment"

        self.template_form = "equipment_form.j2.html"
        self.template_list = "equipment_list.j2.html"

        self._listColumn("id")
        self._listColumn("hidden")
        self._listColumn("name", magic_field="magic-string")
        self._listColumn("pretty_name", magic_field="magic-string")

        self._addRelationship("category", "name", magic_field="magic-filter")
        self._addRelationship("subcategory", "name", magic_field="magic-filter")








Equipment.Bind(App)




#Product
@App.route("/")
def index():
    context = {}
    with g.db_scope() as session:
        context['menu_items'] = db.EquipmentCategory.fetch_all(session)
        context['pos2id'], context['id2pos'] = db.Equipment.generate_position_data(session)
        context['manifest'] = session.query(db.EquipmentCategory)
        context['total_size'] = session.query(db.Equipment).count() + session.query(db.Component).count()

        return render_template("index.j2.html", **context)
