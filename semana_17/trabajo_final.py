import requests

TOKEN= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMiLCJub21icmUiOiJhbHVtbm8ifQ.eC452_kHQbCP4wDVvN6nl5Vx8V6HhQP8D5EljApFXS8"
URL_API_GET = f"http://pad19.com:3030/productos/10?token={TOKEN}" # luego estos acordate de ponerlos en un archivo aparte
URL_API_POST = f"http://pad19.com:3030/pedidos/10?token={TOKEN}" # luego estos acordate de ponerlos en un archivo aparte

# SOLICITAR LOS DATOS DE STOCK Y MOSTRARLOS

def solicitar_stock(ruta):
    proceso= requests.get(ruta)

    if (proceso.status_code == 200):
        return proceso.json()

    else:
        return False


def mostrar_stock(datos):
    for item in datos:
        print(f"ID {item['id']}. {item['nombre']} -> Stock disponible:{item['stock']}")
        print()

def principal():
    datos_json= solicitar_stock(URL_API_GET)
    
    if (datos_json == False):
        print("Error al solicitar datos")
    else:
        mostrar_stock(datos_json["productos"])



# HACER EL PEDIDO

def enviar_pedido(a, b):
    parametros = {"id":a, "cantidad":b}
    solicitud = requests.post(URL_API_POST, json=parametros)
    
    if (solicitud.status_code == 200):
        return solicitud.json()
    return False


def hacer_pedido():
    pedido= []
        
    while True:
        print("Ingrese a continuación id del producto y cantidad, para finalizar el pedido presione '0'")
        a= int(input("id del producto: "))
        b= int(input("cantidad: "))

        if ( a !=0 ):
            pedido.append({ "id": a, "cantidad": b })
        else:
            break

    proceso= enviar_pedido(pedido[a], pedido[b])
    if (proceso == True):
            print("Error al conectarse con el servidor")
    else:
            print("Pedido finalizado")

            

if (__name__ == "__main__"):
    principal()
    hacer_pedido()




        
        

    
