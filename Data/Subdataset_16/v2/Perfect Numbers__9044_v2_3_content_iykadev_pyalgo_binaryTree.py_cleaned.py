def fonk1(root_val):
    return [root_val, [], []]
def fonk2(b4, new_branch):
    b1 = b4.pop(1)
    if len(b1) > 1:
        b4.insert(1, [new_branch, b1, []])
    else:
        b4.insert(1, [new_branch, [], []])
    return b4
def fonk3(b4, new_branch):
    b2 = b4.pop(2)
    if len(b2) > 1:
        b4.insert(2, [new_branch, [], b2])
    else:
        b4.insert(2, [new_branch, [], []])
    return b4
def fonk4(b4):
    return b4[0]
def fonk5(b4, new_val):
    b4[0] = new_val
def fonk6(b4):
    return b4[1]
def fonk7(b4):
    return b4[2]
if b3 = = "__main__":
    b4 = fonk1(3)
    fonk2(b4, 4)
    fonk2(b4, 5)
    fonk3(b4, 6)
    fonk3(b4, 7)
    b5 = fonk6(b4)
    print("Left child of b4:", b5)
    fonk5(b5, 9)
    print("Tree after setting left child's b4 value to 9:", b4)
    fonk2(b5, 11)
    print("Tree after inserting 11 to the left of the left child:", b4)
    b6 = fonk7(fonk7(b4))
    print("Right child of the right child of the b4:", b6)