
class Node_root:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def findLCA(T, key, n1, n2):
    root = Node_root(key)
    print ('root.key', root.key)
    if root is None or T == None or T == [[]]:
        return None
    num_rows = len(T)
    print ('num_rows', num_rows)
    num_columns = len(T[0])
    print ('num_columns', num_columns)
    parent = key
    print ('parent', parent)
    for child in range(0, num_columns):
        if T[parent][child] == 1 and  child <= parent:
            root.left = child
            print ('root.left', root.left )
        elif T[parent][child] == 0:
                pass
        elif T[parent][child] == 1 and  child > parent:
            root.right = child
            print ('root.right', root.right )
    if root.key == n1 or root.key == n2:
        return root
    left_lca = findLCA(T, root.left, n1, n2)
    right_lca = findLCA(T, root.right, n1, n2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca
print ("LCA(4,5) = ", findLCA([[0, 1, 0, 0, 0],[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]], key = 3, n1 = 1, n2 = 4))