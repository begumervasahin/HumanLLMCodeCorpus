class BinarySearchTree:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
    def __init__(self):
        self.make_empty()
    def make_empty(self):
        self.root = None
        self.count = 0
        self.removed = None
        self.order = "pre"
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
        self.count += 1
    def _insert(self, node, key, value):
        if node is None:
            return BinarySearchTree.Node(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)
        return node
    def lookup(self, key):
        return self._lookup(self.root, key)
    def _lookup(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._lookup(node.left, key)
        else:
            return self._lookup(node.right, key)
    def remove(self, key):
        self.removed = None
        self.root = self._remove(self.root, key)
        return self.removed
    def _remove(self, node, key):
        if node is None:
            return None
        if key == node.key:
            if node.left is None and node.right is None:
                self.removed = node.value
                self.count -= 1
                return None
            if node.left is None:
                self.removed = node.value
                self.count -= 1
                return node.right
            if node.right is None:
                self.removed = node.value
                self.count -= 1
                return node.left
            min_node = self._minimum(node.right)
            saved_value = node.value
            node.key = min_node.key
            node.value = min_node.value
            node.right = self._remove(node.right, min_node.key)
            self.removed = saved_value
            return node
        elif key < node.key:
            node.left = self._remove(node.left, key)
        else:
            node.right = self._remove(node.right, key)
        return node
    def _minimum(self, node):
        while node.left is not None:
            node = node.left
        return node
    def preorder(self):
        self.order = "pre"
        return self
    def inorder(self):
        self.order = "in"
        return self
    def postorder(self):
        self.order = "post"
        return self
    def __iter__(self):
        return self._traverse(self.root)
    def _traverse(self, node):
        if node is None:
            return
        if self.order == "pre":
            yield node.value
        if node.left:
            yield from self._traverse(node.left)
        if self.order == "in":
            yield node.value
        if node.right:
            yield from self._traverse(node.right)
        if self.order == "post":
            yield node.value
    def __len__(self):
        return self.count