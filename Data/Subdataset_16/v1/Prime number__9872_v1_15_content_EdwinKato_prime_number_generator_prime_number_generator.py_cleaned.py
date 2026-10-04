def fonk1(n):
    a1 = 2
    b1 = []
    while a1 <= n:
        b2 = True
        a2 = 2
        while a2 < a1:
            if a1 % a2 = = 0:
                b2 = False
                break
            a2 += 1
        if b2:
            b1.append(a1)
        a1 += 1
    return b1
print(fonk1(10))