class class1:
    def fonk1(self, b1 = None, b2=None):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        return 'class1 [' + str(self.b1) + ']'
class class2:
    def fonk3(self):
        self.b3 = None
        self.b4 = None
    def fonk4(self, x):
        if self.b3 is None:
            self.b3 = class1(x, None)
            self.b4 = self.b3
        elif self.b4 = = self.b3:
            self.b4 = class1(x, None)
            self.b3.b2 = self.b4
        else:
            b5 = class1(x, None)
            self.b4.b2 = b5
            self.b4 = b5
    def fonk5(self):
        if self.b3:
            b5 = self.b3
            b6 = 'class2 [\n' + str(b5.b1) + '\n'
            while b5.b2:
                b5 = b5.b2
                b6 += str(b5.b1) + '\n'
            return b6 + ']'
        return 'class2 []'
    def fonk6(self):
        self.fonk3()
if b7 = = '__main__':
    b8 = class2()
    b8.fonk4(1)
    b8.fonk4(2)
    b8.fonk4(3)
    print(b8)
    b8.fonk6()
    print(b8)