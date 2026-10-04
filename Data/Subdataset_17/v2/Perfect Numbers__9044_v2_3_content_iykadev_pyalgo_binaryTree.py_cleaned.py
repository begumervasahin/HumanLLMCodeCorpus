def BinaryTree(root_val):
    return [root_val, [], []]
def insert_left(root, new_branch):
    left_subtree = root.pop(1)
    if len(left_subtree) > 1:
        root.insert(1, [new_branch, left_subtree, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root
def insert_right(root, new_branch):
    right_subtree = root.pop(2)
    if len(right_subtree) > 1:
        root.insert(2, [new_branch, [], right_subtree])
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
    root = BinaryTree(3)
    insert_left(root, 4)
    insert_left(root, 5)
    insert_right(root, 6)
    insert_right(root, 7)
    left_child = get_left_child(root)
    print("Left child of root:", left_child)
    set_root_val(left_child, 9)
    print("Tree after setting left child's root value to 9:", root)
    insert_left(left_child, 11)
    print("Tree after inserting 11 to the left of the left child:", root)
    right_child_of_right_child = get_right_child(get_right_child(root))
    print("Right child of the right child of the root:", right_child_of_right_child)