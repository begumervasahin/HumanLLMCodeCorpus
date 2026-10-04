class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
def inorder_traversal(node, result=None):
    if result is None:
        result = []
    if node:
        inorder_traversal(node.left, result)
        if node.val is not None:
            result.append(node.val)
        inorder_traversal(node.right, result)
    return result
def preorder_traversal(node, result=None):
    if result is None:
        result = []
    if node:
        if node.val is not None:
            result.append(node.val)
        preorder_traversal(node.left, result)
        preorder_traversal(node.right, result)
    return result
def populate_tree(values, index=0):
    if index < len(values) and values[index] is not None:
        node = TreeNode(values[index])
        node.left = populate_tree(values, 2 * index + 1)
        node.right = populate_tree(values, 2 * index + 2)
        return node
    return None
def print_traversal_result(title, result):
    print(title)
    for value in result:
        print(value)
    print(" ")
test_arrays = [
    [1, None, 2, None, None, 3],
    [1, 2, 3, 4, 5, 6, None],
    [1, 2, 3]
]
for arr in test_arrays:
    root = populate_tree(arr)
    inorder_result = inorder_traversal(root)
    print_traversal_result("In-order Traversal", inorder_result)
    preorder_result = preorder_traversal(root)
    print_traversal_result("Pre-order Traversal", preorder_result)