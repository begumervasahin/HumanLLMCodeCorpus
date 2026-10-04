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
        if self.b3 is None:
            print("List is empty")
            return
        b10 = self.b3
        b11 = self.b3
        while b11 and b11.b2:
            b10 = b10.b2
            b11 = b11.b2.b2
        b12 = b10.b1
        b13 = self.b4.b1 if self.b4 else "None"
        print("Middle element:", b12)
        print("Last element:", b13)
    def fonk9(self):
        b14 = None
        b6 = self.b3
        while b6:
            b15 = b6.b2
            b6.b2 = b14
            b14 = b6
            b6 = b15
        self.b3 = b14
    def fonk10(self):
        if self.b3 is None:
            print("List is empty")
            return
        b16 = self.fonk11()
        b17 = self.fonk12(b16.b2 if b16 else None)
        b18 = self.fonk13(self.b3, b17)
        self.fonk12(b17)
        print("Palindrome" if b18 else "Not b18")
    def fonk11(self):
        b10 = self.b3
        b11 = self.b3
        while b11 and b11.b2:
            b11 = b11.b2.b2
            b10 = b10.b2
        return b10
    def fonk12(self, b3):
        b14 = None
        b6 = b3
        while b6:
            b15 = b6.b2
            b6.b2 = b14
            b14 = b6
            b6 = b15
        return b14
    def fonk13(self, b19, b20):
        while b20:
            if b19.b1 != b20.b1:
                return False
            b19 = b19.b2
            b20 = b20.b2
        return True
b21 = class2()
b21.fonk6()
b21.fonk5()
b21.fonk10()