class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
    def find_value(self, lookup_value):
        if self.data is None:
            return str(lookup_value) + " Not Found"
        elif lookup_value < self.data:
            if self.left is None:
                return str(lookup_value) + " Not Found"
            return self.left.find_value(lookup_value)
        elif lookup_value > self.data:
            if self.right is None:
                return str(lookup_value) + " Not Found"
            return self.right.find_value(lookup_value)
        else:
            return str(self.data) + " is found"
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
root = TreeNode(14)
root.insert(6)
root.insert(18)
root.insert(3)
print(root.find_value(7))
print(root.find_value(14))
root.print_tree()