class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b1):
        if b1 = = self.b1:
            return False
        elif b1 < self.b1:
            if self.b2:
                return self.b2.fonk2(b1)
            else:
                self.b2 = class1(b1)
                return True
        else:
            if self.b3:
                return self.b3.fonk2(b1)
            else:
                self.b3 = class1(b1)
                return True
    def fonk3(self, b1):
        if b1 = = self.b1:
            return True
        elif b1 < self.b1:
            return self.b2.fonk3(b1) if self.b2 else False
        else:
            return self.b3.fonk3(b1) if self.b3 else False
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
    def fonk7(self, b1):
        if b1 < self.b1:
            if self.b2:
                self.b2 = self.b2.fonk7(b1)
            else:
                print(f'class1 with b1 {b1} not found!')
        elif b1 > self.b1:
            if self.b3:
                self.b3 = self.b3.fonk7(b1)
            else:
                print(f'class1 with b1 {b1} not found!')
        else:
            if not self.b2:
                return self.b3
            if not self.b3:
                return self.b2
            b4 = self.fonk8()
            self.b1 = b4.b1
            self.b3 = self.b3.fonk7(b4.b1)
        return self
    def fonk8(self):
        b5 = self
        while b5.b2:
            b5 = b5.b2
        return b5
if b6 = = "__main__":
    b7 = class1(10)
    b7.fonk2(5)
    b7.fonk2(15)
    b7.fonk2(3)
    b7.fonk2(7)
    b7.fonk2(13)
    b7.fonk2(17)
    print("In-order traversal:")
    b7.fonk5()
    print("\nPre-order traversal:")
    b7.fonk4()
    print("\nPost-order traversal:")
    b7.fonk6()
    print("\nSearching for 7 in the tree:")
    print("Found!" if b7.fonk3(7) else "Not found!")
    print("\nDeleting 15 from the tree:")
    b7.fonk7(15)
    b7.fonk5()
    print("\nDeleting 10 from the tree (b7):")
    b7 = b7.fonk7(10)
    if b7:
        b7.fonk5()
    else:
        print("Tree is empty.")