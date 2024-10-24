from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.utils.functions import *

autoresBP = Blueprint('autores', __name__)
rutaAutores = "ficheros/autores.json"
rutaLibros = "ficheros/libros.json"

@autoresBP.get('/')
def getAutores():
    autores = leeFichero(rutaAutores)
    return jsonify(autores), 200

@autoresBP.post('/')
def addAutores():
    autores = leeFichero(rutaAutores)
    libros = leeFichero(rutaLibros)
    if request.is_json:
        nuevoAutor = request.get_json()
        for libro in libros:
            if libro["id"] == nuevoAutor["id_autor"]:
                nuevoAutor["id"] = nuevo_id(autores)
                autores.append(nuevoAutor)
                escribeFichero(autores, rutaAutores)
                return nuevoAutor, 201
        return {"error": "Libro no encontrado"}, 404
    else:
        return {"error": "JSON no es correcto"}, 415


@autoresBP.delete('/<int:id>')
@jwt_required()
def borraAutor(id):
    listaAutores = leeFichero(rutaAutores)
    for autor in listaAutores:
        if autor["id"] == id:
            listaAutores.remove(autor)
            escribeFichero(listaAutores, rutaAutores)
            return {}, 200
    return {"error": "Autor no encontrado"}, 404