#pylint: disable=R0201

from wfmastery import App
from wfmastery import db

from flask import render_template
from flask import g
from flask import url_for
# from flask import
from flask.views import MethodView


crud_map = dict(
    equipment=dict(
        title="Equipment",
        record_cls=db.Equipment,
        list_fields=["TODO"],
        template_list="crud_list.j2.html",
        template_form="crud_form.j2.html",

    )
)

class CrudAPI(MethodView):

    def __init__(self, **kwargs):

        self.identity = None
        self.title = None
        self.template_list = None
        self.list_fields = None
        self.template_form = None
        self.record_cls = None

        expected_fields = "identity,title,template_list,list_fields,template_form,record_cls".split(",")

        defaults = dict(
            template_list="crud_list.j2.html",
            template_form="crud_form.j2.html"
        )



        for expected in expected_fields:
            value = kwargs.get(expected, defaults.get(expected, None))
            if value is not None:
                setattr(self, expected, value)
            else:
                raise Exception("Missing {}".format(expected))

        self.record_meta = self.record_cls.My_meta()

    def get_context(self, **kwargs):
        kwargs['origin'] = self
        return kwargs


    def get(self, record_id=None):
        template = ""
        context = self.get_context()
        form_context = self.get_context(new_form=True, record_cls=self.record_cls)


        with g.db_scope() as session:
            if record_id is None:
                #list
                template = self.template_list
                context['records'] = session.query(self.record_cls).order_by(self.record_cls.id)

                context['form_body'] = render_template(self.template_form, **form_context)#pylint: disable=E1102,E1121

            else:

                template = self.template_form
                form_context['record'] = session.query(self.record_cls).filter(self.record_cls.id == record_id)
                form_context['new_form'] = False
                context = form_context

            # from dbgp.client import brk
            # brk(port=51165)


            return render_template(template, **context)




views = {}
for view_name, view_recipe in crud_map.items():
    if "identity" not in view_recipe:
        view_recipe['identity'] = view_name

    views[view_name] = CrudAPI.as_view(view_name, **view_recipe)
    App.add_url_rule("/{}/".format(view_name),
                     defaults=dict(record_id=None),
                     view_func=views[view_name],
                     methods=["GET"])

    App.add_url_rule("/{}/".format(view_name),
                     view_func=views[view_name],
                     methods=["POST"])

    App.add_url_rule("/{}/<int:record_id>".format(view_name),
                     view_func=views[view_name],
                     methods=["GET", "PUT", "DELETE"])



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
