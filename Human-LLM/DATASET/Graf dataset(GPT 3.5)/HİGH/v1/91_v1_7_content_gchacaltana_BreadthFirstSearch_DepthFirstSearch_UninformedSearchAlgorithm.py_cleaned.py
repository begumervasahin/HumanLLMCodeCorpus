from Node import Node
class class1(object):
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.fonk2()
    def fonk2(self):
        self.b3 = []
        self.b3.append(self.b1[0])
    def fonk3(self, node):
        pass
    def fonk4(self):
        return self.b3.pop(0)
    def fonk5(self):
        return len(self.b3)
    def fonk6(self, b4):
        for node in self.b1:
            if node.b4 = = b4:
                return node
    def fonk7(self):
        if self.fonk5() == 0:
            raise Exception("La cola esta vacia")
    def fonk8(self, b5):
        if b5 = = self.b2:
            raise Exception("Ciudad encontrada: %s" % b5)
    def fonk9(self):
        pass
    def fonk10(self, node):
        b6 = node.getChildrenNodes()
        for child in b6:
            b7 = self.fonk6(child.b4)
            if (isinstance(b7, Node)):
                self.fonk3(b7)
b8 = Node("b8")
b9 = Node("b9")
b10 = Node("b10")
b11 = Node("b11")
b12 = Node("b12")
b13 = Node("b13")
b14 = Node("b14")
b15 = Node("b15")
b16 = Node("b16")
b17 = Node("b17")
b8.addChild(b9)
b8.addChild(b10)
b8.addChild(b11)
b9.addChild(b12)
b9.addChild(b13)
b10.addChild(b13)
b11.addChild(b13)
b11.addChild(b16)
b12.addChild(b14)
b13.addChild(b17)
b13.addChild(b15)
b14.addChild(b17)
b15.addChild(b17)
b16.addChild(b17)
b18 = class1([b8, b9, b10, b11, b12, b13, b14, b15, b16, b17], "b17")
try:
    b18.fonk9()
except Exception as e:
    print(e)