def fonk1(b6, b1 = 0, desc=0):
    def fonk2(b5, b2 = 0):
        b3 = b2 + b5
        b4 = len(b6)
        if b2 < 0 or b3 >= b4:
            return
        if b1 = = 2:
            print("Sub:", b2, "-", b3, "::", b6)
        if b6[b2] > b6[b3]:
            b6[b2], b6[b3] = b6[b3], b6[b2]
            fonk2(b5, b2 - b5)
        fonk2(b5, b2 + 1)
    b5 = len(b6)
    while b5:
        if b1:
            print("Gap:", b5)
        fonk2(b5)
        b5
    if desc:
        b6 = b6[::-1]
    return b6