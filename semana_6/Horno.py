from random import randint


while True:
    to = int(input("Ingrese temperatura objetivo: "))
    if to <= 0:
        break
    else:
        lecturas = [randint(300, 320) for x in range(50)]
        acumulado = 0
        promedio = 0
        
        for item in lecturas:
            acumulado= acumulado + item

        promedio= acumulado/len(lecturas)
        print(promedio)

        if promedio > to and promedio > 320:
            print("Apagar los dos quemadores")
        elif (promedio - to) <-100:
            print("Encender los dos quemadores")
        elif -100 <= (promedio - to) <= 0:
            print("Encender un quemador")
        elif 300 <= promedio <= 320:
            print("Horno a temperatura correcta")