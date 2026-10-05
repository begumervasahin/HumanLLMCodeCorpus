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
        if self.l:
            print(self.l.v)
        else:
            print("No left child")
    def printRight(self):
        if self.r:
            print(self.r.v)
        else:
            print("No right child")
    def printVal(self):
        print(self.v)
    def printParent(self):
        if self.p:
            print(self.p.v)
        else:
            print("No parent")