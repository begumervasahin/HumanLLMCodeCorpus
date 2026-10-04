class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            return self.left.contains(target) if self.left else False
        else:
            return self.right.contains(target) if self.right else False
    def get_max(self):
        return self.value if self.right is None else self.right.get_max()
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
if __name__ == "__main__":
    bst = BinarySearchTree(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)
    print("Tree contains 7:", bst.contains(7))
    print("Tree contains 9:", bst.contains(9))
    print("Max value in tree:", bst.get_max())
    print("All values in tree:")
    bst.for_each(print)
