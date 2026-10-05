def fonk1(b4, b1 = 0, desc=0):
    for i in range(1, len(b4)):
        b2 = b4[i]
        b3 = i - 1
        while b3 >= 0 and b4[b3] > b2:
            b4[b3 + 1] = b4[b3]
            b3 -= 1
            if b1 = = 2:
                print("Sub:", b3, "::", b4)
        b4[b3 + 1] = b2
        if b1:
            print("Iteration", i, ":", b4)
    if desc:
        b4 = b4[::-1]
    return b4
