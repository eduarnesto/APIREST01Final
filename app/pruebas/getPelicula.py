import requests

url="http://localhost:5351/peliculas/1"

respuesta = requests.get(url)
codigo = respuesta.status_code

if codigo == 200:
    print("Petición correcta")
    json = respuesta.json()
    print("id:", json["id"])
    print("Títtulo:", json["titulo"])
    print("Año lanzamiento:", json["anyoLanzamiento"])
else:
    print("El recurso no existe")