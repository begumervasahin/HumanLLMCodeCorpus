def fonk1(uncompressed):
    b1 = {chr(i): chr(i) for i in range(256)}
    b2 = []
    b3 = ""
    for c in uncompressed:
        b4 = b3 + c
        if b4 in b1:
            b3 = b4
        else:
            b2.append(b1[b3])
            b1[b4] = len(b1)
            b3 = c
    if b3:
        b2.append(b1[b3])
    return b2
def fonk2(b7):
    from io import StringIO
    b1 = {chr(i): chr(i) for i in range(256)}
    b2 = StringIO()
    b3 = b7.pop(0)
    b2.write(b3)
    for b6 in b7:
        if b6 in b1:
            b5 = b1[b6]
        elif b6 = = len(b1):
            b5 = b3 + b3[0]
        else:
            raise ValueError('Bad b7 symbol: %s' % b6)
        b2.write(b5)
        b1[len(b1)] = b3 + b5[0]
        b3 = b5
    return b2.getvalue()
b7 = fonk1('ALIALIALIALIALI')
print("Compressed:", b7)
b8 = fonk2(b7)
print("Decompressed:", b8)