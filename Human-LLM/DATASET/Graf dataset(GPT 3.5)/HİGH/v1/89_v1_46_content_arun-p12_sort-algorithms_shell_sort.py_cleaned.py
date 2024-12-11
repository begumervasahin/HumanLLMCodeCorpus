def fonk1(b5, b1 = 0, desc=0):
    def fonk2(b4, b2 = 0):
        j, b3 = (b4 + b2), len(b5)
        if b2 < 0 or j >= len(b5):
            return
        if b1 = = 2:
            print("Sub:", b2, "-", j, "::", b5)
        if b5[b2] > b5[j]:
            b5[b2], b5[j] = b5[j], b5[b2]
            fonk2(b4, b2 - b4)
        fonk2(b4, b2 + 1)
    b4 = len(b5)
    while b4:
        if b1:
            print("Gap:", b4)
        fonk2(b4, 0)
        b4
    if desc:
        b5 = b5[::-1]
    return b5