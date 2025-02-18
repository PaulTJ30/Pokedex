from marshmallow import Schema, fields, ValidationError

class UserSchema(Schema):
    pokemon_id = fields.Str(
        required=True,
        validate = lambda x: len(x) > 0,
        error_messages = {
            "required": "El id del pokemon es requerido"
        }
    )
    user_id = fields.Str(
      required=True,
      validate = lambda x: len(x) > 0,
      error_messages = {
          "required": "El id del usuario es requerido"
      }
    )
    password = fields.Str(
        required=True,
        validate = lambda x: len(x) > 0,
        error_messages = {
            "required": "La contraseña es requerida"
        }
    )
    email = fields.Str(
        required=True,
        validate = lambda x: "@utma.edu.mx" in x,
        error_messages = {
            "required": "El correo es requerido"
        }
    )