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

from schema import SCHEMA_MAP





def startup(cleaned=False, working_dir=None):
    """
        Creates a new
    """

    working_dir = working_dir or abspath(dirname(__file__))
    working_file = join(working_dir, "equipment.sqlit3")

    conn = sqlite3.connect(working_file)
    #TODO assert/test this is kosher

    if cleaned is True:
        for table_name, table_schema in SCHEMA_MAP.items():
            conn.execute("DROP TABLE IF EXISTS {}".format(table_name))
            conn.execute(table_schema)

    return conn
