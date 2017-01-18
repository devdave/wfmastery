#pylint: disable=R0201

from wfmastery import App
from wfmastery import db

from flask import render_template
from flask import g
from flask import request
from flask import url_for
from flask import redirect
# from flask import
from flask.views import MethodView



class CrudAPI(MethodView):

    def __init__(self):
        self.populate()
        self.template_form = getattr(self, "template_form")
        self.template_list = getattr(self, "template_list")
        self.record_cls = getattr(self, "record_cls")
        self.identity = getattr(self, "identity")
        self.base_url = "/{}/".format(self.__class__.__name__.lower())

    @classmethod
    def Bind(cls, app):
        view = cls.as_view(cls.__name__)

        base_url = "/{}/".format(cls.__name__.lower())



        app.add_url_rule(base_url,
                         defaults=dict(record_id=None),
                         view_func=view, methods=['GET'])
        app.add_url_rule(base_url, methods=['POST'], view_func=view)
        app.add_url_rule("{}<int:record_id>".format(base_url),
                         view_func=view,
                         methods=("GET", "PUT", "DELETE",),
                        )





    def populate(self):
        raise NotImplementedError()


    def get_context(self):
        return dict(origin=self, identity=self.identity)

    def get(self, record_id=None):

        context = self.get_context()
        template = ""
        with g.db_scope() as session:
            if record_id is not None:
                context['record_id'] = record_id
                context['record'] = session\
                    .query(self.record_cls)\
                    .filter(self.record_cls.id == record_id).first()

                template = self.template_form
            else:
                context['records'] = session.query(self.record_cls)
                context['record_count'] = context['records'].count()
                form_context = self.get_context()
                form_context['record_id'] = False
                form_context['record'] = self.record_cls()
                context['record_form'] = render_template(self.template_form, **form_context)
                template = self.template_list

            return render_template(template, **context)

    def post(self):
        #new record
        sanitized = request.form
        if "id" in sanitized:
            del sanitized['id']

        with g.db_scope() as session:
            record = self.record_cls(**sanitized)
            session.add(record)

        return redirect(self.identity)


    def delete(self, record_id=None):
        with g.db_scope as session:
            record = session.query(db.Equipment).filter(db.Equipment.id == record_id)[1].delete()

        return redirect(self.identity)


    def put(self, record_id=None):
        sanitized = request.form
        if "id" in sanitized:
            del sanitized['id']

        with g.db_scope as session:
            session\
                .query(db.Equipment)\
                .filter(db.Equipment.id == record_id)\
                .update(**request.form)
            #I want this to blow up before it leaves scope
            session.commit()




class Equipment(CrudAPI):

    def populate(self):
        self.template_form = "equipment_form.j2.html"
        self.template_list = "equipment_list.j2.html"
        self.record_cls = db.Equipment
        self.identity = "equipment"





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
