def fonk1(root_value):
    return [root_value, [], []]
def fonk2(root, new_branch):
    b1 = root.pop(1)
    if b1:
        root.insert(1, [new_branch, b1, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root
def fonk3(root, new_branch):
    b2 = root.pop(2)
    if b2:
        root.insert(2, [new_branch, [], b2])
    else:
        root.insert(2, [new_branch, [], []])
    return root
def fonk4(root):
    return root[0]
def fonk5(root, new_value):
    root[0] = new_value
def fonk6(root):
    return root[1]
def fonk7(root):
    return root[2]
b3 = fonk1(3)
fonk2(b3, 4)
fonk2(b3, 5)
fonk3(b3, 6)
fonk3(b3, 7)
b4 = fonk6(b3)
print(b4)
fonk5(b4, 9)
print(b3)
fonk2(b4, 11)
print(b3)
b5 = fonk7(fonk7(b3))
print(b5)