class BinarySearchTree:
    class _BSTNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
    def __init__(self):
        self._size = 0
        self._root = None
    def add(self, key, value):
        z = self._BSTNode(key, value)
        y = None
        x = self._root
        while x is not None:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        if y is None:
            self._root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self._size += 1
    def smallest(self):
        if self._root is not None:
            current = self._root
            while current.left is not None:
                current = current.left
            return current.key
        return None
    def largest(self):
        if self._root is not None:
            current = self._root
            while current.right is not None:
                current = current.right
            return current.key
        return None
    def search(self, key):
        found = []
        self._search(self._root, key, found)
        return bool(found)
    def _search(self, subtree, key, found):
        if subtree:
            if key == subtree.key:
                found.append(1)
            elif key < subtree.key:
                self._search(subtree.left, key, found)
            elif key > subtree.key:
                self._search(subtree.right, key, found)
    def is_empty(self):
        return self._size == 0
    def size(self):
        return self._size
    def inorder_walk(self):
        nodes = []
        self._inorder_walk(self._root, nodes)
        return nodes
    def _inorder_walk(self, subtree, nodes):
        if subtree:
            self._inorder_walk(subtree.left, nodes)
            nodes.append(subtree.key)
            self._inorder_walk(subtree.right, nodes)
    def preorder_walk(self):
        nodes = []
        self._preorder_walk(self._root, nodes)
        return nodes
    def _preorder_walk(self, subtree, nodes):
        if subtree:
            nodes.append(subtree.key)
            self._preorder_walk(subtree.left, nodes)
            self._preorder_walk(subtree.right, nodes)
    def postorder_walk(self):
        nodes = []
        self._postorder_walk(self._root, nodes)
        return nodes
    def _postorder_walk(self, subtree, nodes):
        if subtree:
            self._postorder_walk(subtree.left, nodes)
            self._postorder_walk(subtree.right, nodes)
            nodes.append(subtree.key)
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(10, "Ten")
    bst.add(20, "Twenty")
    bst.add(5, "Five")
    bst.add(7, "Seven")
    bst.add(30, "Thirty")
    print("Smallest key:", bst.smallest())
    print("Largest key:", bst.largest())
    print("Search for key 20:", bst.search(20))
    print("Search for key 15:", bst.search(15))
    print("Inorder traversal:", bst.inorder_walk())
    print("Preorder traversal:", bst.preorder_walk())
    print("Postorder traversal:", bst.postorder_walk())
    print("Is the BST empty?", bst.is_empty())
    print("Size of the BST:", bst.size())