class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def build_tree_left():
    root_data = int(input("Enter data (-1 for no node): "))
    if root_data == -1:
        return None
    root = BinaryTree(root_data)
    root.left = build_tree_left()
    root.right = build_tree_left()
    return root
def print_tree_left(root):
    if root is None:
        return
    print(f"{root.data}:", end="")
    if root.left:
        print(f"{root.left.data}", end=",")
    else:
        print("-1", end=",")
    if root.right:
        print(f"{root.right.data}")
    else:
        print("-1")
    print_tree_left(root.left)
    print_tree_left(root.right)
def count_nodes(root):
    if root is None:
        return 0
    left_count = count_nodes(root.left)
    right_count = count_nodes(root.right)
    return left_count + right_count + 1
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
def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1
def print_at_depth_k(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data, end=" ")
        return
    print_at_depth_k(root.left, k-1)
    print_at_depth_k(root.right, k-1)
def replace_node_with_depth_k(root, depth=0):
    if root is None:
        return
    root.data = depth
    replace_node_with_depth_k(root.left, depth+1)
    replace_node_with_depth_k(root.right, depth+1)
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
        return None
    root.left, root.right = root.right, root.left
    mirror_tree(root.left)
    mirror_tree(root.right)
    return root
def build_tree_levelwise():
    root_data = int(input("Enter root data: "))
    if root_data == -1 or root_data < 0:
        return None
    root = BinaryTree(root_data)
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current = q.get()
        left_data = int(input(f"Enter left child of {current.data}: "))
        if left_data != -1:
            left_child = BinaryTree(left_data)
            current.left = left_child
            q.put(left_child)
        right_data = int(input(f"Enter right child of {current.data}: "))
        if right_data != -1:
            right_child = BinaryTree(right_data)
            current.right = right_child
            q.put(right_child)
    return root
def print_tree_levelwise(root):
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current = q.get()
        print(f"{current.data}:", end="")
        if current.left:
            print(f"{current.left.data}", end=",")
            q.put(current.left)
        if current.right:
            print(f"{current.right.data}", end="")
            q.put(current.right)
        print()
if __name__ == "__main__":
    import queue
    root = build_tree_left()
    print_tree_left(root)
    node_count = count_nodes(root)
    print(f"Number of nodes: {node_count}")
    print("Preorder traversal:")
    preorder_traversal(root)
    print()
    print("Inorder traversal:")
    inorder_traversal(root)
    print()
    print("Postorder traversal:")
    postorder_traversal(root)
    print()
    tree_height = height(root)
    print(f"Height of the tree: {tree_height}")
    print("Nodes at depth 2:")
    print_at_depth_k(root, 2)
    print()
    replace_node_with_depth_k(root)
    print("Tree after replacing node values with their depth:")
    print_tree_left(root)
    root = remove_leaves(root)
    print("Tree after removing leaf nodes:")
    print_tree_left(root)
    root = mirror_tree(root)
    print("Mirrored tree:")
    print_tree_left(root)
    root = build_tree_levelwise()
    print("Level-wise tree:")
    print_tree_levelwise(root)