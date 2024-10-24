import requests

url = "http://localhost:5351/actores/"

actor = {"nombre": "Julia Roberts",
        "nacionalidad": "Estados Unidos",
        "id_pelicula": 2}

respuesta = requests.post(url, json=actor)
codigo = respuesta.status_code

if codigo == 201:
    print("Actor añadido")
elif codigo == 404:
    print("La película no existe")
elif codigo == 415:
    print("El JSON no es correcto")
else:
    print("Error al añadir el actor")