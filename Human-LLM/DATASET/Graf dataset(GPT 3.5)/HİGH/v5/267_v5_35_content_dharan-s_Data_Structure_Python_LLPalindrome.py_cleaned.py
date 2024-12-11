class class1:
    def fonk1(self, value):
        self.b1 = value
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b8):
        b4 = class1(b8)
        if not self.b3:
            self.b3 = b4
        else:
            b5 = self.b3
            while b5.b2:
                b5 = b5.b2
            b5.b2 = b4
    def fonk4(self):
        if not self.b3:
            print("List is empty")
        else:
            b5 = self.b3
            while b5:
                print(b5.b1, b6 = ' ')
                b5 = b5.b2
            print()
    def fonk5(self):
        b7 = int(input("Enter the number of nodes: "))
        for _ in range(b7):
            b8 = int(input("Enter b8 to be inserted: "))
            self.fonk3(b8)
    def fonk6(self):
        if not self.b3:
            print("List is Empty")
            return
        b9 = None
        b5 = self.b3
        while b5:
            b10 = b5.b2
            b5.b2 = b9
            b9 = b5
            b5 = b10
        self.b3 = b9
        b11 = self.b3
        b12 = self.b3
        while b12.b2:
            b11 = b11.b2
            b12 = b12.b2
            if b12.b2:
                b12 = b12.b2
        while b11:
            if b11.b1 != b9.b1:
                print("Not a palindrome")
                return
            b11 = b11.b2
            b9 = b9.b2
        print("Palindrome")
if b13 = = "__main__":
    b14 = class2()
    b14.fonk5()
    b14.fonk4()
    b14.fonk6()