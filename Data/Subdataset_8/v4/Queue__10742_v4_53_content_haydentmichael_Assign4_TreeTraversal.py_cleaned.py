class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def inorderTraversal(root, a=None):
    if a is None:
        a = []
    if root:
        inorderTraversal(root.left, a)
        if root.val is not None:
            a.append(root.val)
        inorderTraversal(root.right, a)
    return a
def preorderTraversal(root, a=None):
    if a is None:
        a = []
    if root:
        if root.val is not None:
            a.append(root.val)
        preorderTraversal(root.left, a)
        preorderTraversal(root.right, a)
    return a
def populateTree(arr, i, n):
    root = None
    if i < n:
        if arr[i] is not None:
            root = TreeNode(arr[i])
            root.left = populateTree(arr, 2 * i + 1, n)
            root.right = populateTree(arr, 2 * i + 2, n)
    return root
arr1 = [1, None, 2, None, None, 3]
n = len(arr1)
root2 = populateTree(arr1, 0, n)
print("In-order Traversal")
for x in inorderTraversal(root2):
    print(x)
print()
print("Pre-order Traversal")
for x in preorderTraversal(root2):
    print(x)
print()
arr2 = [1, 2, 3, 4, 5, 6, None]
n1 = len(arr2)
root3 = populateTree(arr2, 0, n1)
print("In-order Traversal")
for x in inorderTraversal(root3):
    print(x)
print()
print("Pre-order Traversal")
for x in preorderTraversal(root3):
    print(x)
arr3 = [1, 2, 3]
n2 = len(arr3)
root4 = populateTree(arr3, 0, n2)
print("In-order Traversal")
for x in inorderTraversal(root4):
    print(x)
print()
print("Pre-order Traversal")
for x in preorderTraversal(root4):
    print(x)