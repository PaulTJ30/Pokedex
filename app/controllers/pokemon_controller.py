from flask import Blueprint, request
from app.tools.response_manager import ResponseManager
from bson import ObjectId
from marshmallow import ValidationError
from app.models.factory import ModelFactory

bp = Blueprint("pokemons", __name__, url_prefix="pokemons")
RM = ResponseManager()
P_Model = ModelFactory.get_model("pokemons")

#Traerte todos
@bp.route("/All", methods=["GET"])
def get_all():
    data = P_Model.find_all()
    return RM.success(data)
#Traerte uno

@bp.route("/", methods=["GET"])
def find_by_id():
    data = P_Model.find_by_id(ObjectId)
    return RM.success(data)