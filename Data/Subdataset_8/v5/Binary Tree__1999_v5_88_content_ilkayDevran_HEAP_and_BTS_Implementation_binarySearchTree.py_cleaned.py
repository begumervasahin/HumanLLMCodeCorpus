class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def inorder_tree_walk(self, node):
        if node is not None:
            self.inorder_tree_walk(node.left)
            print(node.key, end=' ')
            self.inorder_tree_walk(node.right)
    def tree_search(self, key, node=None):
        if node is None:
            node = self.root
        while node is not None:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None
    def tree_minimum(self, node=None):
        if node is None:
            node = self.root
        while node.left is not None:
            node = node.left
        return node
    def tree_maximum(self, node=None):
        if node is None:
            node = self.root
        while node.right is not None:
            node = node.right
        return node
    def tree_successor(self, key):
        node = self.tree_search(key)
        if node is None:
            return None
        if node.right is not None:
            return self.tree_minimum(node.right)
        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent
        return parent
    def tree_predecessor(self, key):
        node = self.tree_search(key)
        if node is None:
            return None
        if node.left is not None:
            return self.tree_maximum(node.left)
        parent = node.parent
        while parent is not None and node == parent.left:
            node = parent
            parent = parent.parent
        return parent
    def tree_insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        current = self.root
        while current is not None:
            if key <= current.key:
                if current.left is None:
                    current.left = Node(key)
                    current.left.parent = current
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(key)
                    current.right.parent = current
                    return
                else:
                    current = current.right
    def tree_delete(self, key):
        node = self.tree_search(key)
        if node is None:
            return
        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
            elif node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left is not None and node.right is None:
            if node.parent is None:
                self.root = node.left
            elif node.parent.left == node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        elif node.left is None and node.right is not None:
            if node.parent is None:
                self.root = node.right
            elif node.parent.left == node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
        else:
            successor = self.tree_successor(key)
            node.key = successor.key
            if successor.parent.left == successor:
                successor.parent.left = None
            else:
                successor.parent.right = None
    def tree_max_path_length(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.tree_max_path_length(node.left), self.tree_max_path_length(node.right))
    def tree_min_path_length(self, node):
        if node is None:
            return 0
        else:
            return 1 + min(self.tree_min_path_length(node.left), self.tree_min_path_length(node.right))
    def tree_ratio_length(self):
        return self.tree_min_path_length(self.root) / self.tree_max_path_length(self.root)
def create_bst_and_test(lst):
    bst = BinarySearchTree()
    for key in lst:
        bst.tree_insert(key)
    print("\n---TREE INFO---\n")
    print("INORDER WALK: ", end='')
    bst.inorder_tree_walk(bst.root)
    print("\nSEARCH for", str(lst[0]), "-->", end=' ')
    print("Key EXISTS!" if bst.tree_search(lst[0]) is not None else "Key does NOT exist!")
    print("SEARCH for", str(lst[5]), "-->", end=' ')
    print("Key EXISTS!" if bst.tree_search(lst[5]) is not None else "Key does NOT exist!")
    print("SEARCH for", str(lst[0] * 2), "-->", end=' ')
    print("Key EXISTS!" if bst.tree_search(lst[0] * 2) is not None else "Key does NOT exist!")
    print("Minimum key in the Tree:", bst.tree_minimum().key)
    print("Maximum key in the Tree:", bst.tree_maximum().key)
    print("Successor of", str(lst[4]), "is", bst.tree_successor(lst[4]).key)
    print("Predecessor of", str(lst[4]), "is", bst.tree_predecessor(lst[4]).key)
    print("Delete root", str(lst[0]) + ":", end=' ')
    bst.tree_delete(lst[0])
    bst.inorder_tree_walk(bst.root)
    print("\nHeight of the Tree:", bst.tree_max_path_length(bst.root))
    print("Depth of the Tree:", bst.tree_min_path_length(bst.root))
    print("Ratio Depth/Height:", bst.tree_ratio_length(), "\n")
def generate_random_array(length, rng):
    from random import randint
    lst = [randint(0, length) for _ in range(rng)]
    return lst
def main():
    create_bst_and_test(generate_random_array(30, 100))
    create_bst_and_test(generate_random_array(50, 1000))
    create_bst_and_test(generate_random_array(100, 500))
if __name__ == '__main__':
    main()