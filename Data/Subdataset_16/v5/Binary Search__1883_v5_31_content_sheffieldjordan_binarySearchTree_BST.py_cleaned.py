class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.a1 = 1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self, b4 = None):
        self.b4 = b4
    def fonk3(self, b1):
        return self.fonk9(self.b4, b1)
    def fonk4(self, b1):
        if self.b4 is None:
            self.b4 = class1(b1)
        else:
            self.fonk8(self.b4, b1)
    def fonk5(self):
        self.fonk12(self.b4)
    def fonk6(self):
        return self.fonk10(self.b4)
    def fonk7(self):
        return self.fonk11(self.b4)
    def fonk8(self, node, b1):
        if b1 = = node.b1:
            node.a1 += 1
        elif b1 < node.b1:
            if node.b2 is None:
                node.b2 = class1(b1)
            else:
                self.fonk8(node.b2, b1)
        else:
            if node.b3 is None:
                node.b3 = class1(b1)
            else:
                self.fonk8(node.b3, b1)
    def fonk9(self, node, b1):
        if node is None:
            return 0
        if b1 = = node.b1:
            return node.a1
        elif b1 < node.b1:
            return self.fonk9(node.b2, b1)
        else:
            return self.fonk9(node.b3, b1)
    def fonk10(self, node):
        if node is None:
            return 0
        return 1 + self.fonk10(node.b2) + self.fonk10(node.b3)
    def fonk11(self, node):
        if node is None:
            return 0
        b5 = self.fonk11(node.b2)
        b6 = self.fonk11(node.b3)
        return max(b5, b6) + 1
    def fonk12(self, node):
        if node is None:
            return
        self.fonk12(node.b2)
        print(f"{node.b1}: {node.a1}")
        self.fonk12(node.b3)
