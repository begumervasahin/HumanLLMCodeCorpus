def fonk1(root_val):
    return [root_val, [], []]
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
def fonk5(root, new_val):
    root[0] = new_val
def fonk6(root):
    return root[1]
def fonk7(root):
    return root[2]
def fonk8(tree, b3 = 0):
    if tree:
        print("  " * b3 + str(tree[0]))
        if len(tree) > 1:
            fonk8(tree[1], b3 + 1)
        if len(tree) > 2:
            fonk8(tree[2], b3 + 1)
if b4 = = "__main__":
    b5 = fonk1(3)
    fonk2(b5, 4)
    fonk2(b5, 5)
    fonk3(b5, 6)
    fonk3(b5, 7)
    print("Initial tree structure:")
    fonk8(b5)
    b6 = fonk6(b5)
    print("\nLeft child:", b6)
    fonk5(b6, 9)
    print("\nTree after setting left child root value to 9:")
    fonk8(b5)
    fonk2(b6, 11)
    print("\nTree after inserting 11 to the left of left child:")
    fonk8(b5)
    b7 = fonk7(fonk7(b5))
    print("\nRight child of the right child:", b7)