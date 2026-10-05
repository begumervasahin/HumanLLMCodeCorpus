class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def build_tree_left():
    root_data = int(input())
    if root_data == -1:
        return None
    root = BinaryTree(root_data)
    left_part = build_tree_left()
    right_part = build_tree_left()
    root.left = left_part
    root.right = right_part
    return root
def print_tree_left(root):
    if root is None:
        return
    if root.data != -1:
        print(root.data, end=":")
    if root.left is not None:
        print(root.left.data, end=",")
    else:
        print("-1", end=",")
    if root.right is not None:
        print(root.right.data, end="")
    else:
        print("-1", end="")
    print()
    print_tree_left(root.left)
    print_tree_left(root.right)
root = build_tree_left()
print_tree_left(root)
def count_nodes(root):
    if root is None:
        return 0
    left_count = count_nodes(root.left)
    right_count = count_nodes(root.right)
    return left_count + right_count + 1
node_count = count_nodes(root)
print(node_count)
def preorder_traversal(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)
preorder_traversal(root)
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.data, end=" ")
    inorder_traversal(root.right)
inorder_traversal(root)
def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=" ")
postorder_traversal(root)
def calculate_height(root):
    if root is None:
        return 0
    left_subtree_height = calculate_height(root.left)
    right_subtree_height = calculate_height(root.right)
    return max(left_subtree_height, right_subtree_height) + 1
tree_height = calculate_height(root)
print(tree_height)
def print_at_depth_k(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data)
    print_at_depth_k(root.left, k - 1)
    print_at_depth_k(root.right, k - 1)
print_at_depth_k(root, 2)
def replace_with_depth_k(root, count):
    if root is None:
        return
    root.data = count
    replace_with_depth_k(root.left, count + 1)
    replace_with_depth_k(root.right, count + 1)
replace_with_depth_k(root, 0)
print_tree_left(root)
def remove_leaves(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return None
    root.left = remove_leaves(root.left)
    root.right = remove_leaves(root.right)
    return root
def mirror_tree(root):
    if root is None:
        return
    if root.left is not None and root.right is not None:
        temp = root.left
        root.left = root.right
        root.right = temp
    mirror_tree(root.left)
    mirror_tree(root.right)
    return root
root1 = mirror_tree(root)
print_tree_left(root1)
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
import queue
def take_input_level_wise():
    root_data = int(input())
    if root_data == -1 or root_data < 0:
        return None
    root = BinaryTreeNode(root_data)
    q.put(root)
    while not q.empty():
        current = q.get()
        print("Enter the left child of:", current.data)
        left = int(input())
        if left != -1:
            left_child = BinaryTreeNode(left)
            current.left = left_child
            q.put(left_child)
        print("Enter the right child of:", current.data)
        right = int(input())
        if right != -1:
            right_child = BinaryTreeNode(right)
            current.right = right_child
            q.put(right_child)
    return root
def print_level_wise(root):
    if root is None:
        return None
    q.put(root)
    while not q.empty():
        current = q.get()
        print(current.data, end=":")
        if current.left is not None:
            print(current.left.data, end=",")
            q.put(current.left)
        if current.right is not None:
            print(current.right.data, end="")
            q.put(current.right)
        print()
root = take_input_level_wise()
print_level_wise(root)
def construct_tree_from_post_and_inorder(postorder, inorder):
    if len(postorder) == 0:
        return None
    root_data = postorder[len(postorder) - 1]
    postorder.pop()
    root = BinaryTreeNode(root_data)
    index = -1
    for i in range(len(inorder)):
        if inorder[i] == root_data:
            index = i
            break
    inorder_left = inorder[0:index]
    inorder_right = inorder[index + 1:]
    postorder_left = postorder[0:len(inorder_left)]
    postorder_right = postorder[len(inorder_left):]
    left_subtree = construct_tree_from_post_and_inorder(postorder_left, inorder_left)
    right_subtree = construct_tree_from_post_and_inorder(postorder_right, inorder_right)
    root.left = left_subtree
    root.right = right_subtree
    return root
def calculate_diameter(root, max_diameter):
    if root is None:
        return max_diameter