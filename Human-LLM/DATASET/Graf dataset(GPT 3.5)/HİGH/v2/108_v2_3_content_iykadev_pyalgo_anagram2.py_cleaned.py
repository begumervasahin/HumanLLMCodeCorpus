def fonk1(s1, s2):
    b1 = list(s1)
    b2 = list(s2)
    b1.sort()
    b2.sort()
    a1 = 0
    b3 = True
    while a1 < len(s1) and b3:
        if b1[a1] == b2[a1]:
            a1 += 1
        else:
            b3 = False
    return b3
print(fonk1('ey edip', 'pide ye'))
