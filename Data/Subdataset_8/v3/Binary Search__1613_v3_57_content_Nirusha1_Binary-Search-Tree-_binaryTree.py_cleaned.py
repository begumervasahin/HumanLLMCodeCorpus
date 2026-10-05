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
        node = self._BSTNode(key, value)
        if self._root is None:
            self._root = node
        else:
            parent = None
            current = self._root
            while current:
                parent = current
                if key < current.key:
                    current = current.left
                else:
                    current = current.right
            if key < parent.key:
                parent.left = node
            else:
                parent.right = node
        self._size += 1
    def smallest(self):
        current = self._root
        while current and current.left:
            current = current.left
        return current.key if current else None
    def largest(self):
        current = self._root
        while current and current.right:
            current = current.right
        return current.key if current else None
    def search(self, key):
        return self._search(self._root, key)
    def _search(self, node, key):
        if node is None or node.key == key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    def is_empty(self):
        return self._size == 0
    def size(self):
        return self._size
    def inorder_walk(self):
        nodes = []
        self._inorder_walk(self._root, nodes)
        return nodes
    def _inorder_walk(self, node, nodes):
        if node:
            self._inorder_walk(node.left, nodes)
            nodes.append(node.key)
            self._inorder_walk(node.right, nodes)
    def preorder_walk(self):
        nodes = []
        self._preorder_walk(self._root, nodes)
        return nodes
    def _preorder_walk(self, node, nodes):
        if node:
            nodes.append(node.key)
            self._preorder_walk(node.left, nodes)
            self._preorder_walk(node.right, nodes)
    def postorder_walk(self):
        nodes = []
        self._postorder_walk(self._root, nodes)
        return nodes
    def _postorder_walk(self, node, nodes):
        if node:
            self._postorder_walk(node.left, nodes)
            self._postorder_walk(node.right, nodes)
            nodes.append(node.key)
if __name__ == "__main__":
    bst = BinarySearchTree()
    keys_values = [(50, 'Value 50'), (30, 'Value 30'), (70, 'Value 70'), (20, 'Value 20'),
                   (40, 'Value 40'), (60, 'Value 60'), (80, 'Value 80')]
    for key, value in keys_values:
        bst.add(key, value)
    print("Smallest key:", bst.smallest())
    print("Largest key:", bst.largest())
    print("Search for key 30:", bst.search(30))
    print("Search for key 35:", bst.search(35))
    print("Is BST empty?", bst.is_empty())
    print("Size of BST:", bst.size())
    print("Inorder walk:", bst.inorder_walk())
    print("Preorder walk:", bst.preorder_walk())
    print("Postorder walk:", bst.postorder_walk())