def create_binary_tree(root_value):
    return [root_value, [], []]
def insert_left_child(root, new_branch):
    left_subtree = root.pop(1)
    if len(left_subtree) > 1:
        root.insert(1, [new_branch, left_subtree, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root
def insert_right_child(root, new_branch):
    right_subtree = root.pop(2)
    if len(right_subtree) > 1:
        root.insert(2, [new_branch, [], right_subtree])
    else:
        root.insert(2, [new_branch, [], []])
    return root
def get_root_value(root):
    return root[0]
def set_root_value(root, new_value):
    root[0] = new_value
def get_left_child(root):
    return root[1]
def get_right_child(root):
    return root[2]
binary_tree = create_binary_tree(3)
insert_left_child(binary_tree, 4)
insert_left_child(binary_tree, 5)
insert_right_child(binary_tree, 6)
insert_right_child(binary_tree, 7)
left_child = get_left_child(binary_tree)
print(left_child)
set_root_value(left_child, 9)
print(binary_tree)
insert_left_child(left_child, 11)
print(binary_tree)
right_right_child = get_right_child(get_right_child(binary_tree))
print(right_right_child)