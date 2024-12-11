class class1:
    def fonk1(self, b2, b1 = None, b3=0):
        self.b2 = b2
        if b1 is None:
            self.b1 = []
        else:
            self.b1 = b1
        self.b3 = b3
    def fonk2(self, b14):
        self.b1.append(b14)
        self.b3 += 1
    def fonk3(self):
        b4 = ''
        b4 += 'class1 Leader: ' + self.b2 + '\n'
        for comp in self.b1:
            b4 += comp.fonk11()
        return b4
class class2:
    def fonk4(self, b5, b6):
        self.b5 = b5
        self.b6 = b6
    def fonk5(self):
        return self.b5 + ' ' + self.b6 + '\n'
    def fonk6(self):
        return self.b5 + ' ' + self.b6
class class3:
    def fonk7(self, b5, b6):
        self.b5 = b5
        self.b6 = b6
        self.b7 = {}
    def fonk8(self):
        return '\t' + self.b5 + ' ' + self.b6 + '\n'
    def fonk9(self):
        return self.b5 + ' ' + self.b6
class class4:
    def fonk10(self, b8 = None, b9=None):
        if b8 is None:
            self.b8 = []
        else:
            self.b8 = b8
        if b9 is None:
            self.b9 = []
        else:
            self.b9 = b9
    def fonk11(self):
        b4 = ''
        for comp in self.b8:
            b4 += comp.fonk11()
        for hometeachee in self.b9:
            b4 += hometeachee.fonk11()
        return b4
if b10 = = "__main__":
    b11 = class2("John", "Doe")
    b12 = class3("Alice", "Smith")
    b13 = class3("Bob", "Johnson")
    b14 = class4([b11], [b12, b13])
    b15 = class1("class1 Leader", [b14])
    print(b15.fonk11())