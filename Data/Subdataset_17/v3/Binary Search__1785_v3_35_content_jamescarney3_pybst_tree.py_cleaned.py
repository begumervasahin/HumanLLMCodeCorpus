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
        if value == self.value:
            return self
        elif value < self.value and self.left:
            return self.left.lookup(value)
        elif value > self.value and self.right:
            return self.right.lookup(value)
        return None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root is None:
            self.root = BinarySearchTreeNode(value)
        else:
            self.root.insert(value)
    def lookup(self, value):
        if self.root is None:
            return None
        return self.root.lookup(value)
bst = BinarySearchTree()
values_to_insert = [10, 5, 15, 3, 7, 12, 18]
for value in values_to_insert:
    bst.insert(value)
lookup_values = [7, 6]
for value in lookup_values:
    node = bst.lookup(value)
    if node:
        print(f"Node with value {node.value} found in the tree.")
    else:
        print(f"Value {value} not found in the tree.")