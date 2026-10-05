import time
import os
def fonk1(prompt):
    while True:
        try:
            b1 = int(input(prompt))
            return b1
        except ValueError:
            print('Solo introduzca números.')
            print('Inténtelo nuevamente.')
            time.sleep(1)
            os.system('cls' if os.b2 = = 'nt' else 'clear')
def fonk2():
    while True:
        b3 = fonk1("Introduzca el número de b5: ")
        b4 = [None] * b3
        break
    for i in range(b3):
        while True:
            try:
                b5 = fonk1('Elemento {}: '.format(i+1))
                b4[i] = b5
                break
            except ValueError:
                print('Solo introduzca números.')
                print('Inténtelo nuevamente.')
                time.sleep(1)
                os.system('cls' if os.b2 = = 'nt' else 'clear')
    b6 = sum(b4)
    print('Promedio: ', b6 / b3)
if b7 = = "__main__":
    fonk2()