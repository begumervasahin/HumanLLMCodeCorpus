class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
        self.b4 = None
    def fonk3(self, b9):
        b5 = class1(b9)
        if self.b3 is None:
            self.b3 = b5
            self.b4 = b5
        else:
            self.b4.b2 = b5
            self.b4 = b5
    def fonk4(self, b9):
        b5 = class1(b9)
        if self.b3 is None:
            self.b3 = b5
        else:
            b6 = self.b3
            while b6.b2:
                b6 = b6.b2
            b6.b2 = b5
    def fonk5(self):
        if self.b3 is None:
            print("List is empty")
        else:
            b6 = self.b3
            while b6:
                print(b6.b1, b7 = " ")
                b6 = b6.b2
            print()
    def fonk6(self):
        b8 = int(input("Enter the number of nodes: "))
        for _ in range(b8):
            b9 = int(input("Enter b9 to be inserted: "))
            self.fonk4(b9)
    def fonk7(self):
        if self.b4:
            print("Tail element:", self.b4.b1)
    def fonk8(self):
        if self.b3 is not None:
            b10 = self.b3
            b11 = self.b3
            while b11 and b11.b2:
                b10 = b10.b2
                b11 = b11.b2.b2
            print("Middle element:", b10.b1)
            print("Last element:", (self.b4.b1 if self.b4 else "None"))
    def fonk9(self):
        b12 = None
        b6 = self.b3
        while b6:
            b13 = b6.b2
            b6.b2 = b12
            b12 = b6
            b6 = b13
        self.b3 = b12
    def fonk10(self):
        if self.b3 is None:
            print("List is empty")
            return
        b10 = self.b3
        b11 = self.b3
        b14 = None
        while b11 and b11.b2:
            b11 = b11.b2.b2
            b14 = b10
            b10 = b10.b2
        b15 = None
        if b11:
            b15 = b10.b2
        else:
            b15 = b10
        b15 = self.fonk11(b15)
        b16 = True
        b17 = self.b3
        while b15:
            if b17.b1 != b15.b1:
                b16 = False
                break
            b17 = b17.b2
            b15 = b15.b2
        if b14:
            b14.b2 = self.fonk11(b15)
        if b16:
            print("Palindrome")
        else:
            print("Not b16")
    def fonk11(self, b3):
        b12 = None
        b6 = b3
        while b6:
            b13 = b6.b2
            b6.b2 = b12
            b12 = b6
            b6 = b13
        return b12
b18 = class2()
b18.fonk6()
b18.fonk5()
b18.fonk10()