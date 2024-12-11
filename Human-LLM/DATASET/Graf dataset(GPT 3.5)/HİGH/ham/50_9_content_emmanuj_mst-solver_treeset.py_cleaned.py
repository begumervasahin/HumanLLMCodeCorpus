'''
Emmanuel John (emmanuj)
class1 to represent a set of d-heaps
'''
from node import Node
class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, b4):
        self.b1[b4] = Node(b4)
    def fonk3(self, b4):
        b2 = self.b1[b4].b3.b3
        while(b2 != self.b1[b4].b3):
            self.b1[b4].b3 = b2
            b4 = b2.value
            b2 = self.b1[b4].b3.b3
        return b2.value
    def fonk4(self, u, v):
        b5 = None
        if self.b1[u].b6 > self.b1[v].b6:
            self.b1[v].b3 = self.b1[u]
            b5 = self.b1[u]
        elif self.b1[u].b6 < self.b1[v].b6:
            self.b1[u].b3 = self.b1[v]
            b5 = self.b1[v]
        else:
            self.b1[u].b3 = self.b1[v]
            self.b1[v].b6 = self.b1[v].b6 + 1
            b5 = self.b1[v]
        return b5
    def fonk5(self):
        print self.b1