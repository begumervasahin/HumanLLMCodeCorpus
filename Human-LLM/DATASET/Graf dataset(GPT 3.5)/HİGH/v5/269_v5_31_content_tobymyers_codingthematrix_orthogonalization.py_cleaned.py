from vec import Vec
def fonk1(b4, v, b1 = 1E-20):
    b2 = v * v
    b3 = ((b4 * v) / b2) if b2 > b1 else 0
    return b3 * v
def fonk2(b4, vlist):
    for v in vlist:
        b4 = b4 - fonk1(b4, v)
    return b4
def fonk3(b4, vlist, b1 = 1E-20):
    b5 = {len(vlist): 1}
    for i, v in enumerate(vlist):
        b2 = v * v
        b3 = (b4 * v) / b2 if b2 > b1 else 0
        b5[i] = b3
        b4 = b4 - b3 * v
    return b4, b5
def fonk4(vlist):
    b6 = []
    for v in vlist:
        b6.append(fonk2(v, b6))
    return b6
def fonk5(vlist):
    b6 = []
    b7 = []
    b8 = set(range(len(vlist)))
    for v in vlist:
        vstar, b9 = fonk3(v, b6)
        b6.append(vstar)
        b7.append(Vec(b8, b9))
    return b6, b7