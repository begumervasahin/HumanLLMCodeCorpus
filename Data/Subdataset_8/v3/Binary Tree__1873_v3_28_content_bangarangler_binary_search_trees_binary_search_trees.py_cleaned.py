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
        return self.right.get_max() if self.right else self.value
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
    for val in [3, 8, 2, 4, 7, 9]:
        bst.insert(val)
    print(bst.contains(4))
    print(bst.contains(6))
    print(bst.get_max())
    bst.for_each(print_node_value)
