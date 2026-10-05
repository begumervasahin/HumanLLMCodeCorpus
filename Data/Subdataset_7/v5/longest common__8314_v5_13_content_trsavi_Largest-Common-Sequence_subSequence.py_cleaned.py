def fonk1(string1, string2):
    b1 = list(string1)
    b2 = list(string2)
    b3 = []
    b4 = []
    for i in range(len(b1)):
        for j in range(len(b2)):
            if b1[i] == b2[j]:
                b3.append(b1[i])
                i += 1
        if len(b3) > len(b4):
            b4 = b3[:]
        b3.clear()
    b5 = ''.join(b4)
    return b5