def fonk1(b1):
    a1 = 0
    while b1 > 1:
        a1 += 1
        if b1 % 2:
            b1 = 3 * b1 + 1
        else:
            b1 = b1 / 2
        print(b1)
def fonk2(b1):
    fonk1(b1)
fonk2(15000)