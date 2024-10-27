from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils.functions import *

librosBP = Blueprint('libros', __name__)
rutaLibros = "ficheros/libros.json"
rutaAutor = "ficheros/autores.json"

@librosBP.get('/')
def getLibros():
    libros = leeFichero(rutaLibros)
    return jsonify(libros), 200

@librosBP.post('/')
def addLibros():
    libros = leeFichero(rutaLibros)
    autores = leeFichero(rutaAutor)
    if request.is_json:
        nuevoLibro = request.get_json()
        for autor in autores:
            if autor["id"] == nuevoLibro["idAutor"]:
                nuevoLibro["id"] = nuevo_id(libros)
                libros.append(nuevoLibro)
                escribeFichero(libros, rutaLibros)
                return nuevoLibro, 201
        return {"error": "Autor no encontrado"}, 404
    else:
        return {"error": "JSON no es correcto"}, 415


@librosBP.delete('/<int:id>')
@jwt_required()
def borraLibro(id):
    listaLibros = leeFichero(rutaLibros)
    for autor in listaLibros:
        if autor["id"] == id:
            listaLibros.remove(autor)
            escribeFichero(listaLibros, rutaLibros)
            return {}, 200
    return {"error": "Libro no encontrado"}, 404

