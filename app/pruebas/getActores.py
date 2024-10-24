import requests

url = "http://localhost:5351/actores/"

respuesta = requests.get(url)
codigo = respuesta.status_code

if codigo == 200:
    print(respuesta.json())
else:
    print("Error en la petición")