def fonk1(lista):
    if len(lista) <= 1:
        return lista
    b1 = lista[0]
    b2 = [x for x in lista if x == b1]
    b3 = [x for x in lista if x < b1]
    b4 = [x for x in lista if x > b1]
    return fonk1(b3) + b2 + fonk1(b4)
def fonk2(v):
    b5 = []
    while v:
        b6 = min(v)
        b5.append(b6)
        v.remove(b6)
    return b5
def fonk3(b10, b11):
    b7 = []
    i, b8 = 0, 0
    while i < len(b10) and b8 < len(b11):
        if b10[i] <= b11[b8]:
            b7.append(b10[i])
            i += 1
        else:
            b7.append(b11[b8])
            b8 += 1
    b7 += b10[i:]
    b7 += b11[b8:]
    return b7
def fonk4(v):
    if len(v) <= 1:
        return v
    else:
        b9 = len(v)
        b10 = fonk4(v[:b9])
        b11 = fonk4(v[b9:])
        return fonk3(b10, b11)