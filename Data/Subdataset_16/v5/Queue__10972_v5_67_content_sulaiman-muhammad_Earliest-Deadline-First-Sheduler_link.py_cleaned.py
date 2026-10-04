class class1:
    def fonk1(self, b1 = None, b2=None):
        self.b1 = b1
        self.b2 = b2
class class2:
    def fonk2(self):
        self.b3 = None
        self.b4 = None
    def fonk3(self, x, pos):
        b5 = class1(x)
        b5.b2 = pos.b2
        pos.b2 = b5
    def fonk4(self, x):
        b5 = class1(x)
        if self.b3 is None:
            self.b3 = b5
            self.b4 = b5
        else:
            self.b4.b2 = b5
            self.b4 = b5
    def fonk5(self, x):
        b6 = self.b3
        while b6 is not None and b6.b1 != x:
            b6 = b6.b2
        return b6
    def fonk6(self):
        b6 = self.b3
        while b6:
            print(b6.b1)
            b6 = b6.b2
    def fonk7(self, node):
        if self.b3 is None:
            self.b3 = node
            self.b4 = node
        elif self.b3.b1.cpu > node.b1.cpu:
            node.b2 = self.b3
            self.b3 = node
        else:
            b6 = self.b3
            while b6.b2 is not None and b6.b2.b1.cpu < node.b1.cpu:
                b6 = b6.b2
            node.b2 = b6.b2
            b6.b2 = node
            if node.b2 is None:
                self.b4 = node
    def fonk8(self):
        b7 = None
        b6 = self.b3
        while b6:
            b2 = b6.b2
            b6.b2 = b7
            b7 = b6
            b6 = b2
        self.b3 = b7
        self.fonk6()
    def fonk9(self, x):
        b5 = class1(x)
        if self.b3 is None:
            self.b3 = b5
            self.b4 = b5
        else:
            b5.b2 = self.b3
            self.b3 = b5
    def fonk10(self):
        if self.b3 is None:
            print("empty")
            return None
        b8 = self.b3
        self.b3 = self.b3.b2
        if self.b3 is None:
            self.b4 = None
        b8.b2 = None
        return b8
def fonk11():
    b9 = class2()
    b9.fonk9(1)
    b9.fonk7(class1({'cpu': 3}))
    b9.fonk6()
    print("b4", b9.b4.b1)
    b9.fonk10()
    b9.fonk10()
    b9.fonk10()
    b9.fonk10()
if b10 = = "__main__":
    fonk11()