
from enum import Enum

class Simple(Enum):
    string = 0
    integer = 0
    text = 0

def parse_table(record_cls):
    obj = record_cls()
    table = obj.__table__

    relationships = {}
    columns = {}
    foreign_keys = {}
    #assume there are no composite primary keys... please
    primary_key_name, primary_key_column = table.primary_key.columns.items()[0]

    for key, column in table.columns.items():
        if column.foreign_keys:
            foreign_keys[key] = column
        else:
            columns[key] = column
