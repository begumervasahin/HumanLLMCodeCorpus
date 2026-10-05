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
        b4.append((self, float('-inf'), float('inf')))
        while b4:
            b6, lower, b5 = b4.pop()
            if not lower < b6.b1 < b5:
                return False
            if b6.b2:
                b4.append((b6.b2, lower, b6.b1))
            if b6.b3:
                b4.append((b6.b3, b6.b1, b5))
        return True
    def fonk5(self, b6 = None, lower=float('-inf'), b5=float('inf')):
        if b6 is None:
            b6 = self
        if not b6:
            return True
        if not lower < b6.b1 < b5:
            return False
        return self.fonk5(b6.b2, lower, b6.b1) and \
               self.fonk5(b6.b3, b6.b1, b5)
b7 = class1(5)
b7.fonk2(3)
b7.fonk3(7)
b7.b2.fonk2(1)
b7.b2.fonk3(4)
print("Iterative Check:", b7.fonk4())
print("Recursive Check:", b7.fonk5())
