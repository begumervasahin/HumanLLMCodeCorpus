class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def build_tree():
    root_data = int(input("Enter node value (-1 for no node): "))
    if root_data == -1:
        return None
    root = BinaryTree(root_data)
    root.left = build_tree()
    root.right = build_tree()
    return root
def print_tree(root):
    if root is None:
        return
    print(f"{root.data}:", end="")
    if root.left:
        print(f"{root.left.data},", end="")
    else:
        print("-1,", end="")
    if root.right:
        print(f"{root.right.data}")
    else:
        print("-1")
    print_tree(root.left)
    print_tree(root.right)
def count_nodes(root):
    if root is None:
        return 0
    left_count = count_nodes(root.left)
    right_count = count_nodes(root.right)
    return 1 + left_count + right_count
def preorder_traversal(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.data, end=" ")
    inorder_traversal(root.right)
def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=" ")
def tree_height(root):
    if root is None:
        return 0
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return max(left_height, right_height) + 1
def print_nodes_at_depth_k(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data, end=" ")
        return
    print_nodes_at_depth_k(root.left, k - 1)
    print_nodes_at_depth_k(root.right, k - 1)
def replace_node_with_depth(root, depth):
    if root is None:
        return
    root.data = depth
    replace_node_with_depth(root.left, depth + 1)
    replace_node_with_depth(root.right, depth + 1)
def remove_leaves(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return None
    root.left = remove_leaves(root.left)
    root.right = remove_leaves(root.right)
    return root
def mirror_tree(root):
    if root is None:
        return
    root.left, root.right = root.right, root.left
    mirror_tree(root.left)
    mirror_tree(root.right)
    return root
import queue
class BinaryTreeLevelwise:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def take_input_levelwise():
    root_data = int(input("Enter root node value: "))
    if root_data == -1:
        return None
    root = BinaryTreeLevelwise(root_data)
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current = q.get()
        left_data = int(input(f"Enter left child of {current.data}: "))
        if left_data != -1:
            left_child = BinaryTreeLevelwise(left_data)
            current.left = left_child
            q.put(left_child)
        right_data = int(input(f"Enter right child of {current.data}: "))
        if right_data != -1:
            right_child = BinaryTreeLevelwise(right_data)
            current.right = right_child
            q.put(right_child)
    return root
def print_levelwise(root):
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current = q.get()
        print(f"{current.data}:", end="")
        if current.left:
            print(f"{current.left.data},", end="")
            q.put(current.left)
        else:
            print("-1,", end="")
        if current.right:
            print(f"{current.right.data}")
            q.put(current.right)
        else:
            print("-1")
def build_tree_from_post_in(postorder, inorder):
    if not postorder:
        return None
    root_data = postorder.pop()
    root = BinaryTreeLevelwise(root_data)
    index = inorder.index(root_data)
    in_left = inorder[:index]
    in_right = inorder[index + 1:]
    post_left = postorder[:len(in_left)]
    post_right = postorder[len(in_left):]
    root.left = build_tree_from_post_in(post_left, in_left)
    root.right = build_tree_from_post_in(post_right, in_right)
    return root
if __name__ == "__main__":
    root = build_tree()
    print_tree(root)
    print(f"Total nodes: {count_nodes(root)}")
    print("Preorder traversal:")
    preorder_traversal(root)
    print("\nInorder traversal:")
    inorder_traversal(root)
    print("\nPostorder traversal:")
    postorder_traversal(root)
    print(f"\nTree height: {tree_height(root)}")
    k = int(input("Enter depth k: "))
    print(f"Nodes at depth {k}:")
    print_nodes_at_depth_k(root, k)
    print()
    replace_node_with_depth(root, 0)
    print("Tree after replacing nodes with their depth:")
    print_tree(root)
    root = remove_leaves(root)
    print("Tree after removing leaves:")
    print_tree(root)
    root = mirror_tree(root)
    print("Mirrored tree:")
    print_tree(root)
    root_levelwise = take_input_levelwise()
    print_levelwise(root_levelwise)
    postorder = [4, 5, 2, 6, 7, 3, 1]
    inorder = [4, 2, 5, 1, 6, 3, 7]
    root_from_post_in = build_tree_from_post_in(postorder, inorder)
    print_levelwise(root_from_post_in)