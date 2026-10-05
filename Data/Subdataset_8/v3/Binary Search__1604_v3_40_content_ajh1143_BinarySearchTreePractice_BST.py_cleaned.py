class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return True
        else:
            if self.right_child:
                return self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return True
    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.left_child:
                return self.left_child.find(data)
            else:
                return False
        else:
            if self.right_child:
                return self.right_child.find(data)
            else:
                return False
    def preorder_traversal(self):
        if self:
            print(str(self.value))
            if self.left_child:
                self.left_child.preorder_traversal()
            if self.right_child:
                self.right_child.preorder_traversal()
    def inorder_traversal(self):
        if self:
            if self.left_child:
                self.left_child.inorder_traversal()
            print(str(self.value))
            if self.right_child:
                self.right_child.inorder_traversal()
    def postorder_traversal(self):
        if self:
            if self.left_child:
                self.left_child.postorder_traversal()
            if self.right_child:
                self.right_child.postorder_traversal()
            print(str(self.value))
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    def preorder_traversal(self):
        print("Preorder:")
        if self.root:
            self.root.preorder_traversal()
    def inorder_traversal(self):
        print("Inorder:")
        if self.root:
            self.root.inorder_traversal()
    def postorder_traversal(self):
        print("Postorder:")
        if self.root:
            self.root.postorder_traversal()
bst = BinaryTree()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.preorder_traversal()
bst.postorder_traversal()
bst.inorder_traversal()