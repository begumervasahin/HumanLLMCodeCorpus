from b1 import div_rule
def fonk1(b2,b4):
    b1 = div_rule(b4)
    a1 = 0
    b2 = b2[::-1]
    for i in b2:
        b3 = b1.__next__()
        a1 += int(i) * b3
        print(a1)
        if abs(a1) > 3*b4:
            if a1 > 0:
                a1 -= 3*b4
            else:
                a1 += 3*b4
    return a1 % b4 = = 0