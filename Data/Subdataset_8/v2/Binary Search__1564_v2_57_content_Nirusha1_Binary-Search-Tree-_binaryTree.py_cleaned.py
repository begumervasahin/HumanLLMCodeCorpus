class BinarySearchTree:
    def __init__(self):
        self._size = 0
        self._root = None
    class _BSTNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
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
        elif key < y.key:
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
    def largest(self):
        if self._root is not None:
            current = self._root
            while current.right is not None:
                current = current.right
            return current.key
    def search(self, key):
        found = []
        self._search(self._root, key, found)
        return len(found) > 0
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
    bst.add(50, 'Value 50')
    bst.add(30, 'Value 30')
    bst.add(70, 'Value 70')
    bst.add(20, 'Value 20')
    bst.add(40, 'Value 40')
    bst.add(60, 'Value 60')
    bst.add(80, 'Value 80')
    print("Smallest key:", bst.smallest())
    print("Largest key:", bst.largest())
    print("Search for key 30:", bst.search(30))
    print("Search for key 35:", bst.search(35))
    print("Is BST empty?", bst.is_empty())
    print("Size of BST:", bst.size())
    print("Inorder walk:", bst.inorder_walk())
    print("Preorder walk:", bst.preorder_walk())
    print("Postorder walk:", bst.postorder_walk())