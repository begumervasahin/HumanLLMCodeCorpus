class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root is None:
            self.root = BinarySearchTreeNode(value)
        else:
            self.root.insert(value)
        return self.root
    def lookup(self, value):
        if self.root is None:
            return None
        return self.root.lookup(value)
class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTreeNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BinarySearchTreeNode(value)
            else:
                self.right.insert(value)
    def lookup(self, value):
        if self.value == value:
            return self
        elif value < self.value:
            return self.left.lookup(value) if self.left else None
        elif value > self.value:
            return self.right.lookup(value) if self.right else None
        return None
