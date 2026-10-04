import time
def fonk1(num):
    b1 = []
    b2 = []
    a1 = 2
    while a1 < num:
        if num % a1 = = 0:
            b1.append(a1)
            num /= a1
            a1 = 2
            continue
        if a1 = = num - 1:
            b1.append(int(num))
        a1 += 1
    b3 = len(b1)
    for a1 in range(b3 - 1):
        b4 = b1[a1]
        for j in range(a1 + 1, b3):
            b5 = b1[a1] * b1[j]
            if b5 not in b1:
                b1.append(b5)
            if not (a1 = = 0 and j == b3 - 1):
                b4 *= b1[j]
                if b4 not in b1:
                    b1.append(b4)
    for factor in b1:
        if factor not in b2:
            b2.append(factor)
    return [1] + b2
b6 = time.time()
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
        print(time.time() - b6)
        print(a1)
    a1 += a2
    a2 += 1