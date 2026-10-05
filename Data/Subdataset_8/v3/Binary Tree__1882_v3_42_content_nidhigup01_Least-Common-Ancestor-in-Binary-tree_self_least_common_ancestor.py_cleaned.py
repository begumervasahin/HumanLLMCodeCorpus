class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def build_tree_from_adjacency_matrix(adjacency_matrix, key, parent):
    node = TreeNode(key)
    if not adjacency_matrix or not adjacency_matrix[key]:
        return None
    for child in range(len(adjacency_matrix[key])):
        if adjacency_matrix[key][child] == 1 and child != parent:
            if child < key:
                node.left = build_tree_from_adjacency_matrix(adjacency_matrix, child, key)
            else:
                node.right = build_tree_from_adjacency_matrix(adjacency_matrix, child, key)
    return node
def find_lowest_common_ancestor(root, node1, node2):
    if root is None:
        return None
    if root.key == node1 or root.key == node2:
        return root
    left_lca = find_lowest_common_ancestor(root.left, node1, node2)
    right_lca = find_lowest_common_ancestor(root.right, node1, node2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca
def find_lca(adjacency_matrix, key, node1, node2):
    root = build_tree_from_adjacency_matrix(adjacency_matrix, key, -1)
    lca_node = find_lowest_common_ancestor(root, node1, node2)
    return lca_node.key if lca_node else None
print("LCA(1, 4) =", find_lca([[0, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [1, 0, 0, 0, 1],
                                [0, 0, 0, 0, 0]], key=3, node1=1, node2=4))