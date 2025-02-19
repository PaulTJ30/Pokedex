from app import mongo
from app.models.super_clase import SuperClass
from bson import ObjectId

class PokemonFavorites(SuperClass):
    def _init_(self):
        super()._init_("pokemon_favorites")
        
    def update(self, object_id,data):
        raise NotImplementedError("Los pokemones no se pueden actualizar")
    
    def find_by_id(self, object_id):
        return NotImplementedError("Los pokemones no se pueden encontrar de manera individual")
    
    def find_all(self, user_id):
        #Buscando los pokemones utilizando el id para saber cuales pokemones tiene
        data =  self.collection.find({"user_id": ObjectId(user_id)})
        return data