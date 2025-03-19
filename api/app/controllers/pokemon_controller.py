from flask import Blueprint, request
from app.tools.response_manager import ResponseManager
from bson import ObjectId
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from flask_jwt_extended import jwt_required


bp = Blueprint("pokemon", __name__, url_prefix="/pokemon")
RM = ResponseManager()
P_Model = ModelFactory.get_model("pokemons")

#Traerte uno
@bp.route("/get/<string:pokemon_id>", methods=["GET"])
@jwt_required()
def get_pokemon(pokemon_id):
    pokemon = P_Model.find_by_id(ObjectId(pokemon_id))
    return RM.success(pokemon)

#Traerte todos
@bp.route("/All", methods=["GET"])
@jwt_required()
def get_all():
    data = P_Model.find_all()
    return RM.success(data)