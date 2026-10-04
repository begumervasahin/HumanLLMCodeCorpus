class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)
def get_max(root):
    current = root
    while current and current.right:
        current = current.right
    return current
def get_min(root):
    current = root
    while current and current.left:
        current = current.left
    return current
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
def delete(root, data):
    if root is None:
        return root
    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        temp = get_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root
def find_lca(root, x, y):
    while root:
        if root.data < x and root.data < y:
            root = root.right
        elif root.data > x and root.data > y:
            root = root.left
        else:
            break
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