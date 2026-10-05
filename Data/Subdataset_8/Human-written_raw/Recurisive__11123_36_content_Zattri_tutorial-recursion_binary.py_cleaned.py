class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.p = None
        self.v = val
    def addLeft(self, childNode):
        self.l = childNode
        childNode.p = self
    def addRight(self, childNode):
        self.r = childNode
        childNode.p = self
    def printLeft(self):
        print(self.l)
    def printRight(self):
        print(self.r)
    def printVal(self):
        print(self.v)
    def printParent(self):
        print(self.p)