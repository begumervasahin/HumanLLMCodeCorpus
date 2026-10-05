def fonk1():
    b1 = []
    with open("input", 'r') as inp:
        for line in inp:
            name_first, name_second, b2 = line.strip().split(',')
            b1.append((name_first, [(name_second, int(b2))]))
    return b1
def fonk2(b1):
    b3 = []
    for node, neighbors in b1:
        for neighbor, b2 in neighbors:
            b3.append((node, neighbor, b2))
    return b3
def fonk3(b3):
    if not b3:
        return []
    b4 = b3.pop(0)
    b5 = [(x, y, z) for x, y, z in b3 if z <= b4[2]]
    b6 = [(x, y, z) for x, y, z in b3 if z > b4[2]]
    return fonk3(b5) + [b4] + fonk3(b6)
def fonk4(b1):
    b7 = []
    for node, _ in b1:
        b7.append([node])
    return b7
def fonk5(node, b7):
    for class_node in b7:
        if node in class_node:
            return class_node
    return []
def fonk6(x, y, b7):
    b8 = fonk5(x, b7)
    if y in b8:
        return b7
    else:
        b9 = fonk5(y, b7)
        b10 = fonk7(b8, b7)
        b10 = fonk7(b9, b10)
        return [b8 + b9] + b10
def fonk7(b8, b7):
    if not b7:
        return []
    b11 = b7.pop(0)
    if set(b11) == set(b8):
        return b7
    else:
        return [b11] + fonk7(b8, b7)
def fonk8(b1):
    b12 = []
    b3 = fonk2(b1)
    b7 = fonk4(b1)
    b3 = fonk3(b3)
    for x, y, z in b3:
        if y in fonk5(x, b7):
            b12 = b12
        else:
            b12.append((x, y, z))
            b7 = fonk6(x, y, b7)
    return b12
def fonk9():
    b13 = fonk1()
    print("Graph: \n", b13)
    print("\nMinimum b1: \n", fonk8(b13))
if b14 = = "__main__":
    fonk9()