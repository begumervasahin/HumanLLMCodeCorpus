class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b3 = b1
class class2:
    def fonk2(self, b2 = None):
        self.b4 = class1(b2) if b2 is not None else None
    def fonk3(self, b2):
        if self.b4 is None:
            return -1
        b5 = self.b4
        b6 = None
        while b5:
            if b5.b2 = = b2:
                if b6 is None:
                    self.b4 = b5.b3
                else:
                    b6.b3 = b5.b3
                return 0
            b6 = b5
            b5 = b5.b3
        return -1
    def fonk4(self, b2):
        b7 = class1(b2)
        if self.b4 is None:
            self.b4 = b7
        elif b2 < self.b4.b2:
            b7.b3 = self.b4
            self.b4 = b7
        else:
            b5 = self.b4
            while b5.b3 and b5.b3.b2 < b2:
                b5 = b5.b3
            b7.b3 = b5.b3
            b5.b3 = b7
    def fonk5(self):
        if self.b4 is None:
            print("Empty.")
        else:
            b5 = self.b4
            while b5:
                print(b5.b2, b8 = ", ")
                b5 = b5.b3
            print()
def fonk6():
    b9 = class2()
    print("contains...")
    b9.fonk5()
    print()
    print("inserting 1...")
    b9.fonk4(1)
    print("contains:")
    b9.fonk5()
    print()
    print("inserting 5...")
    b9.fonk4(5)
    print("contains:")
    b9.fonk5()
    print()
    print("removing 1...")
    b9.fonk3(1)
    print("contains:")
    b9.fonk5()
    print()
    print("removing 5...")
    b9.fonk3(5)
    print("contains...")
    b9.fonk5()
    print()
    print("removing 0...")
    b9.fonk3(0)
    print("contains:")
    b9.fonk5()
    print()
if b10 = = "__main__":
    fonk6()