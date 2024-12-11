import itertools
def fonk1(num_bits):
    b1 = itertools.product([0, 1], repeat=num_bits)
    b2 = [''.join(map(str, bits)) for bits in b1]
    return b2
def fonk2(message, b5):
    b3 = '0' * (len(b5) - 1)
    b4 = message + b3
    b4 = list(b4)
    b5 = list(b5)
    for i in range(len(b4) - len(b3)):
        if b4[i] == '1':
            for j in range(len(b5)):
                b4[i + j] = str(int(b4[i + j]) ^ int(b5[j]))
    return ''.join(b4[-len(b3):])
def fonk3(message, b5, b6 = None):
    b7 = fonk2(message, b5)
    b8 = fonk1(len(b5))
    b9 = []
    if b6 is None:
        b6 = fonk1(len(message) - len(b5))
    for prefix in b6:
        for combination in b8:
            b10 = prefix + combination
            if fonk2(b10, b5) == b7:
                b9.append(b10)
    return b9
print(fonk3("11010110", "10011", ["111"]))