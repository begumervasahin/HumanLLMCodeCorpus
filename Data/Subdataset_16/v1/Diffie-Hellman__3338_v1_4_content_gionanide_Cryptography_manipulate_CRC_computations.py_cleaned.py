import itertools
def fonk1(num_bits):
    b1 = list(itertools.product([0, 1], repeat=num_bits))
    return [''.join(map(str, t)) for t in b1]
def fonk2(b3, b4):
    b2 = '0' * (len(b4) - 1)
    b3 = b3 + b2
    b3 = list(b3)
    b4 = list(b4)
    for i in range(len(b3) - len(b2)):
        if b3[i] == '1':
            for j in range(len(b4)):
                b3[i + j] = str(int(b3[i + j]) ^ int(b4[j]))
    return ''.join(b3[-len(b2):])
def fonk3(b3, b4, b5 = None):
    b6 = fonk2(b3, b4)
    b7 = fonk1(len(b4))
    b8 = []
    if b5 is None:
        b5 = fonk1(len(b3) - len(b4))
    for prefix in b5:
        for candidate in b7:
            b9 = prefix + candidate
            if fonk2(b9, b4) == b6:
                b8.append(b9)
    return b8
if b10 = = "__main__":
    b3 = "11010110"
    b4 = "10011"
    b5 = ["111"]
    b11 = fonk3(b3, b4, b5)
    print("Collisions found:")
    for collision in b11:
        print(collision)