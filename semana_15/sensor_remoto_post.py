import requests

ID_SENSOR = 16
VALOR = 25.5
URL_API_POST = "http://pad19.com:3030/cargar_sensor"


def enviar_dato_sensor(sens, val):
    parametros = {
        "sensor": sens,
        "valor": val
    }

    solicitud = requests.post(URL_API_POST, json=parametros)

    if (solicitud.status_code == 200):
        return solicitud.json()
    return False


if (__name__ == "__main__"):
    proceso = enviar_dato_sensor(ID_SENSOR, VALOR)
    if (proceso == False):
        print("Error al conectar con el servidor de logs")
    else:
        print(proceso["mensaje"])