class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def setRootVal(self, obj):
        self.key = obj
    def getRootVal(self):
        return self.key
r = BinaryTree('a')
print("Root value:", r.getRootVal())
print("Left child:", r.getLeftChild())
r.insertLeft('b')
print("Left child after insertion:", r.getLeftChild())
print("Root value of left child:", r.getLeftChild().getRootVal())
r.insertRight('c')
print("Right child:", r.getRightChild())
print("Root value of right child:", r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print("Updated root value of right child:", r.getRightChild().getRootVal())