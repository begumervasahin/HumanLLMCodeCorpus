def BinaryTree(r):
    return [r, [], []]
def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root
def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root
def get_root_val(root):
    return root[0]
def set_root_val(root, new_val):
    root[0] = new_val
def get_left_child(root):
    return root[1]
def get_right_child(root):
    return root[2]
if __name__ == "__main__":
    r = BinaryTree(3)
    insert_left(r, 4)
    insert_left(r, 5)
    insert_right(r, 6)
    insert_right(r, 7)
    l = get_left_child(r)
    print("Left child of root:", l)
    set_root_val(l, 9)
    print("Tree after setting left child's root value to 9:", r)
    insert_left(l, 11)
    print("Tree after inserting 11 to the left of the left child:", r)
    print("Right child of the right child of the root:", get_right_child(get_right_child(r)))