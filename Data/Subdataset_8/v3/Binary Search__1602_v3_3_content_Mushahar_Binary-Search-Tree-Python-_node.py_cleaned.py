class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        if value == self.value:
            return False
        elif value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = Node(value)
                return True
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = Node(value)
                return True
    def find(self, value):
        if value == self.value:
            return True
        elif value < self.value and self.left:
            return self.left.find(value)
        elif value > self.value and self.right:
            return self.right.find(value)
        else:
            return False
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
    def delete(self, value):
        if value == self.value:
            if self.left and self.right:
                successor = self.right.find_successor()
                self.value = successor.value
                self.right = self.right.delete(self.value)
                return self
            elif self.left:
                return self.left
            elif self.right:
                return self.right
            else:
                return None
        elif value < self.value and self.left:
            self.left = self.left.delete(value)
            return self
        elif value > self.value and self.right:
            self.right = self.right.delete(value)
            return self
        else:
            return self
    def find_successor(self):
        if self.left:
            return self.left.find_successor()
        else:
            return self
if __name__ == "__main__":
    root = Node(5)
    root.insert(3)
    root.insert(8)
    root.insert(1)
    root.insert(4)
    root.insert(7)
    root.insert(9)
    print("Preorder traversal:")
    root.preorder()
    print("Inorder traversal:")
    root.inorder()
    print("Postorder traversal:")
    root.postorder()
    print("Finding elements:")
    print(root.find(4))
    print(root.find(10))
    print("Deleting elements:")
    root.delete(1)
    root.delete(8)
    print("Inorder traversal after deletion:")
    root.inorder()