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
        self._root = None
        self._count = 0
        self._removed = None
        self._order = "pre"
    def insert(self, key, value):
        self._root = self._insert(self._root, key, value)
        self._count += 1
    def _insert(self, node, key, value):
        if node is None:
            return BinarySearchTree.Node(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)
        return node
    def lookup(self, key):
        return self._lookup(self._root, key)
    def _lookup(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.value
        if key < node.key:
            return self._lookup(node.left, key)
        else:
            return self._lookup(node.right, key)
    def remove(self, key):
        self._removed = None
        self._root = self._remove(self._root, key)
        return self._removed
    def _remove(self, node, key):
        if node is None:
            return None
        if key == node.key:
            if node.left is None and node.right is None:
                self._removed = node.value
                self._count -= 1
                return None
            if node.right is None:
                self._removed = node.value
                self._count -= 1
                return node.left
            if node.left is None:
                self._removed = node.value
                self._count -= 1
                return node.right
            min_larger_node = self._minimum(node.right)
            saved_value = node.value
            node.key, node.value = min_larger_node.key, min_larger_node.value
            node.right = self._remove(node.right, min_larger_node.key)
            self._removed = saved_value
            return node
        if key < node.key:
            node.left = self._remove(node.left, key)
        else:
            node.right = self._remove(node.right, key)
        return node
    def _minimum(self, node):
        while node.left is not None:
            node = node.left
        return node
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
    def _traverse(self, node):
        if node is None:
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
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10, "Value for 10")
    bst.insert(5, "Value for 5")
    bst.insert(15, "Value for 15")
    bst.insert(3, "Value for 3")
    bst.insert(7, "Value for 7")
    print("Lookup 10:", bst.lookup(10))
    print("Lookup 5:", bst.lookup(5))
    print("Lookup 20:", bst.lookup(20))
    print("Remove 5:", bst.remove(5))
    print("Lookup 5:", bst.lookup(5))
    print("In-order traversal:")
    for value in bst.inorder():
        print(value)
    print("Pre-order traversal:")
    for value in bst.preorder():
        print(value)
    print("Post-order traversal:")
    for value in bst.postorder():
        print(value)
    print("Number of nodes:", len(bst))
