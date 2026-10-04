import itertools
def fonk1(num):
    b1 = list(itertools.product([0, 1], repeat=num))
    b2 = [''.join(map(str, tpl)) for tpl in b1]
    return b2
def fonk2(b4, b5):
    b3 = '0' * (len(b5) - 1)
    b4 = list(b4 + b3)
    b5 = list(b5)
    for i in range(len(b4) - len(b3)):
        if b4[i] == '1':
            for j in range(len(b5)):
                b4[i + j] = str(int(b4[i + j]) ^ int(b5[j]))
    return ''.join(b4[-len(b3):])
def fonk3(b4, b5, b6 = None):
    b7 = fonk2(b4, b5)
    b2 = fonk1(len(b5))
    b8 = []
    if b6 is None:
        b6 = fonk1(len(b4) - len(b5))
    for prefix in b6:
        for calc_bit in b2:
            b9 = prefix + calc_bit
            if fonk2(b9, b5) == b7:
                b8.append(b9)
    return b8
if b10 = = "__main__":
    b4 = "11010110"
    b5 = "10011"
    b11 = ["111"]
    b12 = fonk3(b4, b5, b11)
    print("Collisions:")
    for collision in b12:
        print(collision)