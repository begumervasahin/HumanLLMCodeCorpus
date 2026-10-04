class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
    def insert(self, val):
        if self.value == val:
            return False
        elif val < self.value:
            if self.left:
                return self.left.insert(val)
            else:
                self.left = Node(val)
                return True
        else:
            if self.right:
                return self.right.insert(val)
            else:
                self.right = Node(val)
                return True
    def find(self, val):
        if self.value == val:
            return True
        elif val > self.value:
            return self.right.find(val) if self.right else False
        else:
            return self.left.find(val) if self.left else False
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
    def delete(self, val):
        if self.value == val:
            if self.left and self.right:
                successor = self.right.find_successor()
                self.value = successor.value
                self.right = self.right.delete(successor.value)
            elif self.left:
                return self.left
            elif self.right:
                return self.right
            else:
                return None
        elif val > self.value:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left:
                self.left = self.left.delete(val)
        return self
    def find_successor(self):
        if self.left:
            return self.left.find_successor()
        return self