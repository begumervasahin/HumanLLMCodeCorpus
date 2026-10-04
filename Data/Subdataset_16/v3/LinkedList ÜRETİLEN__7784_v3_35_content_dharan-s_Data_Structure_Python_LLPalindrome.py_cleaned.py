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
        if not self.b3:
            self.b3 = self.b4 = b5
        else:
            self.b4.b2 = b5
            self.b4 = b5
    def fonk4(self, b9):
        b5 = class1(b9)
        if not self.b3:
            self.b3 = b5
        else:
            b6 = self.b3
            while b6.b2:
                b6 = b6.b2
            b6.b2 = b5
    def fonk5(self):
        if not self.b3:
            print("List is empty")
            return
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
        if not self.b3:
            return
        b10 = self.b3
        b11 = self.b3
        while b11 and b11.b2:
            b10 = b10.b2
            b11 = b11.b2.b2
        print("Middle element:", b10.b1)
        b12 = self.b3
        while b12.b2:
            b12 = b12.b2
        print("Last element:", b12.b1)
    def fonk9(self):
        b13 = None
        b6 = self.b3
        while b6:
            b14 = b6.b2
            b6.b2 = b13
            b13 = b6
            b6 = b14
        self.b3 = b13
    def fonk10(self):
        if not self.b3:
            print("List is empty")
            return
        if not self.b3.b2:
            print("Palindrome")
            return
        b10 = self.b3
        b11 = self.b3
        while b11 and b11.b2:
            b10 = b10.b2
            b11 = b11.b2.b2
        b13 = None
        b6 = b10
        while b6:
            b14 = b6.b2
            b6.b2 = b13
            b13 = b6
            b6 = b14
        b15 = self.b3
        b16 = b13
        while b16:
            if b15.b1 != b16.b1:
                print("Not a palindrome")
                return
            b15 = b15.b2
            b16 = b16.b2
        print("Palindrome")
if b17 = = "__main__":
    b18 = class2()
    b18.fonk6()
    b18.fonk5()
    b18.fonk10()