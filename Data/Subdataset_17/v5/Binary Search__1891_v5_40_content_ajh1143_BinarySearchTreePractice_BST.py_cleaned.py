class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, data):
        if data == self.value:
            return False
        elif data < self.value:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True
    def find(self, data):
        if data == self.value:
            return True
        elif data < self.value:
            return self.left.find(data) if self.left else False
        else:
            return self.right.find(data) if self.right else False
    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
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
        return self.root.find(data) if self.root else False
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