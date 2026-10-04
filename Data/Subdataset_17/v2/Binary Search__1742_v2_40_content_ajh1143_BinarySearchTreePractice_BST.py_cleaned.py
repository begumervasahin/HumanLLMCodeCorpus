class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
    def insert(self, data):
        if data == self.value:
            return False
        elif data < self.value:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
    def find(self, data):
        if data == self.value:
            return True
        elif data < self.value:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
    def preorder(self):
        print(self.value)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.value)
        if self.rightChild:
            self.rightChild.inorder()
    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
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
        if self.root:
            print("Preorder traversal:")
            self.root.preorder()
    def inorder(self):
        if self.root:
            print("Inorder traversal:")
            self.root.inorder()
    def postorder(self):
        if self.root:
            print("Postorder traversal:")
            self.root.postorder()
if __name__ == "__main__":
    bst = Tree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.preorder()
    bst.inorder()
    bst.postorder()