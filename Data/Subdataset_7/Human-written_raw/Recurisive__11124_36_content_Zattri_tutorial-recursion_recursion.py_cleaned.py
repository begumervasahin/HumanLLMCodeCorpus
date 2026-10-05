import binary
def fonk1(b1):
    print(b1)
    if b1 > 0:
        fonk1(b1-1)
def fonk2(b1):
    if b1 = = 0:
        return 1
    else:
        return b1 * fonk2(b1 - 1)
def fonk3(b1, b2 = 1):
    if b1 = = 0:
        return b2
    else:
        return fonk3(b1-1, b2 * b1)
b3 = binary.Node(0)
b4 = binary.Node(1)
b5 = binary.Node(2)
b6 = binary.Node(3)
b7 = binary.Node(4)
b8 = binary.Node(5)
b3.addLeft(b4)
b3.addRight(b5)
b4.addLeft(b6)
b5.addLeft(b7)
b5.addRight(b8)
def fonk4(root):
    print(root.b9)
    if (root.l or root.r):
        if root.l:
            print("Left")
            fonk4(root.l)
        if root.r:
            print("Right")
            fonk4(root.r)
    else:
        print("Up")
def fonk5(root, val):
    if (root.b9 = = val):
        print("Found")
    else:
        if (root.l or root.r):
            if root.l:
                fonk5(root.l, val)
            if root.r:
                fonk5(root.r, val)
def fonk6(b1):
    b10 = []
    if len(b1) < 2:
        return b1
    b11 = int(len(b1) / 2)
    b12 = fonk6(b1[:b11])
    b13 = fonk6(b1[b11:])
    a1 = 0
    a2 = 0
    while a1 < len(b12) and a2 < len(b13):
        if b12[a1] > b13[a2]:
            b10.append(b13[a2])
            a2 += 1
        else:
            b10.append(b12[a1])
            a1 += 1
    b10 += b12[a1:]
    b10 += b13[a2:]
    return b10