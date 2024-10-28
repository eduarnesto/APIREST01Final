from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.utils.functions import *

autoresBP = Blueprint('autores', __name__)
rutaAutores = "ficheros/autores.json"
rutaLibros = "ficheros/libros.json"

@autoresBP.get('/<int:id>')
def getAutores(id):
    autores = leeFichero(rutaAutores)
    for autor in autores:
        if autor["id"] == id:
            return autor, 200
    return {"error" : "Autor no encontrado"}, 404

@autoresBP.get('autores/<int:id>')
def getLibros(id):
    libros = leeFichero(rutaLibros)
    lista = []
    for libro in libros:
        if libro["idAutor"] == id:
            lista.append(libro)
    if len(lista) > 0:
        return lista, 200
    return {"error": "No hay libros para el autor indicado"}, 404

@autoresBP.put('/<int:id>')
@jwt_required()
def modificaAutor(id):
    autores = leeFichero(rutaAutores)
    if request.is_json:
        nuevo_autor = request.get_json()
        for autor in autores:
            if autor["id"] == id:
                autor.update(nuevo_autor)
                escribeFichero(autores, rutaAutores)
                return autor, 200
        nuevo_autor["id"] = id
        autores.append(nuevo_autor)
        escribeFichero(autores, rutaAutores)
        return nuevo_autor, 201
    else:
        return {"error": "JSON erróneo"}, 415