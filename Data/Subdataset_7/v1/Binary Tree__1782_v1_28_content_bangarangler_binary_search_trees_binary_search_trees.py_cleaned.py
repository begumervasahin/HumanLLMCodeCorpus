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
        elif b1 >= self.b1:
            if not self.b3:
                self.b3 = class1(b1)
            else:
                self.b3.fonk2(b1)
    def fonk3(self, b4):
        if b4 = = self.b1:
            return True
        elif b4 < self.b1:
            if self.b2:
                return self.b2.fonk3(b4)
            else:
                return False
        else:
            if self.b3:
                return self.b3.fonk3(b4)
            else:
                return False
    def fonk4(self):
        if self.b3:
            return self.b3.fonk4()
        else:
            return self.b1
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
    b6.fonk2(3)
    b6.fonk2(8)
    b6.fonk2(2)
    b6.fonk2(4)
    b6.fonk2(7)
    b6.fonk2(9)
    print(b6.fonk3(4))
    print(b6.fonk3(6))
    print(b6.fonk4())
    b6.fonk5(print_node_value)
