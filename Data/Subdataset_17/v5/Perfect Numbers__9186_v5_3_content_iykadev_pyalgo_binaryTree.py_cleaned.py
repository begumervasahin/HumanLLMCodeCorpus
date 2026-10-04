def create_binary_tree(root_val):
    return [root_val, [], []]
def insert_left(root, new_branch):
    left_subtree = root.pop(1)
    if left_subtree:
        root.insert(1, [new_branch, left_subtree, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root
def insert_right(root, new_branch):
    right_subtree = root.pop(2)
    if right_subtree:
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
def print_tree(tree, level=0):
    if tree:
        print("  " * level + str(tree[0]))
        if len(tree) > 1:
            print_tree(tree[1], level + 1)
        if len(tree) > 2:
            print_tree(tree[2], level + 1)
if __name__ == "__main__":
    r = create_binary_tree(3)
    insert_left(r, 4)
    insert_left(r, 5)
    insert_right(r, 6)
    insert_right(r, 7)
    print("Initial tree structure:")
    print_tree(r)
    left_child = get_left_child(r)
    print("\nLeft child:", left_child)
    set_root_val(left_child, 9)
    print("\nTree after setting left child root value to 9:")
    print_tree(r)
    insert_left(left_child, 11)
    print("\nTree after inserting 11 to the left of left child:")
    print_tree(r)
    right_of_right = get_right_child(get_right_child(r))
    print("\nRight child of the right child:", right_of_right)