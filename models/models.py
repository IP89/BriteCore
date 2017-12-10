from datetime import datetime

class RiskType(object):
    name = None
    id = None
    fields = []

    def __init__(self, name, id, fields=[]):
        self.id = id
        self.name = name
        self.fields = fields

    def toJSON(self):
        return { "name": self.name }

class Field(object):
    name = None
    id = None
    type_id = []

    def __init__(self, name, type_id, id):
        self.id = id
        self.name = name
        self.type_id = type_id

    def toJSON(self):
        return { "name": self.name }

class Type(object):
    parent_id = None
    type = None

    def __init__(self, parent_id, type):
        self.parent_id = parent_id
        self.type = type

class Text(Type):
    id = None
    value = None

    def __init__(self, value, id, type_id):
        self.id = id
        self.value = value
        Type.__init__(self, type_id, "text")

    def toJSON(self):
        return { "type": "text", "value": self.value }

class Number(Type):
    id = None
    value = None

    def __init__(self, value, id, type_id):
        self.id = id
        self.value = float(value)
        Type.__init__(self, type_id, "number")

    def toJSON(self):
        return { "type": "number", "value": self.value }

class Date(Type):
    id = None
    value = None

    def __init__(self, value, id, type_id):
        self.id = id
        self.value = value
        Type.__init__(self, type_id, "Date")

    def toJSON(self):
        return { "type": "date", "value": self.value }

class Enum(Type):
    id = None
    selected_index = None
    subtype_ids = []

    def __init__(self, id, type_id, selected_index=None, subtype_ids=[]):
        self.id = id
        self.selected_index = selected_index
        self.subtype_ids = subtype_ids
        Type.__init__(self, type_id, "Enum")

    def toJSON(self):
        return { "type": "enum", "n_options": len(self.subtype_ids), "selected_index": self.selected_index }


