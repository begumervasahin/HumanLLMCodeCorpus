class BinaryTree:
    def __init__(self, root_value):
        self.key = root_value
        self.left_child = None
        self.right_child = None
    def insert_left_child(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_tree = BinaryTree(new_node)
            new_tree.left_child = self.left_child
            self.left_child = new_tree
    def insert_right_child(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            new_tree = BinaryTree(new_node)
            new_tree.right_child = self.right_child
            self.right_child = new_tree
    def get_right_child(self):
        return self.right_child
    def get_left_child(self):
        return self.left_child
    def set_root_value(self, obj):
        self.key = obj
    def get_root_value(self):
        return self.key
r = BinaryTree('a')
print(r.get_root_value())
print(r.get_left_child())
r.insert_left_child('b')
print(r.get_left_child())
print(r.get_left_child().get_root_value())
r.insert_right_child('c')
print(r.get_right_child())
print(r.get_right_child().get_root_value())
r.get_right_child().set_root_value('hello')
print(r.get_right_child().get_root_value())