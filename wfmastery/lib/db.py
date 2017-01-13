# pylint: disable=C0301
"""
    Consolidate database logic.

    Briefly considered using peewee or such but seems excessive when
    all I really need is a list but given how shit works I am going to end up with
    a many to many with a join table in the middle that is linked to
    child join tables that uses natural keys.
"""

from os.path import dirname, abspath, join
import sqlite3


class InputError(Exception):
    pass


class DB(object):

    def __init__(self, schema_map, cleaned=False, working_dir=None):

        self.schema_map = schema_map
        self.working_dir = working_dir or abspath(dirname(__file__))
        self.working_file = join(working_dir, "equipment.sqlit3")

        self.conn = sqlite3.connect(self.working_file)


        if cleaned is True:
            for table_name, table_schema in self.schema_map.items():
                self.conn.execute("DROP TABLE IF EXISTS {}".format(table_name))
                self.conn.execute(table_schema)


    def fetch_manifest(self, table_name, key_field, order_by=None, *concat_fields):
        cursor = self.conn.cursor()
        order_by = order_by or key_field
        if len(concat_fields) == 0:
            raise Exception("Provide atleast one table 'field' argument")

        select_fields = ",".join(concat_fields)
        for row in cursor.execute("SELECT {},{} FROM {} ORDER_BY {}".format(key_field, select_fields, table_name, order_by)):
            yield row

    def update_record(self, table_name, data, **kwargs):
        if "id" not in kwargs:
            raise Exception("expected record id as id=#")


    def delete_record(self, table_name, id=None):
        pass

    def create_record(self, data):
        pass
