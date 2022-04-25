if (__name__ == "__main__"):
    
    dias= ('viernes', 'sábado', 'domingo')
    cant= [int(input('Ingrese cantidad de entregas realizadas el día viernes: ')), int(input('Ingrese cantidad de entregas realizadas el día sábado: ')), int(input('Ingrese cantidad de entregas realizadas el día viernes: '))]

    valor_1= 300
    valor_2= 200

    monto_vier= valor_1* cant[0]
    monto_sab= valor_1* cant[1]
    monto_dom= valor_2* cant[2]

    print(f'Se realizaron {cant[0]} entregas el día {dias[0]}, {cant[1]} entregas el día {dias[1]} y {cant[2]} el día {dias[2]}.')
    print(f'Debe cobrar $ {monto_vier} por las entregas del día {dias[0]}, \n'
    f'$ {monto_sab} por las del {dias[1]} y $ {monto_dom} por las del {dias[2]}.')

    total_entregas= cant[0]+ cant[1]+ cant[2]
    print(f'Las entregas totales del fin de semana fueron {total_entregas}.')


    monto_vier= valor_1* cant[0]
    monto_sab= valor_1* cant[1]
    monto_dom= valor_2* cant[2]
        
    total_entregas= cant[0]+ cant[1]+ cant[2]
    total_1= monto_vier + monto_sab + monto_dom + 1000
    total_2= monto_vier + monto_sab + monto_dom

    """ def mensaje_1():
        print(f'Debe cobrar $ {total_1}')

    def mensaje_2():
        print(f'Debe cobrar $ {total_2}')


    if total_entregas > 20:
            print(mensaje_1())
    else:
            print(mensaje_2()) """

    def monto_entregas():
        if int(total_entregas) > 20:
            print(f'Debe cobrar $ {total_1}')
        else:
            print(f'Debe cobrar $ {total_2}')

    print(monto_entregas())
    



    





