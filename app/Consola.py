from http.client import responses

import requests
from urllib3 import request

username = input("User: ")
password = input("Password: ")
resultado = requests.post(
   "http://localhost:5050/users/login",
   json={"username": username, "password": password},
   headers={"Content-Type": "application/json"})
token = resultado.json().get("token")

print ("Token: " + token)

try:
   response = requests.get("http://localhost:5050/autores",headers={"Authorization": "Bearer " + token})
except Exception as e:
   print(e)
# Si la petición es exitosa
if response.status_code == 200:
   # Muestra el json correspondiente a la petición
   print(response.json())
# Si no, muestra este mensaje
else:
   print("Se ha producido un error")
