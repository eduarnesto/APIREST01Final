import requests

url_user = "http://localhost:5351/users"

usuario = { "username": "Manolo", "password": "hola"}

respuestaUsuario = requests.get(url_user, json=usuario)
codigoUsuario = respuestaUsuario.status_code

if codigoUsuario == 200:
    jsonUsuario = respuestaUsuario.json() # {'token': valor_token}

    valor_token = jsonUsuario["token"]
    cabecera = {'Authorization': f'Bearer {valor_token}'}

    url_pelicula = "http://localhost:5351/peliculas/10"
    
    pelicula = {"titulo": "Peli2", "anyoLanzamiento": 2025}

    respuestaPelicula = requests.put(url_pelicula, json=pelicula, headers=cabecera)

    codigoPelicula = respuestaPelicula.status_code

    if codigoPelicula == 200:
        print("Se ha modificado la película")
    elif codigoPelicula == 201:
        print("Se ha añadido una nueva película")
    else:
        print("Ha habido algún error en la petición")

else:
    print("Error en la autenticación del usuario")