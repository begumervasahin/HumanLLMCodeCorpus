class class1:
    def fonk1(self, value):
        self.b1 = value
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
            while b6.b2 is not None:
                b6 = b6.b2
            b6.b2 = b5
    def fonk5(self):
        if self.b3 is None:
            print("List is empty")
        else:
            b6 = self.b3
            while b6 is not None:
                print(b6.b1, " ", b7 = '')
                b6 = b6.b2
            print()
    def fonk6(self):
        b8 = int(input("Enter the number of nodes: "))
        for i in range(b8):
            b9 = int(input("Enter b9 to be inserted: "))
            self.fonk4(b9)
    def fonk7(self):
        if self.b3 is not None:
            print(self.b4.b1)
    def fonk8(self):
        if self.b3 is not None:
            b10 = self.b3
            b11 = self.b3
            while b11.b2:
                b10 = b10.b2
                b11 = b11.b2
                if b11.b2 is not None:
                    b11 = b11.b2
            print("Middle element:", b10.b1)
            print("Last element:", b11.b1)
    def fonk9(self):
        if self.b3 and self.b3.b2:
            b12 = None
            b6 = self.b3
            while b6 is not None:
                b13 = b6.b2
                b6.b2 = b12
                b12 = b6
                b6 = b13
            self.b3 = b12
    def fonk10(self):
        if self.b3 and self.b3.b2:
            b6 = self.b3
            self.fonk9()
            b14 = self.b3
            while b6 and b14:
                if b6.b1 != b14.b1:
                    print("Not palindrome")
                    return
                b6 = b6.b2
                b14 = b14.b2
            print("Palindrome")
        elif self.b3 is None:
            print("List is Empty")
        else:
            print("Palindrome")
if b15 = = "__main__":
    b16 = class2()
    b16.fonk6()
    print("Linked List:")
    b16.fonk5()
    b16.fonk10()