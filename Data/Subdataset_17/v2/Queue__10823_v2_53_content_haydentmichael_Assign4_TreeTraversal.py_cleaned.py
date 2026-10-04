class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def inorder_traversal(result_list, node):
    if node:
        inorder_traversal(result_list, node.left)
        if node.value is not None:
            result_list.append(node.value)
        inorder_traversal(result_list, node.right)
    return result_list
def preorder_traversal(result_list, node):
    if node:
        if node.value is not None:
            result_list.append(node.value)
        preorder_traversal(result_list, node.left)
        preorder_traversal(result_list, node.right)
    return result_list
def build_tree_from_list(values, root, index, length):
    if index < length:
        node = TreeNode(values[index])
        root = node
        root.left = build_tree_from_list(values, root.left, 2 * index + 1, length)
        root.right = build_tree_from_list(values, root.right, 2 * index + 2, length)
    return root
def print_traversal(traversal, traversal_type):
    print(f"{traversal_type} Traversal:")
    for value in traversal:
        print(value)
    print()
if __name__ == "__main__":
    tree_arrays = [
        [1, None, 2, None, None, 3],
        [1, 2, 3, 4, 5, 6, None],
        [1, 2, 3]
    ]
    for index, tree_values in enumerate(tree_arrays):
        num_elements = len(tree_values)
        root = build_tree_from_list(tree_values, None, 0, num_elements)
        inorder_result = inorder_traversal([], root)
        preorder_result = preorder_traversal([], root)
        print(f"Tree {index + 1}: {tree_values}")
        print_traversal(inorder_result, "In-order")
        print_traversal(preorder_result, "Pre-order")