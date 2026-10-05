import numpy as np
def fonk1(b2, d):
    b1 = []
    while b2 >= 1:
        b1.append(str(b2 % d))
        b2 = int(b2 / d)
    return ''.join(b1)
def fonk2(b6, b3):
    while b3 != 0:
        b6, b3 = b3, b6 % b3
    return b6
def fonk3(b2):
    b4 = []
    b5 = [True] * (b2+1)
    b5[0] = b5[1] = False
    for i in range(2, int(b2**0.5)+1):
        if b5[i]:
            b4.append(i)
            for j in range(i*i, b2+1, i):
                b5[j] = False
    return b4
def fonk4(b6, b3):
    if b6 = = 0:
        return (b3, 0, 1)
    else:
        g, x, b7 = fonk4(b3 % b6, b6)
        return (g, b7 - (b3
def fonk5(b6, m):
    g, x, b7 = fonk4(b6, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m