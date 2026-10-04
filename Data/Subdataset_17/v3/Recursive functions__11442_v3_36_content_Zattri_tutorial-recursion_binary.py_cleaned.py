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
        print("Left child:", self.left.value if self.left else None)
    def print_right(self):
        print("Right child:", self.right.value if self.right else None)
    def print_value(self):
        print("Value:", self.value)
    def print_parent(self):
        print("Parent:", self.parent.value if self.parent else None)
if __name__ == "__main__":
    root = Node(10)
    left_child = Node(5)
    right_child = Node(15)
    left_grandchild = Node(3)
    root.add_left(left_child)
    root.add_right(right_child)
    left_child.add_left(left_grandchild)
    root.print_value()
    root.print_left()
    root.print_right()
    left_child.print_value()
    left_child.print_parent()
    left_child.print_left()
    left_grandchild.print_value()
    left_grandchild.print_parent()
