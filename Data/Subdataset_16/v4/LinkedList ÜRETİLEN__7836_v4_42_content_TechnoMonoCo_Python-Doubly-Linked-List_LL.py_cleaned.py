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
                    b4 = self.b2
                    self.b1 = self.b2.b1
                    self.b2 = self.b2.b2
                    del b4
                return 0
            elif self.b2 is None:
                return -1
            else:
                return self.b2.fonk2(b1)
        else:
            if self.b2 is None:
                if self.b1 = = b1:
                    b4 = self
                    b5 = self.b3
                    b5.b2 = None
                    del b4
                    return 0
                else:
                    return -1
            else:
                if self.b1 = = b1:
                    b4 = self
                    b5 = self.b3
                    b5.b2 = self.b2
                    del b4
                    return 0
                else:
                    return self.b2.fonk2(b1)
    def fonk3(self, b1):
        if b1 < self.b1:
            b6 = class1(b1, self, self.b3)
            if self.b3:
                self.b3.b2 = b6
            self.b3 = b6
        elif self.b2 is None:
            b6 = class1(b1, None, self)
            self.b2 = b6
        else:
            self.b2.fonk3(b1)
    def fonk4(self, s):
        if self.b1 is not None:
            s += ", " + str(self.b1)
        if self.b2 is None:
            print(s)
        else:
            self.b2.fonk4(s)
    def fonk5(self):
        if self.b2 is None:
            if self.b1 is None:
                print("Empty.")
            else:
                print(self.b1)
        else:
            self.b2.fonk4(str(self.b1))
def fonk6():
    b7 = class1(0)
    print("contains:")
    b7.fonk5()
    print()
    print("inserting 1...")
    b7.fonk3(1)
    print("contains:")
    b7.fonk5()
    print()
    print("inserting 5...")
    b7.fonk3(5)
    print("contains:")
    b7.fonk5()
    print()
    print("removing 1...")
    b7.fonk2(1)
    print("contains:")
    b7.fonk5()
    print()
    print("removing 5...")
    b7.fonk2(5)
    print("contains:")
    b7.fonk5()
    print()
    print("removing 0...")
    b7.fonk2(0)
    print("contains:")
    b7.fonk5()
    print()
if b8 = = "__main__":
    fonk6()