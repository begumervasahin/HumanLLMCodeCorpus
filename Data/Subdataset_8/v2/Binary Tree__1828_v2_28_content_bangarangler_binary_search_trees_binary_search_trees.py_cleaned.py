class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)
        else:
            return False
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
def print_node_value(value):
    print(value)
if __name__ == "__main__":
    bst = BinarySearchTree(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(9)
    print(bst.contains(4))
    print(bst.contains(6))
    print(bst.get_max())
    bst.for_each(print_node_value)
