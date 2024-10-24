import requests

url="http://localhost:5351/users"
usuario = { "username": "Manolo",
        "password": "hola"}

response = requests.post(url, json=usuario)
codigo = response.status_code

if codigo == 201:
    print("El registro se ha hecho correctamente")
    print(response.json())
else:
    print("El registro no se ha realizado correctamente")
