class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    def add_left_child(self, child_node):
        self.left = child_node
        child_node.parent = self
    def add_right_child(self, child_node):
        self.right = child_node
        child_node.parent = self
    def print_left_child(self):
        if self.left:
            print("Left Child:", self.left.value)
        else:
            print("No left child")
    def print_right_child(self):
        if self.right:
            print("Right Child:", self.right.value)
        else:
            print("No right child")
    def print_value(self):
        print("Node Value:", self.value)
    def print_parent(self):
        if self.parent:
            print("Parent Node:", self.parent.value)
        else:
            print("No parent node")