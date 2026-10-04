import time
b1 = time.time()
def fonk1(b4):
    b2 = list()
    b3 = list()
    a1 = 2
    while a1 < b4:
        if b4%a1 = = 0:
            b2.append(a1)
            b4 = int(b4/a1)
            a1 = 2
            continue
        if a1 = = b4-1:
            b2.append(b4)
        a1 += 1
    print(b2)
    print(len(b2), sum(b2))
    a1 = 0
    b5 = len(b2)
    while a1 < b5-1:
        b6 = a1+1
        b7 = b2[a1]
        while b6 < b5 and b5 > 2:
            b8 = b2[a1]*b2[b6]
            if b8 not in b2:
                b2.append(b8)
            if not (a1 = = 0 and b6==b5-1):
                b7*=b2[b6]
                if b7 not in b2:
                    b2.append(b7)
            b6+=1
        a1+=1
    for x in b2:
        if x not in b3:
            b3.append(x)
    return [1]+b3
print(fonk1(33550336))
print(time.time()-b1)