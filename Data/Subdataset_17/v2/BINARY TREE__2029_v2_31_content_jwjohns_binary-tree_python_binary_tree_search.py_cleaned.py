import datetime
from random import randint
class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
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
        if self.value == data:
            return True
        elif self.value > data:
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
        print(str(self.value))
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(str(self.value))
    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(str(self.value))
        if self.rightChild:
            self.rightChild.inorder()
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
        print("PreOrder Traversal:")
        if self.root:
            self.root.preorder()
    def postorder(self):
        print("PostOrder Traversal:")
        if self.root:
            self.root.postorder()
    def inorder(self):
        print("InOrder Traversal:")
        if self.root:
            self.root.inorder()
def main():
    bst = Tree()
    n = 10000
    start = datetime.datetime.now()
    for _ in range(n):
        bst.insert(randint(0, 20000))
    finish = datetime.datetime.now()
    print("Insertion Time (microseconds):", (finish - start).microseconds)
    start = datetime.datetime.now()
    bst.inorder()
    finish = datetime.datetime.now()
    print("InOrder Traversal Time (microseconds):", (finish - start).microseconds % 1000)
if __name__ == "__main__":
    main()