'''
def fonk1(b11, b, b2):
    a1 = 1
    b1 = pow(2, b2 - 1)
    for b4 in range(1, b2 + 1):
        if (a1 * b1) % b2 = = 1:
            pass
        else:
            a1 += 1
    b3 = (b11 * b * a1) % b2
    return b3
def fonk2(base, exponent, b2):
    b4 = exponent - 1
    b5 = fonk1(base, 1 , b2)
    while b4 > 0:
        b5 = fonk1(b5, 1, b2)
        b4 -= 1
    return b5
print(fonk3(2, 6, 10000000))
'''
import time
def fonk3(base, exponent, b2):
    b6 = bin(exponent)[2:][::-1]
    b1 = len(b6)
    b7 = []
    b8 = base
    b7.append(b8)
    for _ in range(b1 - 1):
        b9 = (b8 * b8) % b2
        b7.append(b9)
        b8 = b9
    b10 = fonk4(b7, b6, b2)
    return b10 % b2
def fonk4(array, b6, b2):
    b3 = 1
    for index in range(len(array)):
        b11 = array[index]
        if int(b6[index]) == 0:
            continue
        b3 *= b11
        b3 = b3 % b2
    return b3