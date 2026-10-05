class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def find_LCA(matrix, root_key, node1, node2):
    root = TreeNode(root_key)
    if root is None or matrix is None or matrix == [[]]:
        return None
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    for child in range(num_columns):
        if matrix[root_key][child] == 1 and child <= root_key:
            root.left = child
        elif matrix[root_key][child] == 1 and child > root_key:
            root.right = child
    if root.key == node1 or root.key == node2:
        return root
    left_lca = find_LCA(matrix, root.left, node1, node2)
    right_lca = find_LCA(matrix, root.right, node1, node2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca
print("LCA(4,5) = ", find_LCA([[0, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [1, 0, 0, 0, 1],
                                [0, 0, 0, 0, 0]], root_key=3, node1=1, node2=4))