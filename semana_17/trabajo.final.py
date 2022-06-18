import requests, json

TOKEN= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMiLCJub21icmUiOiJhbHVtbm8ifQ.eC452_kHQbCP4wDVvN6nl5Vx8V6HhQP8D5EljApFXS8"
URL_API_GET = "http://pad19.com:3030/productos/10" # luego estos acordate de ponerlos en un archivo aparte
URL_API_POST = "http://pad19.com:3030/pedidos/10" # luego estos acordate de ponerlos en un archivo aparte



def solicitar_stock(ruta):
    proceso= requests.get(ruta)

    if (proceso.status_code == 200):
        return proceso.json()
    else:
        return False

def mostrar_stock(datos):
    print(datos["id"])
    
def principal():
    datos_json= solicitar_stock(URL_API_GET)
    
    if (datos_json == False):
        print("Error al solicitar datos")
    else:
        mostrar_stock(datos_json)







