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
        print("Left child:", self.l.v if self.l else None)
    def printRight(self):
        print("Right child:", self.r.v if self.r else None)
    def printVal(self):
        print("Value:", self.v)
    def printParent(self):
        print("Parent:", self.p.v if self.p else None)
if __name__ == "__main__":
    root = Node(10)
    left_child = Node(5)
    right_child = Node(15)
    left_grandchild = Node(3)
    root.addLeft(left_child)
    root.addRight(right_child)
    left_child.addLeft(left_grandchild)
    root.printVal()
    root.printLeft()
    root.printRight()
    left_child.printVal()
    left_child.printParent()
    left_child.printLeft()
    left_grandchild.printVal()
    left_grandchild.printParent()
