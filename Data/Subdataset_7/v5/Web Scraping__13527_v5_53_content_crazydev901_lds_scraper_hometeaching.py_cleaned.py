class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b1 = b1 or []
    def fonk2(self, b14):
        self.b1.append(b14)
    def fonk3(self):
        b3 = f'class1 Leader: {self.b2}\n'
        b4 = ''.join(str(comp) for comp in self.b1)
        return b3 + b4
class class2:
    def fonk4(self, b5, b6):
        self.b5 = b5
        self.b6 = b6
    def fonk5(self):
        return f'{self.b5} {self.b6}\n'
class class3(class2):
    def fonk6(self):
        return f'{self.b5} {self.b6}'
class class4(class2):
    pass
class class5:
    def fonk7(self, b7 = None, b8=None):
        self.b7 = b7 or []
        self.b8 = b8 or []
    def fonk8(self):
        b4 = ''.join(str(comp) for comp in self.b7)
        b9 = ''.join(str(teachee) for teachee in self.b8)
        return b4 + b9
if b10 = = "__main__":
    b11 = class3("John", "Doe")
    b12 = class4("Alice", "Smith")
    b13 = class4("Bob", "Johnson")
    b14 = class5([b11], [b12, b13])
    b15 = class1("class1 Leader", [b14])
    print(b15)