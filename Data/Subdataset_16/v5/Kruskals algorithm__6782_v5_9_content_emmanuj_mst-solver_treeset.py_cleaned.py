from b2 import Node
class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, value):
        if value not in self.b1:
            self.b1[value] = Node(value)
    def fonk3(self, value):
        b2 = self.b1[value]
        if b2.b3 != b2:
            b2.b3 = self.b1[self.fonk3(b2.b3.value)]
        return b2.b3.value
    def fonk4(self, value_u, value_v):
        b4 = self.b1[self.fonk3(value_u)]
        b5 = self.b1[self.fonk3(value_v)]
        if b4 != b5:
            if b4.rank > b5.rank:
                b5.b3 = b4
            elif b4.rank < b5.rank:
                b4.b3 = b5
            else:
                b5.b3 = b4
                b4.rank += 1
    def fonk5(self):
        for value, b2 in self.b1.items():
            b6 = b2.b3.value if b2.b3 else None
            print(f"Node: {value}, Parent: {b6}, Rank: {b2.rank}")
