class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b1):
        b4 = class1(b1)
        b4.b2 = self.b3
        self.b3 = b4
    def fonk4(self, b1):
        b4 = class1(b1)
        if not self.b3:
            self.b3 = b4
            return
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = b4
    def fonk5(self):
        b5 = self.b3
        if not b5:
            print("Empty List!!!")
            return
        while b5:
            print(str(b5.b1), b6 = " ")
            b5 = b5.b2
            if b5:
                print("-->", b6 = " ")
        print()
b7 = class2()
for i in range(1, 6):
    b7.fonk3(i)
b7.fonk5()
for i in [12, 13, 3]:
    b7.fonk4(i)
b7.fonk5()
