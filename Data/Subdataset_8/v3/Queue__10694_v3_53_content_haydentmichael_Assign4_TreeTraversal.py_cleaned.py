class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
def preorder_traversal(root):
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)
def populate_tree(arr, i):
    if i < len(arr):
        if arr[i] is None:
            return None
        root = TreeNode(arr[i])
        root.left = populate_tree(arr, 2 * i + 1)
        root.right = populate_tree(arr, 2 * i + 2)
        return root
    return None
def test_tree_traversal(arr):
    root = populate_tree(arr, 0)
    print("Inorder Traversal:")
    print(inorder_traversal(root))
    print("")
    print("Preorder Traversal:")
    print(preorder_traversal(root))
    print("")
arr1 = [1, None, 2, None, None, 3]
test_tree_traversal(arr1)
arr2 = [1, 2, 3, 4, 5, 6, None]
test_tree_traversal(arr2)
arr3 = [1, 2, 3]
test_tree_traversal(arr3)