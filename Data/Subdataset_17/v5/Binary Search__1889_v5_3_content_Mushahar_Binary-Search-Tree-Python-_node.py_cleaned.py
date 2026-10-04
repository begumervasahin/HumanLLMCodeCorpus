class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
    def insert(self, val):
        if val == self.value:
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
        if val == self.value:
            return True
        elif val < self.value:
            return self.left.find(val) if self.left else False
        else:
            return self.right.find(val) if self.right else False
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
        if val == self.value:
            if self.left and self.right:
                successor = self.right.find_min()
                self.value = successor.value
                self.right = self.right.delete(successor.value)
            else:
                return self.left if self.left else self.right
        elif val < self.value:
            if self.left:
                self.left = self.left.delete(val)
        else:
            if self.right:
                self.right = self.right.delete(val)
        return self
    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self