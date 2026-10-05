import itertools
def fonk1(num):
    b1 = list(itertools.product([0, 1], repeat=num))
    b2 = []
    for b3 in b1:
        b3 = str(b3)[1:-1]
        b3 = "".join(b3.split(", "))
        b2.append(b3)
    return b2
def fonk2(b5, b6):
    b4 = '0' * (len(b6) - 1)
    b5 = b5 + b4
    b5 = list(b5)
    b6 = list(b6)
    for i in range(len(b5) - len(b4)):
        if b5[i] == '1':
            for j in range(len(b6)):
                b5[i + j] = str((int(b5[i + j]) ^ int(b6[j])))
    return ''.join(b5[-len(b4):])
def fonk3(b5, b6, b7 = None):
    b8 = fonk2(b5, b6)
    b9 = fonk1(len(b6))
    b2 = []
    if b7 is None:
        b7 = fonk1(len(b5) - len(b6))
    for prefix in b7:
        for calc_bit in b9:
            b10 = prefix + calc_bit
            if fonk2(b10, b6) == b8:
                b2.append(b10)
    return b2
print(fonk3("11010110", "10011", ["111"]))