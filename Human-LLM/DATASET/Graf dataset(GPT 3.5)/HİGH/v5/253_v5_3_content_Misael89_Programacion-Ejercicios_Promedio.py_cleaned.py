import time
import os
def fonk1(prompt):
    while True:
        try:
            b1 = int(input(prompt))
            return b1
        except ValueError:
            print('Por favor, introduzca solo números.')
            print('Inténtelo nuevamente.')
            time.sleep(1)
            fonk2()
def fonk2():
    os.system('cls' if os.b2 = = 'nt' else 'clear')
def fonk3():
    while True:
        try:
            b3 = fonk1("Introduzca el número de elementos: ")
            break
        except KeyboardInterrupt:
            print('Operación cancelada.')
            return
    b4 = [None] * b3
    for i in range(b3):
        while True:
            try:
                b5 = fonk1('Ingrese el valor del elemento {}: '.format(i + 1))
                b4[i] = b5
                break
            except KeyboardInterrupt:
                print('Operación cancelada.')
                return
            except ValueError:
                print('Por favor, introduzca solo números.')
                print('Inténtelo nuevamente.')
                time.sleep(1)
                fonk2()
    b6 = sum(b4)
    b7 = b6 / b3
    print('El promedio de los elementos es:', b7)
if b8 = = "__main__":
    fonk3()