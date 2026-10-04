import math
import time
def nearestOddUnder(number):
    if (number % 2) == 0:
        number = number -1
    else:
        number = number -2
    return number
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
def bruteRSA(n,e):
    start_time = time.time()
    c = math.floor((math.sqrt(n)))
    c = nearestOddUnder(c)
    for i in range(c, 1 , -2):
        if(n%i == 0):
            p = i
            break
    q = n /p
    q = math.floor(q)
    if (n -p*q) != 0:
        raise Exception('nÃ£o deu certo')
    phin = (p-1) * (q-1)
    d = modinv(e,phin)
    if (d*e %phin != 1):
         raise Exception('nÃ£o deu certo')
    total_time = time.time() - start_time
    return (d,total_time)
arr = [(1325147,79), (13339787,351047),(87411743,11),(153988391,365), (642281891,80105) ,(3662937263, 80273),(2461987247,78703) ,(10988963221,118297),(9979645019,9764819), (36207914857,89  )]
tempototal = 0
for val in arr:
    chave, tempo = bruteRSA(*val)
    n1,e1 = val
    print('esse Ã© o par',n1,e1)
    print('a chave Ã©', chave)
    print('esse demorou', tempo)
    tempototal += tempo
print('o tempo total foi de',tempototal)