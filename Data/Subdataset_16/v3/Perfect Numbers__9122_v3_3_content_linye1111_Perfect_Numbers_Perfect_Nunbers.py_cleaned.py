import time
def fonk1(num):
    b1 = []
    b2 = []
    a1 = 2
    while a1 < num:
        if num % a1 = = 0:
            b1.append(a1)
            num
            a1 = 2
            continue
        if a1 = = num - 1:
            b1.append(num)
        a1 += 1
    for a1 in range(len(b1)):
        b3 = b1[a1]
        for j in range(a1 + 1, len(b1)):
            b4 = b1[a1] * b1[j]
            if b4 not in b1:
                b1.append(b4)
            b3 *= b1[j]
            if b3 not in b1:
                b1.append(b3)
    b2 = list(set(b1))
    return [1] + b2
def fonk2():
    b5 = time.time()
    a2 = 3
    a1 = 3
    print(6)
    while True:
        if a1 % 9 != 1:
            a1 += a2
            a2 += 1
            continue
        b1 = fonk1(a1)
        if sum(b1) == a1:
            print(time.time() - b5)
            print(a1)
        a1 += a2
        a2 += 1
if b6 = = "__main__":
    fonk2()