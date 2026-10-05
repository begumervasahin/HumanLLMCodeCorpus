class AVLTreeNode:
    def __init__(self, key_data):
        self.key_data = key_data
        self.count = 1
        self.depth = 0
        self.height = 0
        self.order = -1
        self.parent = None
        self.left = None
        self.right = None
    def is_left_child(self):
        return (self.parent is not None) and (self.parent.left == self)
    def is_right_child(self):
        return (self.parent is not None) and (self.parent.right == self)
    def is_leaf(self):
        return (self.left is None) and (self.right is None)
    def is_root(self):
        return self.parent is None
class AVLTree:
    def __init__(self):
        self.root_node = None
        self.num_nodes = 0
        self.current_node = None
    def find(self, key_data):
    def insert(self, key_data):
    def remove(self, key_data):
    def print_tree(self):
    def get_first(self):
    def mark_order(self):
