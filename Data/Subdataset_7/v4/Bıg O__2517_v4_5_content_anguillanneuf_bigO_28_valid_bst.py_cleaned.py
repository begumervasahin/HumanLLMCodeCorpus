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
            node, lower_bound, b5 = b4.pop()
            if not lower_bound < node.b1 < b5:
                return False
            if node.b2:
                b4.append((node.b2, lower_bound, node.b1))
            if node.b3:
                b4.append((node.b3, node.b1, b5))
        return True
    def fonk5(self, node, lower, upper):
        if not node:
            return True
        if not lower < node.b1 < upper:
            return False
        return (
            self.fonk5(node.b2, lower, node.b1)
            and self.fonk5(node.b3, node.b1, upper)
        )
b6 = class1(5)
b6.fonk2(3)
b6.fonk3(7)
b6.b2.fonk2(1)
b6.b2.fonk3(4)
print("Iterative approach:", b6.fonk4())
print("Recursive approach:", b6.fonk5(b6, float('-inf'), float('inf')))