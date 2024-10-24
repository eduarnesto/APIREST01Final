import requests

url_user = "http://localhost:5351/users"

usuario = { "username": "Manolo", "password": "hola"}

respuestaUsuario = requests.get(url_user, json=usuario)
codigoUsuario = respuestaUsuario.status_code

if codigoUsuario == 200:
    jsonUsuario = respuestaUsuario.json() # {'token': valor_token}

    valor_token = jsonUsuario["token"]
    cabecera = {'Authorization': f'Bearer {valor_token}'}

    urlActor = "http://localhost:5351/actores/2"

    respuestaActor = requests.delete(urlActor, headers=cabecera)

    if respuestaActor == 200:
        print("Actor eliminado correctamente")
    else:
        print("No se ha podido eliminar el actor")
elif codigoUsuario == 404:
    print("No se encontró el usuario")
else:
    print("Error en el login")