def fonk1():
    import random
    b1 = random.sample(xrange(100001), 100)
    return b1
fonk1()
def fonk2(b1):
    print b1
    for i in range(0,len(b1)):
        b2 = i
        for j in range(i,len(b1)):
            if b1[j]<b1[b2]:
                b2 = j
        b3 = b1[i]
        b1[i] = b1[b2]
        b1[b2] = b3
    print b1
fonk2(fonk1())