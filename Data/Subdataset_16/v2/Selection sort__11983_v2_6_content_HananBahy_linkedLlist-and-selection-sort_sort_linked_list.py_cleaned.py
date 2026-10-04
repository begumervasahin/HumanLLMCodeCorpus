class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b1):
        b4 = class1(b1)
        b4.b2 = self.b3
        self.b3 = b4
    def fonk4(self):
        b5 = self.b3
        while b5:
            print(b5.b1, b6 = " -> ")
            b5 = b5.b2
        print("None")
    def fonk5(self):
        b5 = self.b3
        while b5:
            b7 = b5
            b8 = b5.b2
            while b8:
                if b8.b1 < b7.b1:
                    b7 = b8
                b8 = b8.b2
            b5.b1, b7.b1 = b7.b1, b5.b1
            b5 = b5.b2
if b9 = = "__main__":
    b10 = class2()
    b10.fonk3(100)
    b10.fonk3(500)
    b10.fonk3(70)
    b10.fonk3(1)
    b10.fonk3(-1)
    b10.fonk3(8)
    b10.fonk3(40)
    b10.fonk3(70)
    b10.fonk3(5)
    b10.fonk3(-1)
    print("Original list:")
    b10.fonk4()
    b10.fonk5()
    print("Sorted list:")
    b10.fonk4()