import itertools
def fonk1(length):
    b1 = list(itertools.product([0, 1], repeat=length))
    b2 = []
    for combination in b1:
        b3 = ''.join(str(bit) for bit in combination)
        b2.append(b3)
    return b2
def fonk2(message, b6):
    b4 = '0' * (len(b6) - 1)
    b5 = message + b4
    b5 = list(b5)
    b6 = list(b6)
    for i in range(len(b5) - len(b4)):
        if b5[i] == '1':
            for j in range(len(b6)):
                b5[i + j] = str((int(b5[i + j]) ^ int(b6[j])))
    return ''.join(b5[-len(b4):])
def fonk3(message, b6, b7 = None):
    b8 = fonk2(message, b6)
    b9 = fonk1(len(b6))
    b10 = []
    if b7 is None:
        b7 = fonk1(len(message) - len(b6))
    for prefix in b7:
        for calc_bit in b9:
            b11 = prefix + calc_bit
            if fonk2(b11, b6) == b8:
                b10.append(b11)
    return b10
print(fonk3("11010110", "10011", ["111"]))