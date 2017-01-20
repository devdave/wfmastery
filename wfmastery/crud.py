
from wfmastery import App
from . import db
from flask.views import MethodView

from flask import render_template
from flask import g
from flask import request
from flask import url_for
from flask import redirect


class CrudAPI(MethodView):

    def __init__(self):

        #TODO remind me if shit is missing
        self.list_columns = []
        self.magic_columns = {}
        self.relationships = []

        self.template_form = "equipment_form.j2.html"
        self.template_list = "crud_list.j2.html"
        self.record_cls = None
        self.indentity = None

        self.populate()

        assert len(self.list_columns) > 0, "No list_columns have been assigned"
        assert self.template_form is not None
        assert self.template_list is not None
        assert self.record_cls is not None
        assert self.identity is not None

        #change to identity?
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
                # context['record_form'] = render_template(self.template_form, **form_context)
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


    def _listColumn(self, name, magic_field=False):
        """
            shook my head when I realized Javascripts naming convention (lowerUpperWord)
            is spreading out
        """
        self.list_columns.append(name)
        if magic_field is not False:
            self.magic_columns[name] = magic_field

    def _addRelationship(self, record_name, field_value, field_id = "id", magic_field=False):
        """

        """
        relationship = dict(
            name=record_name,
            path="{}.{}".format(record_name, field_value),
            path_id="{}.{}".format(record_name, field_id),
            wtf="who_is_setting_this"
        )

        if magic_field is not False:
            self.magic_columns[record_name] = magic_field

        self.relationships.append(relationship)


@App.template_filter("hijack_thread")
def hijack_thread(context, *args, **kwargs):
    #this kills the flask
    from dbgp.client import brk
    brk(port=51165)
    return ""

#TODO make my own decorator for this
hijack_thread.contextfilter = True

@App.template_filter("dict2attrs")
def dict_to_attributes(attributes, prefix=None):
    results = []
    name2dash = lambda *x: "-".join(x)
    format_str = "%s-{}=\"{}\"" % prefix if prefix else "{}=\"{}\""

    for key, value in attributes.items():
        results.append(format_str.format(key, value))

    #TODO disable autoescape
    return " ".join(results)

@App.template_filter("render_header")
def render_header(context, column_name, value="", **kwargs):
    """
        {%-          if column_name in origin.magic_columns -%}
                {{ cell("", column_name|title, classes=origin.magic_columns[column_name]) -}}
        {%-          else -%}
                {{ cell("", column_name|title) -}}
        {%          endif %}
    """
    result = ""
    if column_name in context['origin'].magic_columns:
        result = context['cell'](value, column_name.capitalize(), classes=context['origin'].magic_columns[column_name])
    else:
        result = context['cell'](value, column_name.capitalize())


    return result

render_header.contextfilter=True


@App.template_filter("dotpath")
def dotpath(path, record):

    path_chain = path.split(".")
    result = record
    while len(path_chain):
        attribute = path_chain.pop(0)
        result = getattr(result, attribute)

    return result
