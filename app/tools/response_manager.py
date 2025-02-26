from flask import jsonify
#Vamos a sustituir a los "jsonify"

class ResponseManager:
    #El primero para mandar mensaje de que todo esta chido, 200
    def success(self, data):
        #Validamos si la data es un string lo convertimos a un objeto para mandar el mensaje
        if isinstance(data,str):
            data = {
                "message": data
            }
        return jsonify(data), 200
    #El segundo es un error del usuario, 400
    def error(self, data="invalid request"):
        if isinstance(data, str):
            data = {
                "message": data
            }
        return jsonify(data), 400
    #El tercero es un error en el servidor, 500 
    def error_server(self, data="SERVER ERROR"):
        if isinstance(data,str):
            data = {
                "message": data
            }
        return jsonify(data), 500