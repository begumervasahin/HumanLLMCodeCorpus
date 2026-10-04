from typing import List
class class1:
    def fonk1(self, b3: str, b4: b1 = 0, b5: b1 = 0, b2: List['class1'] = None):
        if b2 is None:
            b2 = []
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b2 = b2
    def fonk2(self, other):
        return isinstance(other, class1) and self.b3 = = other.b3
    def fonk3(self):
        b6 = '['
        if self.b2:
            b6 += ','.join(node.b3 for node in self.b2)
        b6 += ']'
        return b6
if b7 = = "__main__":
    b8 = class1('A')
    b9 = class1('B')
    b10 = class1('C')
    b11 = class1('D', b2=[b8, b9])
    b12 = class1('E', b2=[b9, b10])
    print(f"class1 D destination nodes: {b11.fonk3()}")
    print(f"class1 E destination nodes: {b12.fonk3()}")
    print(f"class1 A equals class1 B: {b8 = = b9}")
    print(f"class1 A equals class1 A: {b8 = = b8}")