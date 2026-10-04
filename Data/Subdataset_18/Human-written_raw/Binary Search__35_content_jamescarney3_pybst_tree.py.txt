class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if not self.root:
            self.root = BinarySearchTreeNode(value)
        else:
            self.root.insert(value)
        return self.root
    def lookup(self, value):
        if not self.root:
            return None
        elif self.root.value == value:
            return self.root
        else:
            return self.root.lookup(value)
class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTreeNode(value)
                return self.left
            else:
                self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = BinarySearchTreeNode(value)
                return self.right
            else:
                self.right.insert(value)
        return None
    def lookup(self, value):
        if self.value == value:
            return self
        elif value < self.value and self.left:
            return self.left.lookup(value)
        elif value > self.value and self.right:
            return self.right.lookup(value)
        return None
