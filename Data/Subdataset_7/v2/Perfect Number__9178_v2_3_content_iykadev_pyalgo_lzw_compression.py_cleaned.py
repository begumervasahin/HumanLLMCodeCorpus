def fonk1(uncompressed):
    a1 = 256
    b1 = {chr(i): chr(i) for i in range(a1)}
    b2 = ""
    b3 = []
    for char in uncompressed:
        b4 = b2 + char
        if b4 in b1:
            b2 = b4
        else:
            b3.append(b1[b2])
            b1[b4] = a1
            a1 += 1
            b2 = char
    if b2:
        b3.append(b1[b2])
    return b3
def fonk2(b8):
    a1 = 256
    b1 = {chr(i): chr(i) for i in range(a1)}
    b5 = []
    b2 = b8.pop(0)
    b5.append(b2)
    for b7 in b8:
        if b7 in b1:
            b6 = b1[b7]
        elif b7 = = a1:
            b6 = b2 + b2[0]
        else:
            raise ValueError('Bad b8 b7: %s' % b7)
        b5.append(b6)
        b1[a1] = b2 + b6[0]
        a1 += 1
        b2 = b6
    return ''.join(b5)
b8 = fonk1('ALIALIALIALIALI')
print("Compressed:", b8)
b9 = fonk2(b8)
print("Decompressed:", b9)