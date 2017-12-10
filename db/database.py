import json
from models.models import *

class Database(object):
    def __init__(self):
        self.loaded_db = None
        self.db_file = 'mockdb.json'

        self.risk_types = []
        self.fields = []
        self.types = []
        self.enums = []
        self.numbers = []
        self.texts = []
        self.dates = []

        self.loadDB()

    def loadDB(self):
        self.loaded_db = json.load(open(self.db_file))
        self.loadRiskTypes()
        self.loadFields()
        self.loadTypes()
        self.loadEnums()
        self.loadNumbers()
        self.loadTexts()
        self.loadDates()

    def loadRiskTypes(self):
        risk_types = self.loaded_db['risk_types']
        for rt in risk_types:
            rt_object = RiskType(id=rt['id'], name=rt['name'], fields=rt['fields'])
            self.risk_types.append(rt_object)

    def loadFields(self):
        fields = self.loaded_db['fields']
        for f in fields:
            f_object = Field(id=f['id'], name=f['name'], type_id=f['type_id'])
            self.fields.append(f_object)

    def loadTypes(self):
        types = self.loaded_db['types']
        for t in types:
            t_object = Type(parent_id=t['id'], type=t['type'])
            self.types.append(t_object)

    def loadEnums(self):
        enums = self.loaded_db['enums']
        for e in enums:
            e_object = Enum(id=e['id'], selected_index=e['selected_index'], subtype_ids=e['subtype_ids'], type_id=e['type_id'])
            self.enums.append(e_object)

    def loadNumbers(self):
        numbers = self.loaded_db['numbers']
        for n in numbers:
            n_object = Number(id=n['id'], value=n['value'], type_id=n['type_id'])
            self.numbers.append(n_object)

    def loadTexts(self):
        texts = self.loaded_db['texts']
        for t in texts:
            t_object = Text(id=t['id'], value=t['value'], type_id=t['type_id'])
            self.texts.append(t_object)

    def loadDates(self):
        dates = self.loaded_db['dates']
        for d in dates:
            d_object = Date(id=d['id'], value=d['value'], type_id=d['type_id'])
            self.dates.append(d_object)

    def getRiskType(self, id):
        for risk_type in self.risk_types:
            if int(risk_type.id) == int(id):
                return risk_type

        return None

    def getField(self, id):
        for field in self.fields:
            if int(field.id) == int(id):
                return field

        return None

    def getTypeById(self, id):
        for t in self.types:
            if int(t.parent_id) == int(id):
                return self.getType(id, t.type)

        return None

    def getType(self, id, type):
        if type == "enum":
            return self.getEnum(id)

        if type == "number":
            return self.getSubtype(id, self.numbers)

        if type == "text":
            return self.getSubtype(id, self.texts)

        if type == "date":
            return self.getSubtype(id, self.dates)


    def getSubtype(self, type_id, items):
        for item in items:
            if int(type_id) == int(item.parent_id):
                return item.toJSON()

        return None

    def getEnum(self, type_id):
        data = {}
        for enum in self.enums:
            if int(type_id) == int(enum.parent_id):
                data = enum.toJSON()
                data["options"] = []
                for st_id in enum.subtype_ids:
                    st = self.getTypeById(st_id)
                    data["options"].append(st)

                return data



