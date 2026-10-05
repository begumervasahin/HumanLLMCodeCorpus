
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b1):
        self.b2 = class1(b1)
        return self.b2
    def fonk3(self, b1):
        self.b3 = class1(b1)
        return self.b3
    def fonk4(self):
        b4 = []
        b4.append((self, -float('inf'), float('inf')))
        while len(b4) > 0:
            v, lbound, b5 = b4.pop()
            if v.b1 < lbound or v.b1 > b5:
                return False
            if v.b2:
                b4.append((v.b2, lbound, v.b1))
            if v.b3:
                b4.append((v.b3, v.b1, b5))
        return True
    def fonk5(self, node, lower, upper):
        if not node:
            return True
        if node.b1 <= lower or node.b1 >= upper:
            return False
        return self.fonk5(node.b2, lower, node.b1) and \
                self.fonk5(node.b3, node.b1, upper)
b6 = class1(5)
b6.fonk2(3)
b6.fonk3(7)
b6.b2.fonk2(1)
b6.b2.fonk3(9)
print(b6.fonk4())
print(b6.fonk5(b6, -float('inf'), float('inf')))