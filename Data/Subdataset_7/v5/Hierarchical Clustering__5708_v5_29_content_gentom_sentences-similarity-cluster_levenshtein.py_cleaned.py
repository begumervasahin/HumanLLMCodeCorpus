def fonk1(s1, b1):
    if len(s1) > len(b1):
        s1, b1 = b1, s1
    b2 = list(range(len(s1) + 1))
    for i2, c2 in enumerate(b1):
        b3 = [i2 + 1]
        for i1, b4 in enumerate(s1):
            if b4 = = c2:
                b3.append(b2[i1])
            else:
                b3.append(1 + min(b2[i1], b2[i1 + 1], b3[-1]))
        b2 = b3
    return b2[-1]
def fonk2(s1, b1):
    if len(s1) < len(b1):
        return fonk2(b1, s1)
    if len(b1) == 0:
        return len(s1)
    b5 = list(range(len(b1) + 1))
    for i, b4 in enumerate(s1):
        b6 = [i + 1]
        for j, c2 in enumerate(b1):
            b7 = b5[j + 1] + 1
            b8 = b6[j] + 1
            b9 = b5[j] + (b4 != c2)
            b6.append(min(b7, b8, b9))
        b5 = b6
    return b5[-1]