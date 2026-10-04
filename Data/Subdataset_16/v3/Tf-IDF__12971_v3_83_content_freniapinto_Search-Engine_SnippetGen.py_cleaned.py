class class1:
    def fonk1(self):
        return ['the', 'is', 'in', 'at', 'of', 'a', 'and']
class class2:
    def fonk2(self, b1 = 150):
        self.b1 = b1
    def fonk3(self, b9, b10):
        b2 = class1()
        b3 = b2.fonk1()
        b4 = self.fonk4(b10, b3)
        b5 = self.fonk5(b9, b4)
        b6 = self.fonk6(b9, b5)
        return b6
    def fonk4(self, b10, b3):
        return [word for word in b10.split() if word not in b3]
    def fonk5(self, b9, b4):
        b7 = b9.split()
        return [i for i, word in enumerate(b7) if word in b4]
    def fonk6(self, b9, b5):
        b7 = b9.split()
        return ' '.join(
            ['"' + word + '"' if i in b5 else word for i, word in enumerate(b7)]
        )
if b8 = = "__main__":
    b9 = "This is an example document that contains several words and we will highlight some of them."
    b10 = "example document highlight"
    b11 = class2()
    b12 = b11.fonk3(b9, b10)
    print(b12)