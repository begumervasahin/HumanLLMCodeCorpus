import time
import os
def fonk1():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
def fonk2(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Solo introduzca números.')
            print('Inténtelo nuevamente.')
            time.sleep(1)
            fonk1()
def fonk3():
    return fonk2("Introduzca el número de elementos: ")
def fonk4(b6):
    b2 = []
    for i in range(1, b6 + 1):
        b3 = fonk2(f'Elemento {i}: ')
        b2.append(b3)
    return b2
def fonk5(b2):
    b4 = sum(b2)
    b5 = b4 / len(b2)
    print('Promedio: ', b5)
def fonk6():
    fonk1()
    b6 = fonk3()
    b2 = fonk4(b6)
    fonk5(b2)
if b7 = = "__main__":
    fonk6()