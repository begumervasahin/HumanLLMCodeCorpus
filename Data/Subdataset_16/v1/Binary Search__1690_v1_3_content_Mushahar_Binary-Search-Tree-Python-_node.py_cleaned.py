class class1:
    def fonk1(self, val):
        self.b1 = val
        self.b2 = None
        self.b3 = None
    def fonk2(self, val):
        if self.b1 = = val:
            return False
        elif val < self.b1:
            if self.b2:
                return self.b2.fonk2(val)
            else:
                self.b2 = class1(val)
                return True
        else:
            if self.b3:
                return self.b3.fonk2(val)
            else:
                self.b3 = class1(val)
                return True
    def fonk3(self, val):
        if self.b1 = = val:
            return True
        elif val > self.b1:
            if self.b3:
                return self.b3.fonk3(val)
            else:
                return False
        else:
            if self.b2:
                return self.b2.fonk3(val)
            else:
                return False
    def fonk4(self):
        print(self.b1)
        if self.b2:
            self.b2.fonk4()
        if self.b3:
            self.b3.fonk4()
    def fonk5(self):
        if self.b2:
            self.b2.fonk5()
        print(self.b1)
        if self.b3:
            self.b3.fonk5()
    def fonk6(self):
        if self.b2:
            self.b2.fonk6()
        if self.b3:
            self.b3.fonk6()
        print(self.b1)
    def fonk7(self, val):
        if self.b1 = = val:
            if self.b2 and self.b3:
                b4 = self.b3.fonk8()
                self.b1 = b4.b1
                self.b3 = self.b3.fonk7(b4.b1)
                return self
            elif self.b2:
                b5 = self.b2
                del self
                return b5
            elif self.b3:
                b6 = self.b3
                del self
                return b6
            else:
                del self
                return None
        elif val > self.b1:
            if self.b3:
                self.b3 = self.b3.fonk7(val)
            else:
                print('class1 not found !!')
            return self
        else:
            if self.b2:
                self.b2 = self.b2.fonk7(val)
            else:
                print('class1 not found !!')
            return self
    def fonk8(self):
        if self.b2:
            return self.b2.fonk8()
        else:
            return self
if b7 = = "__main__":
    b8 = class1(10)
    b8.fonk2(5)
    b8.fonk2(15)
    b8.fonk2(3)
    b8.fonk2(7)
    b8.fonk2(13)
    b8.fonk2(17)
    print("In-order traversal:")
    b8.fonk5()
    print("\nPre-order traversal:")
    b8.fonk4()
    print("\nPost-order traversal:")
    b8.fonk6()
    print("\nSearching for 7 in the tree:")
    print("Found!" if b8.fonk3(7) else "Not found!")
    print("\nDeleting 15 from the tree:")
    b8.fonk7(15)
    b8.fonk5()
    print("\nDeleting 10 from the tree (b8):")
    b8 = b8.fonk7(10)
    b8.fonk5()