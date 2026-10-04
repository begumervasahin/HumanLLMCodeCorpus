import math
import time
def fonk1(b1):
    if (b1 % 2) == 0:
        b1 = b1 -1
    else:
        b1 = b1 -2
    return b1
def fonk2(b2, b):
    if b2 = = 0:
        return (b, 0, 1)
    else:
        g, b4, b3 = fonk2(b % b2, b2)
        return (g, b3 - (b
def fonk3(b2, m):
    g, b3, b4 = fonk2(b2, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return b3 % m
def fonk4(n,e):
    b5 = time.time()
    b6 = math.floor((math.sqrt(n)))
    b6 = fonk1(b6)
    for b7 in range(b6, 1 , -2):
        if(n%b7 = = 0):
            b8 = b7
            break
    b9 = n /b8
    b9 = math.floor(b9)
    if (n -b8*b9) != 0:
        raise Exception('nÃ£o deu certo')
    b10 = (b8-1) * (b9-1)
    b11 = fonk3(e,b10)
    if (b11*e %b10 != 1):
         raise Exception('nÃ£o deu certo')
    b12 = time.time() - b5
    return (b11,b12)
b13 = [(1325147,79), (13339787,351047),(87411743,11),(153988391,365), (642281891,80105) ,(3662937263, 80273),(2461987247,78703) ,(10988963221,118297),(9979645019,9764819), (36207914857,89  )]
a1 = 0
for val in b13:
    chave, b14 = fonk4(*val)
    n1,b15 = val
    print('esse Ã© o par',n1,b15)
    print('b2 chave Ã©', chave)
    print('esse demorou', b14)
    a1 += b14
print('o b14 total foi de',a1)