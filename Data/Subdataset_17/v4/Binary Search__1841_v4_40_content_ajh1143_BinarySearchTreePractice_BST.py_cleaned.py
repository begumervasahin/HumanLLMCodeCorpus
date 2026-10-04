class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    def insert(self, data):
        if self.value == data:
            return False
        elif data < self.value:
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
        elif data < self.value:
            if self.left_child:
                return self.left_child.find(data)
            else:
                return False
        else:
            if self.right_child:
                return self.right_child.find(data)
            else:
                return False
    def preorder(self):
        print(self.value)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()
    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.value)
        if self.right_child:
            self.right_child.inorder()
    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.value)
class Tree:
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
    def preorder(self):
        print("Preorder traversal:")
        if self.root:
            self.root.preorder()
        else:
            print("Tree is empty.")
    def inorder(self):
        print("Inorder traversal:")
        if self.root:
            self.root.inorder()
        else:
            print("Tree is empty.")
    def postorder(self):
        print("Postorder traversal:")
        if self.root:
            self.root.postorder()
        else:
            print("Tree is empty.")
bst = Tree()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.preorder()
bst.postorder()
bst.inorder()