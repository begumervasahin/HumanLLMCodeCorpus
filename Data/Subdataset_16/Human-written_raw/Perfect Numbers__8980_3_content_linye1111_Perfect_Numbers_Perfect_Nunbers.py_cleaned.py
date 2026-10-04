import time
b1 = time.time()
a1 = 3
def fonk1(num):
    b2 = list()
    b3 = list()
    a2 = 2
    while a2 < num:
        if num%a2 = = 0:
            b2.append(a2)
            num /= a2
            a2 = 2
            continue
        if a2 = = num-1:
            b2.append(num)
        a2 += 1
    a2 = 0
    b4 = len(b2)
    while a2 < b4-1:
        b5 = a2+1
        b6 = b2[a2]
        while b5 < b4 and b4 > 2:
            b7 = b2[a2]*b2[b5]
            if b7 not in b2:
                b2.append(b7)
            if not (a2 = = 0 and b5==b4-1):
                b6*=b2[b5]
                if b6 not in b2:
                    b2.append(b6)
            b5+=1
        a2+=1
    for x in b2:
        if x not in b3:
            b3.append(x)
    return [1]+b3
a2 = 3
print(6)
while True:
    if not a2%b8 = = 1:
        a2 += a1
        a1 += 1
        continue
    b2 = fonk1(a2)
    if sum(b2) == a2:
        print(time.time() - b1)
        print(a2)
    a2 += a1
    a1 += 1