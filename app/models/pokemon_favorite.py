from app import mongo
from app.models.super_clase import SuperClass

class PokemonFavorites(SuperClass):
    def _init_(self):
        super()._init_("pokemon_favorites")
        