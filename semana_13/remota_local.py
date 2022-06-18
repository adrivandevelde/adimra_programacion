import json
import requests

APPID = "b07cceb706b36724ddaa2614cdb76af4"
ID_CIUDAD = "rafaela"
IDIOMA = "en"
RUTA = f"https://api.openweathermap.org/data/2.5/weather?q={ID_CIUDAD}&units=metric&appid={APPID}&lang={IDIOMA}"

def recuperar_remoto(ruta, formato):
    respuesta= requests.get(ruta)

    if formato== "json":
        return respuesta.json

    return False

if (__name__ == "__main__"):
    datos_clima= recuperar_remoto(RUTA, "json")
    print(type(datos_clima))





