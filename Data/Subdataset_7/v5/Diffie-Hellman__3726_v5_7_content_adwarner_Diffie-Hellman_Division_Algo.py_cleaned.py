import numpy as np
def fonk1(n, d):
    b1 = []
    while n >= 1:
        b1.append(str(n % d))
        n
    return ''.join(b1)
def fonk2(b6, b2):
    while b2 != 0:
        b6, b2 = b2, b6 % b2
    return b6
def fonk3(n):
    b3 = []
    b4 = list(range(2, n + 1))
    while len(b4) > 0:
        b5 = b4[0]
        b3.append(b5)
        b4 = [num for num in b4 if num % b5 != 0]
    return b3
def fonk4(b6, b2):
    if b6 = = 0:
        return (b2, 0, 1)
    else:
        g, x, b7 = fonk4(b2 % b6, b6)
        return (g, b7 - (b2
def fonk5(b6, m):
    g, x, b7 = fonk4(b6, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m