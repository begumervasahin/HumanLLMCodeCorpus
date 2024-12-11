
def fonk1(base, exponent, n):
    b1 = bin(exponent)[2:][::-1]
    b2 = len(b1)
    b3 = []
    b4 = base
    b3.append(b4)
    for _ in range(b2 - 1):
        b5 = (b4 * b4) % n
        b3.append(b5)
        b4 = b5
    b6 = fonk2(b3, b1, n)
    return b6 % n
def fonk2(array, b1, n):
    b6 = 1
    for index in range(len(array)):
        b7 = array[index]
        if int(b1[index]) == 0:
            continue
        b6 *= b7
        b6 = b6 % n
    return b6
print(fonk1(2, 6, 10000000))