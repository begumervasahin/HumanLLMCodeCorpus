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
def getMax(root):
    current = root
    while current and current.right:
        current = current.right
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
def getMin(root):
    current = root
    while current and current.left:
        current = current.left
    return current
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
        temp = getMin(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root
def lca(root, x, y):
    while root:
        if root.data < x and root.data < y:
            root = root.right
        elif root.data > x and root.data > y:
            root = root.left
        else:
            break
    return root
def sortedArrayToBST(arr):
    if not arr:
        return None
    mid = len(arr)
    root = Node(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])
    return root
root = None
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, -2)
root = insert(root, 4)
root = insert(root, 1)
root = insert(root, 9)
root = insert(root, 11)
root = insert(root, 5)
inorder(root)
print()
print("LCA of 1 and 5:", lca(root, 1, 5).data)