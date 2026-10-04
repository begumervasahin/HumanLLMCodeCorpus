class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def inorder_traversal(result, root):
    if root:
        inorder_traversal(result, root.left)
        if root.val is not None:
            result.append(root.val)
        inorder_traversal(result, root.right)
    return result
def preorder_traversal(result, root):
    if root:
        if root.val is not None:
            result.append(root.val)
        preorder_traversal(result, root.left)
        preorder_traversal(result, root.right)
    return result
def populate_tree(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
        root.left = populate_tree(arr, root.left, 2 * i + 1, n)
        root.right = populate_tree(arr, root.right, 2 * i + 2, n)
    return root
def print_traversal_result(title, result):
    print(title)
    for x in result:
        print(x)
    print(" ")
arrays = [
    [1, None, 2, None, None, 3],
    [1, 2, 3, 4, 5, 6, None],
    [1, 2, 3]
]
for arr in arrays:
    n = len(arr)
    root = None
    root = populate_tree(arr, root, 0, n)
    inorder_result = []
    inorder_result = inorder_traversal(inorder_result, root)
    print_traversal_result("In-order Traversal", inorder_result)
    preorder_result = []
    preorder_result = preorder_traversal(preorder_result, root)
    print_traversal_result("Pre-order Traversal", preorder_result)