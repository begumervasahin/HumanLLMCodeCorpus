def fonk1(s,x):
    b1 = [0,s]
    a1 = 2
    while (b1[a1-1] + b1[a1-2] <= x):
        b1.append(b1[a1-1] + b1[a1-2])
        a1 += 1
    print b1
    return b1
def fonk2( orgFs, x):
    b2 = None
    for b3 in orgFs:
        if b3 > x:
            break
        if b3 = = 0 or b3 == 1:
            continue
        if x % b3 = = 0:
            if b2 is None:
                b2 = x/b3
            else:
                if x/b3 <= b2:
                    b2 = x/b3
    return b2
if b4 = = '__main__':
    a2 = 464
    b5 = fonk1(1,a2)
    b6 = fonk2(b5, a2)
    if b6 is None:
        b6 = a2
    print "Min Interger Found:%d" % b6
    fonk1(b6, a2)