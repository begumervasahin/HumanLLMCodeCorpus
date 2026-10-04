class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)
def get_max(root):
    while root and root.right:
        root = root.right
    return root
def get_min(root):
    while root and root.left:
        root = root.left
    return root
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root
def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))
def delete_node(root, data):
    if root is None:
        return None
    if data < root.data:
        root.left = delete_node(root.left, data)
    elif data > root.data:
        root.right = delete_node(root.right, data)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        min_node = get_min(root.right)
        root.data = min_node.data
        root.right = delete_node(root.right, min_node.data)
    return root
def find_lca(root, x, y):
    if root is None:
        return None
    if root.data < x and root.data < y:
        return find_lca(root.right, x, y)
    if root.data > x and root.data > y:
        return find_lca(root.left, x, y)
    return root
def sorted_array_to_bst(arr):
    if not arr:
        return None
    mid = len(arr)
    root = Node(arr[mid])
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid + 1:])
    return root
def main():
    root = None
    nodes = [6, 7, -2, 4, 1, 9, 11, 5]
    for node in nodes:
        root = insert(root, node)
    print("In-order traversal of the BST:")
    inorder(root)
    print()
    x, y = 1, 5
    ancestor = find_lca(root, x, y)
    if ancestor:
        print(f"The lowest common ancestor of {x} and {y} is: {ancestor.data}")
    else:
        print(f"There is no common ancestor for {x} and {y}")
if __name__ == '__main__':
    main()