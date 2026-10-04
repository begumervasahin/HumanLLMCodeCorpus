def fonk1(b1, b2):
    b1 = b1.replace(" ", "").lower()
    b2 = b2.replace(" ", "").lower()
    b3 = list(b1)
    b4 = list(b2)
    b3.sort()
    b4.sort()
    a1 = 0
    b5 = True
    while a1 < len(b3) and b5:
        if b3[a1] == b4[a1]:
            a1 += 1
        else:
            b5 = False
    return b5
if b6 = = "__main__":
    b7 = fonk1('ey edip', 'pide ye')
    print(b7)
