class BinarySearchTree:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
    def __init__(self):
        self._root = None
        self._count = 0
        self._removed = None
        self._order = "pre"
    def insert(self, key, value):
        self._root = self._insert(self._root, key, value)
        self._count += 1
    def lookup(self, key):
        return self._lookup(self._root, key)
    def remove(self, key):
        self._removed = None
        self._root = self._remove(self._root, key)
        return self._removed
    def preorder(self):
        self._order = "pre"
        return self
    def inorder(self):
        self._order = "in"
        return self
    def postorder(self):
        self._order = "post"
        return self
    def __iter__(self):
        return self._traverse(self._root)
    def __len__(self):
        return self._count
    def _insert(self, node, key, value):
        if not node:
            return BinarySearchTree.Node(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)
        return node
    def _lookup(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.value
        if key < node.key:
            return self._lookup(node.left, key)
        else:
            return self._lookup(node.right, key)
    def _remove(self, node, key):
        if not node:
            return None
        if key == node.key:
            if not node.left and not node.right:
                self._removed = node.value
                self._count -= 1
                return None
            if not node.right:
                self._removed = node.value
                self._count -= 1
                return node.left
            if not node.left:
                self._removed = node.value
                self._count -= 1
                return node.right
            min_node = self._minimum(node.right)
            saved_value = node.value
            node.key = min_node.key
            node.value = min_node.value
            node.right = self._remove(node.right, min_node.key)
            self._removed = saved_value
            return node
        if key < node.key:
            node.left = self._remove(node.left, key)
        else:
            node.right = self._remove(node.right, key)
        return node
    def _traverse(self, node):
        if self._order == "pre":
            yield node.value
        if node.left:
            for element in self._traverse(node.left):
                yield element
        if self._order == "in":
            yield node.value
        if node.right:
            for element in self._traverse(node.right):
                yield element
        if self._order == "post":
            yield node.value
    def _minimum(self, node):
        while node.left:
            node = node.left
        return node