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
    a1 = 0
    b3 = len(b1)
    while a1 < b3 - 1:
        b4 = a1 + 1
        b5 = b1[a1]
        while b4 < b3 and b3 > 2:
            b6 = b1[a1] * b1[b4]
            if b6 not in b1:
                b1.append(b6)
            if not (a1 = = 0 and b4 == b3 - 1):
                b5 *= b1[b4]
                if b5 not in b1:
                    b1.append(b5)
            b4 += 1
        a1 += 1
    for x in b1:
        if x not in b2:
            b2.append(x)
    return [1] + b2
b7 = time.time()
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
        print(time.time() - b7)
        print(a1)
    a1 += a2
    a2 += 1