class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTreeNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = BinarySearchTreeNode(value)
            else:
                self.right.insert(value)
    def lookup(self, value):
        if self.value == value:
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
        if not self.root:
            self.root = BinarySearchTreeNode(value)
        else:
            self.root.insert(value)
    def lookup(self, value):
        if not self.root:
            return None
        return self.root.lookup(value)
if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        bst.insert(value)
    print("In-order traversal:")
    def inorder_traversal(node):
        if not node:
            return
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)
    inorder_traversal(bst.root)
    print()
    print("Looking up values:")
    lookup_values = [3, 6, 9]
    for value in lookup_values:
        node = bst.lookup(value)
        if node:
            print(f"Value {value}: {node.value}")
        else:
            print(f"Value {value}: Not found")