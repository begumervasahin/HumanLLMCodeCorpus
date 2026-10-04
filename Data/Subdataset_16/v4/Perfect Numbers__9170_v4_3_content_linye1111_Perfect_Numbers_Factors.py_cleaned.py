import time
def fonk1(a2):
    b1 = []
    b2 = []
    a1 = 2
    while a1 < a2:
        if a2 % a1 = = 0:
            b1.append(a1)
            a2
            a1 = 2
            continue
        if a1 = = a2 - 1:
            b1.append(a2)
        a1 += 1
    print("Initial factors:", b1)
    print("Number of factors:", len(b1), "Sum of factors:", sum(b1))
    for a1 in range(len(b1) - 1):
        b3 = b1[a1]
        for j in range(a1 + 1, len(b1)):
            b4 = b1[a1] * b1[j]
            if b4 not in b1:
                b1.append(b4)
            b3 *= b1[j]
            if b3 not in b1:
                b1.append(b3)
    for x in b1:
        if x not in b2:
            b2.append(x)
    return [1] + b2
if b5 = = "__main__":
    b6 = time.time()
    a2 = 33550336
    print("Factors of", a2, ":", fonk1(a2))
    print("Execution time:", time.time() - b6)