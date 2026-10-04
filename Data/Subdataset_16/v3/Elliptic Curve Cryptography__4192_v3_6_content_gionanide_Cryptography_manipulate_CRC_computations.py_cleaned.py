import itertools
def fonk1(length):
    b1 = [''.join(map(str, bits)) for bits in itertools.product('01', repeat=length)]
    return b1
def fonk2(b13, b4):
    b2 = '0' * (len(b4) - 1)
    b3 = list(b13 + b2)
    b4 = list(b4)
    for i in range(len(b3) - len(b2)):
        if b3[i] == '1':
            for j in range(len(b4)):
                b3[i + j] = str(int(b3[i + j]) ^ int(b4[j]))
    return ''.join(b3[-(len(b4) - 1):])
def fonk3(b13, b4, b5 = None):
    b6 = fonk2(b13, b4)
    b7 = len(b4)
    b8 = fonk1(b7)
    b9 = []
    if b5 is None:
        b10 = len(b13) - b7
        b5 = fonk1(b10)
    for prefix in b5:
        for combination in b8:
            b11 = prefix + combination
            if fonk2(b11, b4) == b6:
                b9.append(b11)
    return b9
if b12 = = "__main__":
    b13 = "11010110"
    b4 = "10011"
    b5 = ["111"]
    b9 = fonk3(b13, b4, b5)
    print("Collisions:")
    for collision in b9:
        print(collision)