from flask import Blueprint, request
from app.tools.response_manager import ResponseManager
from app.schemas.pokemon_favorites_schema import PokemonFavoriteSchema
from bson import ObjectId
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint("favorite_pokemon", __name__, url_prefix="/favorite-pokemons")
RM = ResponseManager()
FP_MODEL = ModelFactory.get_model("pokemon_favorites")
FP_SCHEMA = PokemonFavoriteSchema()

#Crear
@bp.route("/", methods=["POST"])
@jwt_required()
def create():
    user_id = get_jwt_identity()
    try:
        data = request.json
        data = FP_SCHEMA.load(data)
        data["user_id"] = user_id 
        fp = FP_MODEL.create(data)
        return RM.success({"_id":fp})
    except ValidationError as err:
        print(err)
        return RM.error("Es necesario enviar todos los parametros")
#Eliminar
@bp.route("/<string:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    FP_MODEL.delete(ObjectId(id))
    return RM.success("Pokemon eliminado con exito")
#Get ALL
@bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    user_id = get_jwt_identity()
    data = FP_MODEL.find_all(user_id)
    return RM.success(data)
