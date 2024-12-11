def fonk1():
    b1 = []
    b2 = ""
    b3 = ""
    a1 = 0
    b4 = file("input", 'r')
    b5 = b4.read()
    a2 = 0
    b6 = len(b5)
    while a2 < b6:
        b2 = ""
        b3 = ""
        a1 = 0
        while b5[a2] != ',':
            b2 += b5[a2]
            a2 += 1
        a2 += 1
        while b5[a2] != ',':
            b3 += b5[a2]
            a2 += 1
        a2 += 1
        while b5[a2] != '\n':
            a1 = b5[a2]
            a2 += 1
        b7 = (b2, [(b3, a1)])
        b1.append(b7)
        a2 += 1
    return b1
def fonk2(b1):
    b8 = []
    for (x, y) in b1:
        for a2, j in y:
            b9 = (x, a2, j)
            b8.append(b9)
    return b8
def fonk3(b8):
    b10 = []
    b11 = []
    if not b8:
        return []
    b12 = b8.pop(0)
    for (x, y, z) in b8:
        if z <= b12[2]:
            b10.append((x, y, z))
        else:
            b11.append((x, y, z))
    b10 = fonk3(b10)
    b11 = fonk3(b11)
    return b10 + [b12] + b11
def fonk4(b1):
    b13 = []
    for (x, y) in b1:
        b13.append([x])
    return b13
def fonk5(x, vert):
    if not vert:
        return []
    else:
        for tmp in vert:
            if x in tmp:
                return tmp
        return []
def fonk6(x, y, vert):
    b14 = fonk5(x, vert)
    if y in b14:
        return vert
    else:
        b15 = fonk5(y, vert)
        b16 = fonk7(b14, vert)
        b17 = fonk7(b15, b16)
        return [b14 + b15] + b17
def fonk7(b14, vert):
    if not vert:
        return []
    else:
        b18 = vert.pop(0)
        if set(b18) == set(b14):
            return vert
        else:
            return [b18] + (fonk7(b14, vert))
def fonk8(b1):
    b19 = []
    b8 = fonk2(b1)
    b20 = fonk4(b1)
    b8 = fonk3(b8)
    for (x, y, z) in b8:
        if y in fonk5(x, b20):
            b19 = b19
        else:
            b19.append((x, y, z))
            b20 = fonk6(x, y, b20)
    return b19
def fonk9():
    b21 = fonk1()
    print "Graph: \n", b21
    print "\nMinimum b1: \n", fonk8(b21)
fonk9()