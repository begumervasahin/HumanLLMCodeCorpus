class class1:
    def fonk1(self, b2, b1 = None, b3=0):
        self.b2 = b2
        if b1 is None:
            self.b1 = []
        else:
            self.b1 = b1
        self.b3 = b3
    def fonk2(self, b16):
        self.b1.append(b16)
        self.b3 += 1
    def fonk3(self):
        b4 = f'class1 Leader: {self.b2}\n'
        b5 = ''
        for b16 in self.b1:
            b5 += b16.fonk11()
        return b4 + b5
class class2:
    def fonk4(self, b6, b7):
        self.b6 = b6
        self.b7 = b7
    def fonk5(self):
        return f'{self.b6} {self.b7}\n'
    def fonk6(self):
        return f'{self.b6} {self.b7}'
class class3:
    def fonk7(self, b6, b7):
        self.b6 = b6
        self.b7 = b7
        self.b8 = {}
    def fonk8(self):
        return f'\t{self.b6} {self.b7}\n'
    def fonk9(self):
        return f'{self.b6} {self.b7}'
class class4:
    def fonk10(self, b9 = None, b10=None):
        if b9 is None:
            self.b9 = []
        else:
            self.b9 = b9
        if b10 is None:
            self.b10 = []
        else:
            self.b10 = b10
    def fonk11(self):
        b5 = ''
        for companion in self.b9:
            b5 += companion.fonk11()
        b11 = ''
        for hometeachee in self.b10:
            b11 += hometeachee.fonk11()
        return b5 + b11
if b12 = = "__main__":
    b13 = class2("John", "Doe")
    b14 = class3("Alice", "Smith")
    b15 = class3("Bob", "Johnson")
    b16 = class4([b13], [b14, b15])
    b17 = class1("class1 Leader", [b16])
    print(b17.fonk11())