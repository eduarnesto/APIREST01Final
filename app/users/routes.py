import bcrypt
from flask import Blueprint, request
from bcrypt import *
from flask_jwt_extended import create_access_token

from app.utils.functions import *

rutaUsuarios = "ficheros/users.json"

usersBP = Blueprint('users', __name__)

@usersBP.post('/')
def registerUser():
    listaUsuarios = leeFichero(rutaUsuarios)
    if request.is_json:
        nuevoUsuario = request.get_json()
        contrasenya = nuevoUsuario["password"].encode("UTF-8")
        sal = gensalt()
        hash = hashpw(contrasenya, sal).hex()
        nuevoUsuario["password"] = hash
        listaUsuarios.append(nuevoUsuario)
        escribeFichero(listaUsuarios, rutaUsuarios)
        return nuevoUsuario, 201
    else:
        return {"error": "JSON no correcto"}, 415

@usersBP.get('/')
def loginUser():
    usuarios = leeFichero(rutaUsuarios)
    if request.is_json:
        usuarioJson = request.get_json()
        nombreUsuario = usuarioJson["username"]
        for usuario in usuarios:
            if usuario["username"] == nombreUsuario:
                contrasenyaJson = usuarioJson["password"].encode("UTF-8")
                if checkpw(contrasenyaJson, bytes.fromhex(usuario["password"])):
                    #autenticación correcta
                    token = create_access_token(identity = nombreUsuario)
                    return {"token": token}, 200
                else:
                    return {"error": "No autorizado"}, 401
        return {"error": "usuario no encontrado"}, 404
    return {"error": "JSON no es correcto"}, 415

@usersBP.post("/login")
def getUser():
   if request.is_json:
       user = request.get_json()
       username = user["username"]
       password = user["password"]
       usuarios = leeFichero(rutaUsuarios)
       for usuario in usuarios:
           if usuario["username"] == username and bcrypt.checkpw(password.encode("utf-8"),bytes.fromhex(usuario["password"])):
               return {"token": create_access_token(identity=username)}, 200
       return {"token":"Contrasenya o usuario no valido"}, 401
   return {"error": "Request must be JSON"}, 415