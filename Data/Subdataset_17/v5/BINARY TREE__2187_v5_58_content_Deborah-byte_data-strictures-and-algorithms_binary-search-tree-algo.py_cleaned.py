class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    def find_value(self, value):
        if value < self.data:
            if self.left is None:
                return f"{value} Not Found"
            return self.left.find_value(value)
        elif value > self.data:
            if self.right is None:
                return f"{value} Not Found"
            return self.right.find_value(value)
        else:
            return f"{self.data} is found"
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=' ')
        if self.right:
            self.right.print_tree()
if __name__ == "__main__":
    root = Node(14)
    root.insert(6)
    root.insert(18)
    root.insert(3)
    print(root.find_value(7))
    print(root.find_value(14))
    root.print_tree()
