import sys
from Node import Node
class class1(object):
    def fonk1(self, b1):
        self.b1 = b1[:]
    def fonk2(self):
        return len(self.b1)
    def fonk3(self, b2):
        return any(node.b2 = = b2 for node in self.b1)
    def fonk4(self):
        b3 = sys.maxint
        b4 = None
        for node in self.b1:
            if node.b2 < b3:
                b3 = node.b2
                b4 = node
        self.b1.remove(b4)
        return b4.idx
