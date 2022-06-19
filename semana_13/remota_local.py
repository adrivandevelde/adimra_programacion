
import requests

APPID = "b07cceb706b36724ddaa2614cdb76af4"
ID_CIUDAD = "rafaela"
IDIOMA = "es"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={ID_CIUDAD}&units=metric&appid={APPID}&lang={IDIOMA}"

def solicitar_datos_clima(ruta):
    proceso = requests.get(ruta)

    if proceso.status_code == 200:
        return proceso.json

    return False

def mostrar_datos_clima(datos):
    print(datos["main"]["temp"])
    print(datos["weather"][0]["description"])

def principal():
    datos_json= solicitar_datos_clima(URL)
    if datos_json == False:
        print("Error al solicitar datos")
    else:
        mostrar_datos_clima(datos_json)


if (__name__ == "__main__"):
    principal()





