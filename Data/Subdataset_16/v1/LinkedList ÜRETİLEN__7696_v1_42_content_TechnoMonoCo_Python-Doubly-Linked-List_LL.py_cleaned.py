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
                    return 0
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
                    self.b3.b2 = None
                    return 0
                else:
                    return -1
            else:
                if self.b1 = = b1:
                    self.b3.b2 = self.b2
                    return 0
                else:
                    return self.b2.fonk2(b1)
    def fonk3(self, b1):
        if b1 < self.b1:
            b4 = class1(b1, self, None)
            if self.b3 is None:
                self.b1, b4.b1 = b4.b1, self.b1
                self.b2, b4.b2 = b4.b2, self.b2
                self.b3 = b4
            else:
                self.b3.b2 = b4
                self.b3 = b4
        elif self.b2 is None:
            self.b2 = class1(b1, None, self)
        else:
            self.b2.fonk3(b1)
    def fonk4(self, b5):
        if self.b1 is None:
            print(b5)
        else:
            b5 = b5 + ", " + str(self.b1)
            if self.b2 is None:
                print(b5)
            else:
                self.b2.fonk4(b5)
    def fonk5(self):
        if self.b1 is None:
            print("Empty.")
        elif self.b2 is None:
            print(self.b1)
        else:
            self.b2.fonk4(str(self.b1))
def fonk6():
    b6 = class1(0, None, None)
    print("contains...")
    b6.fonk5()
    print("\ninserting 1...")
    b6.fonk3(1)
    print("contains:")
    b6.fonk5()
    print("\ninserting 5...")
    b6.fonk3(5)
    print("contains:")
    b6.fonk5()
    print("\nremoving 1...")
    b6.fonk2(1)
    print("contains:")
    b6.fonk5()
    print("\nremoving 5...")
    b6.fonk2(5)
    print("contains...")
    b6.fonk5()
    print("\nremoving 0...")
    b6.fonk2(0)
    print("contains:")
    b6.fonk5()
if b7 = = "__main__":
    fonk6()