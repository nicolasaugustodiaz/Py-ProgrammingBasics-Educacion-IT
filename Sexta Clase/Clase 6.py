import requests                               #importo libreria requests
r=requests.post("https://localhost:7001/student",json={"name":"Lautaro","courses":3})
print("codigo de estado: ",r.status_code)
respuesta=r.json()
print("respuesta: ",respuesta)