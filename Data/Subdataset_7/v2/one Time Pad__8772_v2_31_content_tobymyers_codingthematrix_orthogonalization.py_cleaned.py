
def fonk1(b3, v, b1 = 1E-20):
    b2 = ((b3 * v) / (v * v)) if v * v > b1 else 0
    return b2 * v
def fonk2(b3, vlist):
    for v in vlist:
        b3 = b3 - fonk1(b3, v)
    return b3
def fonk3(b3, vlist, b1 = 1E-20):
    b4 = {len(vlist): 1}
    for i, v in enumerate(vlist):
        b2 = (b3 * v) / (v * v) if v * v > b1 else 0
        b4[i] = b2
        b3 = b3 - b2 * v
    return (b3, b4)
def fonk4(vlist):
    assert isinstance(vlist, list)
    b5 = []
    for v in vlist:
        b5.append(fonk2(v, b5))
    return b5
def fonk5(vlist):
    assert isinstance(vlist, list)
    b5 = []
    b6 = []
    b7 = set(range(len(vlist)))
    for v in vlist:
        (vstar, sigmadict) = fonk3(v, b5)
        b5.append(vstar)
        b6.append(Vec(b7, sigmadict))
    return b5, b6