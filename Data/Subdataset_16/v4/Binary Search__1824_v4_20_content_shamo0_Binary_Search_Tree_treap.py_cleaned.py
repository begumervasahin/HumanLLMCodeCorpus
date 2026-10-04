import random
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = random.random()
    def fonk2(self):
        return str(self.b1)
class class2:
    def fonk3(self):
        self.b5 = None
        self.a1 = 0
    def fonk4(self, node):
        b6 = node.b3
        node.b3 = b6.b2
        b6.b2 = node
        return b6
    def fonk5(self, node):
        b6 = node.b2
        node.b2 = b6.b3
        b6.b3 = node
        return b6
    def fonk6(self, b7):
        self.a1 += 1
        if self.b5 is None:
            self.b5 = class1(b7)
        else:
            self.b5 = self.fonk7(b7, self.b5)
    def fonk7(self, b7, node):
        if node is None:
            return class1(b7)
        if b7 < node.b1:
            node.b2 = self.fonk7(b7, node.b2)
            if node.b2.b4 > node.b4:
                return self.fonk5(node)
        else:
            node.b3 = self.fonk7(b7, node.b3)
            if node.b3.b4 > node.b4:
                return self.fonk4(node)
        return node
    def fonk8(self, b7):
        return self.fonk9(self.b5, b7)
    def fonk9(self, node, b7):
        if node is None:
            return False
        if b7 = = node.b1:
            return True
        elif b7 < node.b1:
            return self.fonk9(node.b2, b7)
        else:
            return self.fonk9(node.b3, b7)
    def fonk10(self):
        return self.fonk11(self.b5)
    def fonk11(self, node):
        if node is None:
            return 0
        return 1 + max(self.fonk11(node.b2), self.fonk11(node.b3))
    def fonk12(self):
        return self.a1