from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.utils.functions import *

librosBP = Blueprint('libros', __name__)
rutaLibros = "ficheros/libros.json"
rutaAutor = "ficheros/autores.json"

@librosBP.get('/<int:id_libro>')
def getLibros(id_libro):
    libros = leeFichero(rutaLibros)
    for libro in libros:
        if libro["id"] == id_libro:
            return libro, 200
    return {"error" : "Libro no encontrado"}, 404

@librosBP.get('autores/<int:id_libro>')
def getLibros(id_libro):
    autores = leeFichero(rutaAutor)
    lista = []
    for autor in autores:
        if autor["id_libro"] == id_libro:
            lista.append(autor)
    if len(lista) > 0:
        return lista, 200
    return {"error": "No hay autores para el libro indicado"}, 404

@librosBP.put('/<int:id_libro>')
@jwt_required()
def modificaLibro(id_libro):
    libros = leeFichero(rutaLibros)
    if request.is_json:
        nuevo_libro = request.get_json()
        for libro in libros:
            if libro["id"] == id_libro:
                libro.update(nuevo_libro)
                escribeFichero(libros, rutaLibros)
                return libro, 200
        nuevo_libro["id"] = id_libro
        libros.append(nuevo_libro)
        escribeFichero(libros, rutaLibros)
        return nuevo_libro, 201
    else:
        return {"error": "JSON erróneo"}, 415
