class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value
    def add_left(self, child_node):
        self.left = child_node
        child_node.parent = self
    def add_right(self, child_node):
        self.right = child_node
        child_node.parent = self
    def print_left(self):
        print(self.left)
    def print_right(self):
        print(self.right)
    def print_value(self):
        print(self.value)
    def print_parent(self):
        print(self.parent)