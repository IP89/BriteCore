from db import database
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

db = database.Database()

risk_types_blueprint = Blueprint('risk_types', __name__)

@risk_types_blueprint.route('/risk_types', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_all():
    risk_types_info = []

    for risk_type in db.risk_types:
        risk_types_info.append(buildRiskTypesInfo(risk_type))

    return jsonify(risk_types_info), 200


@risk_types_blueprint.route('/risk_types/<risk_type_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get(risk_type_id):
    risk_types_info = buildRiskTypesInfo(db.getRiskType(risk_type_id))
    return jsonify(risk_types_info), 200

def buildRiskTypesInfo(risk_type):
    if not risk_type:
        return None

    info = {
        "name": risk_type.name,
        "fields": []
    }

    for field_id in risk_type.fields:
        field = db.getField(field_id)

        field_info = {}
        field_info["name"] = field.name

        type_info = db.getTypeById(field.type_id);
        field_info["info"] = type_info

        info["fields"].append(field_info)

    return info
