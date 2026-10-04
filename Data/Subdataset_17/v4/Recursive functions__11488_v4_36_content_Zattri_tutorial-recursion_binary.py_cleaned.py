class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.value = val
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
if __name__ == "__main__":
    root = Node(10)
    left_child = Node(5)
    right_child = Node(15)
    root.add_left(left_child)
    root.add_right(right_child)
    root.print_value()
    root.print_left()
    root.print_right()
    left_child.print_parent()
    right_child.print_parent()
