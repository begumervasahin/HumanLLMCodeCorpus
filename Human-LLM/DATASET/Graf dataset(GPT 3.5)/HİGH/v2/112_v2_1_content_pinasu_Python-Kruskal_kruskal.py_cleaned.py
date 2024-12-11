def fonk1():
    b1 = []
    with open("input", 'r') as inp:
        for line in inp:
            nameF, nameS, b2 = line.strip().split(',')
            b2 = int(b2)
            b3 = (nameF, [(nameS, b2)])
            b1.append(b3)
    return b1
def fonk2(b1):
    b4 = []
    for x, y_list in b1:
        for i, j in y_list:
            b5 = (x, i, j)
            b4.append(b5)
    return b4
def fonk3(b4):
    b6 = []
    b7 = []
    if not b4:
        return []
    b8 = b4.pop(0)
    for (x, y, z) in b4:
        if z <= b8[2]:
            b6.append((x, y, z))
        else:
            b7.append((x, y, z))
    b6 = fonk3(b6)
    b7 = fonk3(b7)
    return b6 + [b8] + b7
def fonk4(b1):
    b9 = []
    for x, y_list in b1:
        b9.append([x])
    return b9
def fonk5(x, vert):
    for tmp in vert:
        if x in tmp:
            return tmp
    return []
def fonk6(x, y, vert):
    b10 = fonk5(x, vert)
    if y in b10:
        return vert
    else:
        b11 = fonk5(y, vert)
        b12 = fonk7(b10, vert)
        b13 = fonk7(b11, b12)
        return [b10 + b11] + b13
def fonk7(b10, vert):
    if not vert:
        return []
    b14 = vert.pop(0)
    if set(b14) == set(b10):
        return vert
    else:
        return [b14] + (fonk7(b10, vert))
def fonk8(b1):
    b15 = []
    b4 = fonk2(b1)
    b16 = fonk4(b1)
    b4 = fonk3(b4)
    for (x, y, z) in b4:
        if y in fonk5(x, b16):
            b15 = b15
        else:
            b15.append((x, y, z))
            b16 = fonk6(x, y, b16)
    return b15
def fonk9():
    b17 = fonk1()
    print("Graph: \n", b17)
    print("\nMinimum b1: \n", fonk8(b17))
if b18 = = "__main__":
    fonk9()