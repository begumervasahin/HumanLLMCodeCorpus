import binary
def fonk1(b1):
    print(b1)
    if b1 > 0:
        fonk1(b1 - 1)
def fonk2(b1):
    if b1 = = 0:
        return 1
    else:
        return b1 * fonk2(b1 - 1)
def fonk3(b1, b2 = 1):
    if b1 = = 0:
        return b2
    else:
        return fonk3(b1 - 1, b2 * b1)
b3 = binary.Node(0)
b4 = binary.Node(1)
b5 = binary.Node(2)
b6 = binary.Node(3)
b7 = binary.Node(4)
b8 = binary.Node(5)
b3.add_left(b4)
b3.add_right(b5)
b4.add_left(b6)
b5.add_left(b7)
b5.add_right(b8)
def fonk4(root):
    print(root.b9)
    if root.left:
        print("Left")
        fonk4(root.left)
    if root.right:
        print("Right")
        fonk4(root.right)
    print("Up")
def fonk5(root, val):
    if root.b9 = = val:
        print("Found")
    elif root.left:
        fonk5(root.left, val)
    elif root.right:
        fonk5(root.right, val)
def fonk6(b1):
    if len(b1) < 2:
        return b1
    b10 = len(b1)
    b11 = fonk6(b1[:b10])
    b12 = fonk6(b1[b10:])
    return fonk7(b11, b12)
def fonk7(b11, b12):
    b13 = []
    b14 = j = 0
    while b14 < len(b11) and j < len(b12):
        if b11[b14] > b12[j]:
            b13.append(b12[j])
            j += 1
        else:
            b13.append(b11[b14])
            b14 += 1
    b13.extend(b11[b14:])
    b13.extend(b12[j:])
    return b13