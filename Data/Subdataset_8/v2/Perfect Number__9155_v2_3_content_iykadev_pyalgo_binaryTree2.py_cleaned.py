class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None
    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_tree = BinaryTree(new_node)
            new_tree.left_child = self.left_child
            self.left_child = new_tree
    def insert_right(self, new_node):
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
    def set_root_val(self, obj):
        self.key = obj
    def get_root_val(self):
        return self.key
tree = BinaryTree('a')
print("Root value:", tree.get_root_val())
print("Left child:", tree.get_left_child())
tree.insert_left('b')
print("Left child after insertion:", tree.get_left_child())
print("Root value of left child:", tree.get_left_child().get_root_val())
tree.insert_right('c')
print("Right child:", tree.get_right_child())
print("Root value of right child:", tree.get_right_child().get_root_val())
tree.get_right_child().set_root_val('hello')
print("Updated root value of right child:", tree.get_right_child().get_root_val())