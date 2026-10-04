def fonk1(b3):
    return [b3, [], []]
def fonk2(root, new_branch):
    b1 = root.pop(1)
    if len(b1) > 1:
        root.insert(1, [new_branch, b1, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root
def fonk3(root, new_branch):
    b1 = root.pop(2)
    if len(b1) > 1:
        root.insert(2, [new_branch, [], b1])
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
if b2 = = "__main__":
    b3 = fonk1(3)
    fonk2(b3, 4)
    fonk2(b3, 5)
    fonk3(b3, 6)
    fonk3(b3, 7)
    b4 = fonk6(b3)
    print("Left child of root:", b4)
    fonk5(b4, 9)
    print("Tree after setting left child's root value to 9:", b3)
    fonk2(b4, 11)
    print("Tree after inserting 11 to the left of the left child:", b3)
    print("Right child of the right child of the root:", fonk7(fonk7(b3)))