def fonk1(root_val):
    return [root_val, [], []]
def fonk2(root, new_branch):
    b1 = root.pop(1)
    if len(b1) > 1:
        root.insert(1, [new_branch, b1, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root
def fonk3(root, new_branch):
    b2 = root.pop(2)
    if len(b2) > 1:
        root.insert(2, [new_branch, [], b2])
    else:
        root.insert(2, [new_branch, [], []])
    return root
def fonk4(root):
    return root[0]
def fonk5(root, new_val):
    root[0] = new_val
def fonk6(root):
    return root[1]
def fonk7(root):
    return root[2]
if b3 = = "__main__":
    b4 = fonk1(3)
    fonk2(b4, 4)
    fonk2(b4, 5)
    fonk3(b4, 6)
    fonk3(b4, 7)
    b5 = fonk6(b4)
    print("Left child:", b5)
    fonk5(b5, 9)
    print("Tree after setting left child root value to 9:", b4)
    fonk2(b5, 11)
    print("Tree after inserting 11 to the left of left child:", b4)
    b6 = fonk7(fonk7(b4))
    print("Right child of the right child:", b6)