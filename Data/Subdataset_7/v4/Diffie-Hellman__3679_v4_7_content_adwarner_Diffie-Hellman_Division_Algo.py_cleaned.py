import numpy as np
def fonk1(b2, d):
    b1 = []
    while b2 >= 1:
        b1.append(str(b2 % d))
        b2 = int(b2 / d)
    return ''.join(b1)
def fonk2(b4, b5):
    b3 = b4 % b5
    while b4 % b5 >= 1:
        b2 = b5 * int(b4 / b5) + b4 % b5
        b4 = b5
        b5 = b3
    return b3
def fonk3(b2):
    b6 = []
    b7 = []
    b8 = b2
    b9 = range(b8 + 1)[2:len(range(b8 + 1))]
    b9 = b9[1::2]
    for i in range(len(b9)):
        for j in range(len(b9)):
            prime.append(b9[i] % b9[j])
    b10 = [prime[b11:b11 + len(b9)] for b11 in range(0, len(prime), len(b9))]
    for i in range(len(b10)):
        if b10[i].count(0) == 1:
            b6.append(b9[i])
    b6.insert(0, 2)
    return b6
def fonk4(b4, b5):
    if b4 = = 0:
        return (b5, 0, 1)
    else:
        g, b12, b11 = fonk4(b5 % b4, b4)
        return (g, b11 - (b5
def fonk5(b4, m):
    g, b11, b12 = fonk4(b4, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return b11 % m