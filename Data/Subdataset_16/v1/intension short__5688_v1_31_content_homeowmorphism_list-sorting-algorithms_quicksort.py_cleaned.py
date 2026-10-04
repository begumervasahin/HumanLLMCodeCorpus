import random
def fonk1(b8):
    b1 = len(b8)
    if b1 > 1:
        b2 = random.randint(0, b1-1)
        b3 = b8[b2]
        print("Pivoting", b3, "in", b8)
        b4 = []
        b5 = []
        b6 = [b3]
        for b7 in range(b1):
            if b7 = = b2:
                continue
            elif b8[b7] < b3:
                b4.append(b8[b7])
            elif b8[b7] > b3:
                b5.append(b8[b7])
            else:
                b6.append(b8[b7])
        print("Left becomes", b4, "; b5 becomes", b5)
        return fonk1(b4) + b6 + fonk1(b5)
    return b8
b8 = [random.randint(1, 100) for _ in range(10)]
print("Unsorted list:", b8)
print("Sorted list:", fonk1(b8))