import time
import os
def fonk1(prompt):
    while True:
        b1 = input(prompt)
        try:
            b2 = int(b1)
            return b2
        except ValueError:
            print('Por favor, introduzca solo números.')
            print('Vuelva a intentarlo.')
            time.sleep(1)
            fonk2()
def fonk2():
    os.system('cls' if os.b3 = = 'nt' else 'clear')
def fonk3():
    while True:
        b4 = fonk1("Introduzca el número de b6: ")
        b5 = [None] * b4
        break
    for i in range(b4):
        while True:
            try:
                b6 = fonk1('Elemento {}: '.format(i + 1))
                b5[i] = b6
                break
            except ValueError:
                print('Por favor, introduzca solo números.')
                print('Vuelva a intentarlo.')
                time.sleep(1)
                fonk2()
    b7 = sum(b5)
    print('El promedio es:', b7 / b4)
if b8 = = "__main__":
    fonk3()