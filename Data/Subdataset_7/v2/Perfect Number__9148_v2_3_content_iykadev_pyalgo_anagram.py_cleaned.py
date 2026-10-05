def fonk1(s1, s2):
    b1 = list(s2)
    a1 = 0
    b2 = True
    while a1 < len(s1) and b2:
        a2 = 0
        b3 = False
        while a2 < len(b1) and not b3:
            if s1[a1] == b1[a2]:
                b3 = True
            else:
                a2 += 1
        if b3:
            b1[a2] = None
        else:
            b2 = False
        a1 += 1
    return b2
print(fonk1('ey edip', 'pide ye'))
