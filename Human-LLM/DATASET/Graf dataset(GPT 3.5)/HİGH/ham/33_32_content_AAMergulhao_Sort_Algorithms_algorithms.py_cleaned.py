def fonk1(lista):
    if len(lista) <= 1:
        return lista
    b1 = lista[0]
    b2 = [b7 for b7 in lista if b7 == b1]
    b3 = [b7 for b7 in lista if b7 <  b1]
    b4 = [b7 for b7 in lista if b7 >  b1]
    return fonk1(b3) + \
           b2 + fonk1(b4)
def fonk2(v):
    b5 = []
    b6 = []
    for i in range(len(v)):
        b7 = v[i]
        b5.append(b7)
    while b5:
        b8 = min(b5)
        b6.append(b8)
        b5.remove(b8)
    return b6
def fonk3(b11, b12):
    b9 = []
    i, b10 = 0, 0
    while i < len(b11) and b10 < len(b12):
        if b11[i] <= b12[b10]:
            b9.append(b11[i])
            i += 1
        else:
            b9.append(b12[b10])
            b10 += 1
    b9 += b11[i:]
    b9 += b12[b10:]
    return b9
def fonk4(v):
    if len(v) <= 1:
        return v
    else:
        b8 = len(v)
        b11 = fonk4(v[:b8])
        b12 = fonk4(v[b8:])
        return fonk3(b11, b12)