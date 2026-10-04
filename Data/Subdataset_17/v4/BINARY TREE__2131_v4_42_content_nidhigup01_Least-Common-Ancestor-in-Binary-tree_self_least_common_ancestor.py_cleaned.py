
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def find_lca(T, key, n1, n2):
    root = Node(key)
    if root is None or T is None or T == [[]]:
        return None
    num_columns = len(T[0])
    for child in range(num_columns):
        if T[key][child] == 1 and child < key:
            root.left = child
        elif T[key][child] == 1 and child > key:
            root.right = child
    if root.key == n1 or root.key == n2:
        return root
    left_lca = None
    right_lca = None
    if root.left is not None:
        left_lca = find_lca(T, root.left, n1, n2)
    if root.right is not None:
        right_lca = find_lca(T, root.right, n1, n2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca
def question4(T, r, n1, n2):
    lca_node = find_lca(T, r, n1, n2)
    return lca_node.key if lca_node else None
T = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]
r = 3
n1 = 1
n2 = 4
print("LCA({}, {}) = {}".format(n1, n2, question4(T, r, n1, n2)))