class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b1):
        if b1 < self.b1:
            if not self.b2:
                self.b2 = class1(b1)
            else:
                self.b2.fonk2(b1)
        else:
            if not self.b3:
                self.b3 = class1(b1)
            else:
                self.b3.fonk2(b1)
    def fonk3(self, b4):
        if b4 = = self.b1:
            return True
        elif b4 < self.b1 and self.b2:
            return self.b2.fonk3(b4)
        elif b4 > self.b1 and self.b3:
            return self.b3.fonk3(b4)
        else:
            return False
    def fonk4(self):
        return self.b3.fonk4() if self.b3 else self.b1
    def fonk5(self, cb):
        cb(self.b1)
        if self.b2:
            self.b2.fonk5(cb)
        if self.b3:
            self.b3.fonk5(cb)
def fonk6(b1):
    print(b1)
if b5 = = "__main__":
    b6 = class1(5)
    for val in [3, 8, 2, 4, 7, 9]:
        b6.fonk2(val)
    print(b6.fonk3(4))
    print(b6.fonk3(6))
    print(b6.fonk4())
    b6.fonk5(print_node_value)
