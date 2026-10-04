class class1:
    def fonk1(self, b1 = None, b2=None, b3=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, b1):
        if self.b3 is None:
            if self.b1 = = b1:
                if self.b2 is None:
                    self.b1 = None
                else:
                    b2 = self.b2
                    self.b1 = b2.b1
                    self.b2 = b2.b2
                    if self.b2:
                        self.b2.b3 = self
                    del b2
                return 0
            elif self.b2 is None:
                return -1
            else:
                return self.b2.fonk2(b1)
        else:
            if self.b2 is None:
                if self.b1 = = b1:
                    b3 = self.b3
                    b3.b2 = None
                    del self
                    return 0
                else:
                    return -1
            else:
                if self.b1 = = b1:
                    b3 = self.b3
                    b2 = self.b2
                    b3.b2 = b2
                    b2.b3 = b3
                    del self
                    return 0
                else:
                    return self.b2.fonk2(b1)
    def fonk3(self, b1):
        if b1 < self.b1:
            b4 = class1(b1, self, self.b3)
            if self.b3:
                self.b3.b2 = b4
            self.b3 = b4
        elif self.b2 is None:
            b4 = class1(b1, None, self)
            self.b2 = b4
        else:
            self.b2.fonk3(b1)
    def fonk4(self, b5):
        if self.b1 is not None:
            b5.append(str(self.b1))
        if self.b2:
            self.b2.fonk4(b5)
    def fonk5(self):
        if self.b1 is None and self.b2 is None:
            print("Empty.")
        else:
            b5 = []
            self.fonk4(b5)
            print(", ".join(b5))
def fonk6():
    b6 = class1(0)
    print("contains:")
    b6.fonk5()
    print()
    print("inserting 1...")
    b6.fonk3(1)
    print("contains:")
    b6.fonk5()
    print()
    print("inserting 5...")
    b6.fonk3(5)
    print("contains:")
    b6.fonk5()
    print()
    print("removing 1...")
    b6.fonk2(1)
    print("contains:")
    b6.fonk5()
    print()
    print("removing 5...")
    b6.fonk2(5)
    print("contains:")
    b6.fonk5()
    print()
    print("removing 0...")
    b6.fonk2(0)
    print("contains:")
    b6.fonk5()
    print()
if b7 = = "__main__":
    fonk6()