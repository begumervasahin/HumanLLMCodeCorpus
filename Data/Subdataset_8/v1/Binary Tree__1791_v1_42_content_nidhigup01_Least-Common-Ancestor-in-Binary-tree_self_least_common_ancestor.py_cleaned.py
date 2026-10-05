class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def findLCA(T, key, n1, n2):
    def build_tree(T, key, parent):
        node = Node(key)
        if not T or not T[key]:
            return None
        for child in range(len(T[key])):
            if T[key][child] == 1 and child != parent:
                if child < key:
                    node.left = build_tree(T, child, key)
                else:
                    node.right = build_tree(T, child, key)
        return node
    root = build_tree(T, key, -1)
    def find_lca_helper(node, n1, n2):
        if node is None:
            return None
        if node.key == n1 or node.key == n2:
            return node
        left_lca = find_lca_helper(node.left, n1, n2)
        right_lca = find_lca_helper(node.right, n1, n2)
        if left_lca and right_lca:
            return node
        return left_lca if left_lca is not None else right_lca
    lca_node = find_lca_helper(root, n1, n2)
    return lca_node.key if lca_node else None
print("LCA(1, 4) =", findLCA([[0, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [1, 0, 0, 0, 1],
                                [0, 0, 0, 0, 0]], key=3, n1=1, n2=4))