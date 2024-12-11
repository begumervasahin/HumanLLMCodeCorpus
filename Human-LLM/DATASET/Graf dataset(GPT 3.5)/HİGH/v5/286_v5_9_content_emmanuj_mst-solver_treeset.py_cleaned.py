from b2 import Node
class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, value):
        self.b1[value] = Node(value)
    def fonk3(self, value):
        b2 = self.b1[value]
        while b2.b3 != b2.b3.b3:
            b2.b3 = b2.b3.b3
            b2 = b2.b3
        return b2.b3.value
    def fonk4(self, u, v):
        b4 = self.b1[u]
        b5 = self.b1[v]
        if b4.rank > b5.rank:
            b5.b3 = b4
            return b4
        elif b4.rank < b5.rank:
            b4.b3 = b5
            return b5
        else:
            b4.b3 = b5
            b5.rank += 1
            return b5
    def fonk5(self):
        print(self.b1)