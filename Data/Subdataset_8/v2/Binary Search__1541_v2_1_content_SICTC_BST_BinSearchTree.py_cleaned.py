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
    def make_empty(self):
        self._root = None
        self._count = 0
        self._removed = None
        self._order = "pre"
    def _insert(self, node, key, value):
        if not node:
            new_node = BinarySearchTree.Node(key, value)
            return new_node
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)
        return node
    def insert(self, key, value):
        self._root = self._insert(self._root, key, value)
        self._count += 1
    def _lookup(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.value
        if key < node.key:
            return self._lookup(node.left, key)
        else:
            return self._lookup(node.right, key)
    def lookup(self, key):
        return self._lookup(self._root, key)
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
            minimum_node = self._minimum(node.right)
            saved = node.value
            node.key = minimum_node.key
            node.value = minimum_node.value
            node.right = self._remove(node.right, minimum_node.key)
            self._removed = saved
            return node
        if key < node.key:
            node.left = self._remove(node.left, key)
        else:
            node.right = self._remove(node.right, key)
        return node
    def remove(self, key):
        self._removed = None
        self._root = self._remove(self._root, key)
        return self._removed
    def _minimum(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    def preorder(self):
        self._order = "pre"
    def inorder(self):
        self._order = "in"
    def postorder(self):
        self._order = "post"
    def __iter__(self):
        return self._traverse(self._root)
    def _traverse(self, node):
        if not node:
            return
        if self._order == "pre":
            yield node.value
        if node.left:
            yield from self._traverse(node.left)
        if self._order == "in":
            yield node.value
        if node.right:
            yield from self._traverse(node.right)
        if self._order == "post":
            yield node.value
    def __len__(self):
        return self._count
bst = BinarySearchTree()
bst.insert(5, 'five')
bst.insert(3, 'three')
bst.insert(7, 'seven')
print("Inorder traversal:")
bst.inorder()
for value in bst:
    print(value)