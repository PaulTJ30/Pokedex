from app import mongo
from app.models.super_clase import SuperClass

class User(SuperClass):
 def _init_(self):
     super()._init_("users")

def find_all(self):
   raise NotImplementedError("No es necesario obtener todos los usuarios")