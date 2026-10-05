class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)
def get_maximum_node(root):
    prev = None
    while root:
        prev = root
        root = root.right
    return prev
def insert_node(root, data):
    if root is None:
        root = Node(data)
    elif root.data > data:
        root.left = insert_node(root.left, data)
    else:
        root.right = insert_node(root.right, data)
    return root
def search_node(root, key):
    if root is None or root.data == key:
        return root
    else:
        if root.data > key:
            return search_node(root.left, key)
        else:
            return search_node(root.right, key)
def get_minimum_node(root):
    prev = None
    while root:
        prev = root
        root = root.left
    return prev
def tree_height(root):
    if root:
        return 1 + max(tree_height(root.left), tree_height(root.right))
    return 0
def delete_node(root, data):
    if root is None:
        return None
    if root.data < data:
        root.right = delete_node(root.right, data)
    elif root.data > data:
        root.left = delete_node(root.left, data)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        minimum = get_minimum_node(root.right)
        root.data = minimum.data
        root.right = delete_node(root.right, minimum.data)
    return root
def lowest_common_ancestor(root, key1, key2):
    if key1 > key2:
        key1, key2 = key2, key1
    if root is None:
        return None
    if root.data >= key1 and root.data <= key2:
        return root
    else:
        if root.data > key1 and root.data > key2:
            return lowest_common_ancestor(root.left, key1, key2)
        else:
            return lowest_common_ancestor(root.right, key1, key2)
def sorted_array_to_bst(arr):
    if not arr:
        return None
    mid = len(arr)
    root = Node(arr[mid])
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid+1:])
    return root
def lca_bst(root, x, y):
    if root is None:
        return None
    if (root.data < x and root.data < y):
        return lca_bst(root.right, x, y)
    if (root.data > x and root.data > y):
        return lca_bst(root.left, x, y)
    return root
root = None
root = insert_node(root, 6)
root = insert_node(root, 7)
root = insert_node(root, -2)
root = insert_node(root, 4)
root = insert_node(root, 1)
root = insert_node(root, 9)
root = insert_node(root, 11)
root = insert_node(root, 5)
print("In-order Traversal:")
inorder_traversal(root)
print()
print("Lowest Common Ancestor of 1 and 5:", lca_bst(root, 1, 5).data)