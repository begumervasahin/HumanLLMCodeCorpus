import time
import os
def fonk1():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
def fonk2():
    while True:
        try:
            b2 = int(input("Introduzca el número de elementos: "))
            return b2
        except ValueError:
            print('Solo introduzca números.')
            print('Inténtelo nuevamente.')
            time.sleep(1)
            fonk1()
def fonk3(b2):
    b3 = []
    while len(b3) < b2:
        try:
            b4 = int(input(f'Elemento {len(b3) + 1}: '))
            b3.append(b4)
        except ValueError:
            print('Solo introduzca números.')
            print('Inténtelo nuevamente.')
            time.sleep(1)
            fonk1()
    return b3
def fonk4(b3):
    b5 = sum(b3)
    b6 = b5 / len(b3)
    print('Promedio: ', b6)
def fonk5():
    b2 = fonk2()
    b3 = fonk3(b2)
    fonk4(b3)
if b7 = = "__main__":
    fonk5()