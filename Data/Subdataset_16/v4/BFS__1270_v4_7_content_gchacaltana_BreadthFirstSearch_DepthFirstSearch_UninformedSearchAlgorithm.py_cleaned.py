
b1 = "Gonzalo Chacaltana Buleje"
b2 = "gchacaltanab@gmail.com"
from Node import Node
class class1:
    def fonk1(self, b3, b4):
        self.b3 = b3
        self.b4 = b4
        self.fonk2()
    def fonk2(self):
        self.b5 = [self.b3[0]]
    def fonk3(self, node):
        pass
    def fonk4(self):
        return self.b5.pop(0)
    def fonk5(self):
        return len(self.b5)
    def fonk6(self, b6):
        for node in self.b3:
            if node.b6 = = b6:
                return node
        return None
    def fonk7(self):
        if self.fonk5() == 0:
            raise Exception("The b5 is empty")
    def fonk8(self, b7):
        if b7 = = self.b4:
            raise Exception(f"Target city found: {b7}")
    def fonk9(self):
        pass
    def fonk10(self, node):
        b8 = node.get_children()
        for child in b8:
            b9 = self.fonk6(child.b6)
            if isinstance(b9, Node):
                self.fonk3(b9)
if b10 = = "__main__":
    b11 = [...]
    b12 = "Arequipa"
    b13 = class1(b11, b12)
    try:
        b13.fonk9()
    except Exception as e:
        print(e)