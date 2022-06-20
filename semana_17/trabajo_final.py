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
    print("Producto id: ", datos["productos"][0]["id"])
    print("Descripción: ", datos["productos"][0]["nombre"])
    print("Precio unitario: ", datos["productos"][0]["precio"])
    print("Cantidad disponible: ", datos["productos"][0]["stock"])
    print("\n")
    print("Producto id: ", datos["productos"][1]["id"])
    print("Descripción: ", datos["productos"][1]["nombre"])
    print("Precio unitario: ", datos["productos"][1]["precio"])
    print("Cantidad disponible: ", datos["productos"][1]["stock"])
    print("\n")
    print("Producto id: ", datos["productos"][2]["id"])
    print("Descripción: ", datos["productos"][2]["nombre"])
    print("Precio unitario: ", datos["productos"][2]["precio"])
    print("Cantidad disponible: ", datos["productos"][2]["stock"])
    print("\n")
    print("Producto id: ", datos["productos"][2]["id"])
    print("Descripción: ", datos["productos"][2]["nombre"])
    print("Precio unitario: ", datos["productos"][2]["precio"])
    print("Cantidad disponible: ", datos["productos"][2]["stock"])
    print("\n")
    print("Producto id: ", datos["productos"][3]["id"])
    print("Descripción: ", datos["productos"][3]["nombre"])
    print("Precio unitario: ", datos["productos"][3]["precio"])
    print("Cantidad disponible: ", datos["productos"][3]["stock"])
    print("\n")
    print("Producto id: ", datos["productos"][4]["id"])
    print("Descripción: ", datos["productos"][4]["nombre"])
    print("Precio unitario: ", datos["productos"][4]["precio"])
    print("Cantidad disponible: ", datos["productos"][4]["stock"])
    print("\n")
    print("Producto id: ", datos["productos"][5]["id"])
    print("Descripción: ", datos["productos"][5]["nombre"])
    print("Precio unitario: ", datos["productos"][5]["precio"])
    print("Cantidad disponible: ", datos["productos"][5]["stock"])
    print("\n")
    print("Producto id: ", datos["productos"][6]["id"])
    print("Descripción: ", datos["productos"][6]["nombre"])
    print("Precio unitario: ", datos["productos"][6]["precio"])
    print("Cantidad disponible: ", datos["productos"][6]["stock"])
    print("\n")
    print("Producto id: ", datos["productos"][8]["id"])
    print("Descripción: ", datos["productos"][8]["nombre"])
    print("Precio unitario: ", datos["productos"][8]["precio"])
    print("Cantidad disponible: ", datos["productos"][8]["stock"])
    print("\n")
    print("Producto id: ", datos["productos"][9]["id"])
    print("Descripción: ", datos["productos"][9]["nombre"])
    print("Precio unitario: ", datos["productos"][9]["precio"])
    print("Cantidad disponible: ", datos["productos"][9]["stock"])
    print("\n")
    print("Producto id: ", datos["productos"][10]["id"])
    print("Descripción: ", datos["productos"][10]["nombre"])
    print("Precio unitario: ", datos["productos"][10]["precio"])
    print("Cantidad disponible: ", datos["productos"][10]["stock"])
    print("\n")
    print("Producto id: ", datos["productos"][11]["id"])
    print("Descripción: ", datos["productos"][11]["nombre"])
    print("Precio unitario: ", datos["productos"][11]["precio"])
    print("Cantidad disponible: ", datos["productos"][11]["stock"])
    print("\n")

    #lista_1= [datos["productos"][0]["id"], datos["productos"][0]["nombre"], datos["productos"][0]["precio"], datos["productos"][0]["stock"]]
    #print(lista_1)

def principal():
    datos_json= solicitar_stock(URL_API_GET)
    
    if (datos_json == False):
        print("Error al solicitar datos")
    else:
        mostrar_stock(datos_json)


# HACER EL PEDIDO


def enviar_pedido(a, b):
    parametros = {"id":a, "cantidad":b}
    solicitud = requests.post(URL_API_POST, json=parametros)
    
    if (solicitud.status_code == 200):
        return solicitud.json()
    return False


def hacer_pedido():
    while True:
        print("Ingrese a continuación id del producto y cantidad, para finalizar el pedido presione '0' dos veces")
        a= int(input("id del producto: "))
        b= int(input("cantidad: "))
        
        if ( a !=0 or b !=0 ):
            proceso= enviar_pedido(a, b)
            if (proceso == False):
                print("Error al conectarse con el servidor")
            else:
                print(proceso["mensaje"])
        else:
            print("Pedido finalizado")
            break
            

if (__name__ == "__main__"):
    principal()
    hacer_pedido()

# pendientes: 1- acumular, 2- ver lo de los parámetros en otro archivo



        
        

    
