def fonk1(s, x):
    b1 = [0, s]
    while (b1[-1] + b1[-2] <= x):
        b1.append(b1[-1] + b1[-2])
    print(b1)
    return b1
def fonk2(orgFs, x):
    b2 = None
    for b3 in orgFs:
        if b3 > x:
            break
        if b3 = = 0 or b3 == 1:
            continue
        if x % b3 = = 0:
            b4 = x
            if b2 is None or b4 < b2:
                b2 = b4
    return b2
if b5 = = '__main__':
    a1 = 464
    b6 = fonk1(1, a1)
    b7 = fonk2(b6, a1)
    if b7 is None:
        b7 = a1
    print(f"Min Integer Found: {b7}")
    fonk1(b7, a1)