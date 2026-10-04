class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b1):
        if b1 < self.b1:
            if self.b2 is None:
                self.b2 = class1(b1)
            else:
                self.b2.fonk2(b1)
        else:
            if self.b3 is None:
                self.b3 = class1(b1)
            else:
                self.b3.fonk2(b1)
    def fonk3(self, target):
        if self.b1 = = target:
            return True
        elif target < self.b1:
            return self.b2.fonk3(target) if self.b2 else False
        else:
            return self.b3.fonk3(target) if self.b3 else False
    def fonk4(self):
        return self.b1 if self.b3 is None else self.b3.fonk4()
    def fonk5(self, cb):
        cb(self.b1)
        if self.b2:
            self.b2.fonk5(cb)
        if self.b3:
            self.b3.fonk5(cb)
if b4 = = "__main__":
    b5 = class1(10)
    b5.fonk2(5)
    b5.fonk2(15)
    b5.fonk2(2)
    b5.fonk2(7)
    b5.fonk2(12)
    b5.fonk2(20)
    print("Tree contains 7:", b5.fonk3(7))
    print("Tree contains 9:", b5.fonk3(9))
    print("Max b1 in tree:", b5.fonk4())
    print("All values in tree:")
    b5.fonk5(print)
