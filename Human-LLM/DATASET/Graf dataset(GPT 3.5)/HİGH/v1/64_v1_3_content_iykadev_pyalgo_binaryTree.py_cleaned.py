def fonk1(b2):
    return [b2, [], []]
def fonk2(root, newBranch):
    b1 = root.pop(1)
    if len(b1) > 1:
        root.insert(1, [newBranch, b1, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root
def fonk3(root, newBranch):
    b1 = root.pop(2)
    if len(b1) > 1:
        root.insert(2, [newBranch, [], b1])
    else:
        root.insert(2, [newBranch, [], []])
    return root
def fonk4(root):
    return root[0]
def fonk5(root, newVal):
    root[0] = newVal
def fonk6(root):
    return root[1]
def fonk7(root):
    return root[2]
b2 = fonk1(3)
fonk2(b2, 4)
fonk2(b2, 5)
fonk3(b2, 6)
fonk3(b2, 7)
b3 = fonk6(b2)
print("Left child of root:", b3)
fonk5(b3, 9)
print("Updated tree:", b2)
fonk2(b3, 11)
print("Updated tree after inserting 11 as left child of 9:", b2)
print("Right child of right child of root:", fonk7(fonk7(b2)))