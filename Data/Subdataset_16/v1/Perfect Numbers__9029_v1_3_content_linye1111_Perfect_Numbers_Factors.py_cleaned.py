import time
def fonk1(b3):
    b1 = []
    b2 = []
    a1 = 2
    while a1 < b3:
        if b3 % a1 = = 0:
            b1.append(a1)
            b3 = b3
            a1 = 2
            continue
        if a1 = = b3 - 1:
            b1.append(b3)
        a1 += 1
    print(b1)
    print(len(b1), sum(b1))
    a1 = 0
    b4 = len(b1)
    while a1 < b4 - 1:
        b5 = a1 + 1
        b6 = b1[a1]
        while b5 < b4 and b4 > 2:
            b7 = b1[a1] * b1[b5]
            if b7 not in b1:
                b1.append(b7)
            if not (a1 = = 0 and b5 == b4 - 1):
                b6 *= b1[b5]
                if b6 not in b1:
                    b1.append(b6)
            b5 += 1
        a1 += 1
    for x in b1:
        if x not in b2:
            b2.append(x)
    return [1] + b2
if b8 = = '__main__':
    b9 = time.time()
    b10 = fonk1(33550336)
    print(b10)
    print("Execution time:", time.time() - b9)