class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = class1()
    def fonk3(self, b1):
        b4 = class1(b1)
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = b4
    def fonk4(self):
        b5 = self.b3
        a1 = 0
        while b5.b2:
            a1 += 1
            b5 = b5.b2
        return a1
    def fonk5(self):
        b6 = []
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
            b6.fonk3(b5.b1)
        print(b6)
    def fonk6(self, index):
        if index >= self.fonk4():
            print('Index out of bounds')
            return None
        a2 = 0
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
            if a2 = = index:
                return b5.b1
            a2 += 1
    def fonk7(self, index):
        if index >= self.fonk4():
            print('Index out of bounds')
            return
        a2 = 0
        b5 = self.b3
        while b5.b2:
            b7 = b5
            b5 = b5.b2
            if a2 = = index:
                b7.b2 = b5.b2
                return
            a2 += 1
if b8 = = "__main__":
    b9 = class2()
    b9.fonk3(2)
    b9.fonk3(1)
    b9.fonk7(1)
    b9.fonk5()