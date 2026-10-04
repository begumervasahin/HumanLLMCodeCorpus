import datetime
from random import randint
class Node:
    def __init__(self, val):
        self.value = val
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
            return self.left_child.find(data) if self.left_child else False
        else:
            return self.right_child.find(data) if self.right_child else False
    def preorder(self):
        if self:
            print(self.value)
            if self.left_child:
                self.left_child.preorder()
            if self.right_child:
                self.right_child.preorder()
    def postorder(self):
        if self:
            if self.left_child:
                self.left_child.postorder()
            if self.right_child:
                self.right_child.postorder()
            print(self.value)
    def inorder(self):
        if self:
            if self.left_child:
                self.left_child.inorder()
            print(self.value)
            if self.right_child:
                self.right_child.inorder()
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
        print("PreOrder Traversal:")
        if self.root:
            self.root.preorder()
        else:
            print("Tree is empty")
    def postorder(self):
        print("PostOrder Traversal:")
        if self.root:
            self.root.postorder()
        else:
            print("Tree is empty")
    def inorder(self):
        print("InOrder Traversal:")
        if self.root:
            self.root.inorder()
        else:
            print("Tree is empty")
def main():
    bst = Tree()
    n = 10000
    start = datetime.datetime.now()
    for _ in range(n):
        bst.insert(randint(0, 20000))
    finish = datetime.datetime.now()
    print(f"Time to insert {n} nodes: {(finish - start).total_seconds()} seconds")
    start = datetime.datetime.now()
    bst.inorder()
    finish = datetime.datetime.now()
    print(f"Time to traverse in-order: {(finish - start).total_seconds()} seconds")
if __name__ == "__main__":
    main()