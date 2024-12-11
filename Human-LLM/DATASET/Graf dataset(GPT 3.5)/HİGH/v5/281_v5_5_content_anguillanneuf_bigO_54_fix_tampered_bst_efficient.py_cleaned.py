class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b4 = None):
        if b4 is None:
            b4 = self
        if b4.b2:
            self.fonk2(b4.b2)
        print(b4.b1)
        if b4.b3:
            self.fonk2(b4.b3)
    def fonk3(self, b4 = None):
        if b4 is None:
            b4 = self
        if not b4:
            return
        self.fonk3(b4.b2)
        if not self.b5:
            if self.b7 and b4.b1 < self.b7.b1:
                self.b5 = self.b7
                self.b6 = b4
        else:
            if self.b6:
                if b4.b1 < self.b6.b1:
                    self.b6 = b4
        self.b7 = b4
        self.fonk3(b4.b3)
    def fonk4(self, b8 = None):
        if b8 is None:
            b8 = self
        self.fonk3(b8)
        if self.b5 and self.b6:
            self.b5.b1, self.b6.b1 = self.b6.b1, self.b5.b1
b9 = class1(7)
b9.b2 = class1(4)
b9.b2.b2 = class1(1)
b9.b2.b3 = class1(5)
b9.b3 = class1(11)
print("Original In-order Traversal:")
b9.fonk2()
b9.fonk4()
print("In-order Traversal after Swapping:")
b9.fonk2()