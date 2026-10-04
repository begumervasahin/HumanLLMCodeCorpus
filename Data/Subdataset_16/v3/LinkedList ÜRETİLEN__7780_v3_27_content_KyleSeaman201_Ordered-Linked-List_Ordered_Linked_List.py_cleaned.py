class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
    def fonk2(self):
        return str(self.b1)
    b3 = __str__
class class2:
    def fonk3(self):
        self.b4 = None
        self.b5 = None
    def fonk4(self, b1):
        b6 = class1(b1)
        if not self.b4:
            self.b4 = self.b5 = b6
        elif b1 < self.b4.b1:
            b6.b2 = self.b4
            self.b4 = b6
        elif b1 > self.b5.b1:
            self.b5.b2 = b6
            self.b5 = b6
        else:
            b7 = self.b4
            while b7.b2 and b7.b2.b1 < b1:
                b7 = b7.b2
            b6.b2 = b7.b2
            b7.b2 = b6
            if b6.b2 is None:
                self.b5 = b6
    def fonk5(self, b1):
        if not self.b4:
            return
        if self.b4.b1 = = b1:
            self.b4 = self.b4.b2
            if not self.b4:
                self.b5 = None
            return
        b7 = self.b4
        while b7.b2 and b7.b2.b1 != b1:
            b7 = b7.b2
        if b7.b2:
            b7.b2 = b7.b2.b2
            if b7.b2 is None:
                self.b5 = b7
    def fonk6(self, b1):
        b7 = self.b4
        while b7:
            if b7.b1 = = b1:
                return True
            b7 = b7.b2
        return False
    def fonk7(self):
        if not self.b4:
            return None
        if self.b4 = = self.b5:
            b1 = self.b4.b1
            self.b4 = self.b5 = None
            return b1
        b7 = self.b4
        while b7.b2 != self.b5:
            b7 = b7.b2
        b1 = self.b5.b1
        self.b5 = b7
        self.b5.b2 = None
        return b1
    def fonk8(self):
        return self.b4 is None
    def fonk9(self):
        a1 = 0
        b7 = self.b4
        while b7:
            a1 += 1
            b7 = b7.b2
        return a1
    def fonk10(self):
        b7 = self.b4
        while b7:
            print(b7.b1, b8 = ' -> ')
            b7 = b7.b2
        print('None')
if b9 = = "__main__":
    b10 = class2()
    b10.fonk4(3)
    b10.fonk4(1)
    b10.fonk4(4)
    b10.fonk4(2)
    print("List after adding elements:")
    b10.fonk10()
    print("Size of list:", b10.fonk9())
    b10.fonk5(3)
    print("List after deleting 3:")
    b10.fonk10()
    print("Searching for 4:", b10.fonk6(4))
    print("Searching for 3:", b10.fonk6(3))
    print("Popping the last element:", b10.fonk7())
    print("List after popping the last element:")
    b10.fonk10()
    print("Is the list empty?", b10.fonk8())
    print("Size of list:", b10.fonk9())