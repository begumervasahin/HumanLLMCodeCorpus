class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._size = 0
    class _Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
    def add(self, key, value):
        new_node = self._Node(key, value)
        if self._root is None:
            self._root = new_node
        else:
            current = self._root
            while True:
                if key < current.key:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right
        self._size += 1
    def smallest(self):
        if self._root is None:
            return None
        current = self._root
        while current.left is not None:
            current = current.left
        return current.key
    def largest(self):
        if self._root is None:
            return None
        current = self._root
        while current.right is not None:
            current = current.right
        return current.key
    def search(self, key):
        found = []
        current = self._root
        while current is not None:
            if key == current.key:
                found.append(current.value)
            current = current.left if key < current.key else current.right
        return found
    def is_empty(self):
        return self._size == 0
    def size(self):
        return self._size
    def inorder_walk(self):
        nodes = []
        self._inorder_walk(self._root, nodes)
        return nodes
    def _inorder_walk(self, node, nodes):
        if node is not None:
            self._inorder_walk(node.left, nodes)
            nodes.append(node.key)
            self._inorder_walk(node.right, nodes)
    def preorder_walk(self):
        nodes = []
        self._preorder_walk(self._root, nodes)
        return nodes
    def _preorder_walk(self, node, nodes):
        if node is not None:
            nodes.append(node.key)
            self._preorder_walk(node.left, nodes)
            self._preorder_walk(node.right, nodes)
    def postorder_walk(self):
        nodes = []
        self._postorder_walk(self._root, nodes)
        return nodes
    def _postorder_walk(self, node, nodes):
        if node is not None:
            self._postorder_walk(node.left, nodes)
            self._postorder_walk(node.right, nodes)
            nodes.append(node.key)