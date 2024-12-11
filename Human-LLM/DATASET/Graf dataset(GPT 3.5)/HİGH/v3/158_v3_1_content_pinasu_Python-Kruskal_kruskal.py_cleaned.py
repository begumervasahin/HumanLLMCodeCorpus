def fonk1(b16):
    b1 = []
    with open(b16, 'r') as file:
        for line in file:
            name1, name2, b2 = line.strip().split(',')
            b2 = int(b2)
            b3 = (name1, [(name2, b2)])
            b1.append(b3)
    return b1
def fonk2(b1):
    b4 = []
    for vertex, adj_list in b1:
        for neighbor, b2 in adj_list:
            b5 = (vertex, neighbor, b2)
            b4.append(b5)
    return b4
def fonk3(b4):
    if not b4:
        return []
    b6 = b4[0]
    b7 = [b5 for b5 in b4[1:] if b5[2] <= b6[2]]
    b8 = [b5 for b5 in b4[1:] if b5[2] > b6[2]]
    return fonk3(b7) + [b6] + fonk3(b8)
def fonk4(b1):
    b9 = []
    for vertex, _ in b1:
        b9.append([vertex])
    return b9
def fonk5(vertex, b9):
    for class_ in b9:
        if vertex in class_:
            return class_
    return []
def fonk6(vertex1, vertex2, b9):
    b10 = fonk5(vertex1, b9)
    b11 = fonk5(vertex2, b9)
    if vertex2 in b10:
        return b9
    else:
        b12 = fonk7(b11, b9)
        return [b10 + b11] + b12
def fonk7(class_, b9):
    if not b9:
        return []
    b13 = b9[0]
    if set(b13) == set(class_):
        return b9[1:]
    else:
        return [b13] + fonk7(class_, b9[1:])
def fonk8(b1):
    b14 = []
    b4 = fonk2(b1)
    b9 = fonk4(b1)
    b15 = fonk3(b4)
    for b5 in b15:
        vertex1, vertex2, b2 = b5
        if vertex2 in fonk5(vertex1, b9):
            continue
        else:
            b14.append(b5)
            b9 = fonk6(vertex1, vertex2, b9)
    return b14
def fonk9():
    b16 = "input"
    b1 = fonk1(b16)
    print("Graph:\n", b1)
    print("\nMinimum Spanning Tree:\n", fonk8(b1))
if b17 = = "__main__":
    fonk9()