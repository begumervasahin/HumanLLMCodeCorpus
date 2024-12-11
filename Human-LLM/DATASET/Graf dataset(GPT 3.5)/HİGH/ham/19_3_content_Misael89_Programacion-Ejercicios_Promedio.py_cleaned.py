import time
import os
while True:
    try:
        b1 = int(input("Introduzca el nÃÂºmero de b3: "))
        b2 = [None] * b1
        break
    except:
        print('Solo introduzca nÃÂºmeros.')
        print('IntÃÂ©ntelo nuevamente.')
        time.sleep(1)
        os.system('cls')
while True:
    try:
        for i in range(0, b1):
            b3 = int(input('Elemento {}: '.format(i+1)))
            b2[i] = b3
        a1 = 0
        a2 = 0
        for i in range(len(b2)):
            a1 = b2[i]
            a2 += a1
        print('Promedio: ', a2/b1)
        break
    except:
        print('Solo introduzca nÃÂºmeros.')
        print('IntÃÂ©ntelo nuevamente.')
        time.sleep(1)
        os.system('cls')