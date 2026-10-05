import itertools
def fonk1(length):
    b1 = list(itertools.product([0, 1], repeat=length))
    b2 = []
    for bit_tuple in b1:
        b3 = "".join(map(str, bit_tuple))
        b2.append(b3)
    return b2
def fonk2(b13, b14):
    b4 = '0' * (len(b14) - 1)
    b5 = b13 + b4
    b6 = list(b5)
    b7 = list(b14)
    for i in range(len(b5) - len(b4)):
        if b6[i] == '1':
            for j in range(len(b14)):
                b6[i + j] = str(int(b6[i + j]) ^ int(b7[j]))
    return ''.join(b6[-len(b4):])
def fonk3(b13, b14, b8 = None):
    b9 = fonk2(b13, b14)
    b10 = fonk1(len(b14))
    b11 = []
    if b8 is None:
        b8 = fonk1(len(b13) - len(b14))
    for prefix in b8:
        for bit_combination in b10:
            b12 = prefix + bit_combination
            if fonk2(b12, b14) == b9:
                b11.append(b12)
    return b11
b13 = "11010110"
b14 = "10011"
b8 = ["111"]
print(fonk3(b13, b14, b8))