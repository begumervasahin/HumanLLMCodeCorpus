import itertools
def fonk1(length):
    b1 = list(itertools.product([0, 1], repeat=length))
    b2 = [''.join(map(str, bit_tuple)) for bit_tuple in b1]
    return b2
def fonk2(b12, b13):
    b3 = '0' * (len(b13) - 1)
    b4 = b12 + b3
    b5 = list(b4)
    b6 = list(b13)
    for i in range(len(b4) - len(b3)):
        if b5[i] == '1':
            for j in range(len(b13)):
                b5[i + j] = str(int(b5[i + j]) ^ int(b6[j]))
    return ''.join(b5[-len(b3):])
def fonk3(b12, b13, b7 = None):
    b8 = fonk2(b12, b13)
    b9 = fonk1(len(b13))
    b10 = []
    if b7 is None:
        b7 = fonk1(len(b12) - len(b13))
    for prefix in b7:
        for bit_combination in b9:
            b11 = prefix + bit_combination
            if fonk2(b11, b13) == b8:
                b10.append(b11)
    return b10
b12 = "11010110"
b13 = "10011"
b7 = ["111"]
print(fonk3(b12, b13, b7))