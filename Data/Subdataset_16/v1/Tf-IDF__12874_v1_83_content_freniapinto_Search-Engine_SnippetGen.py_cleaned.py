class class1:
    def fonk1(self):
        return ['the', 'is', 'in', 'at', 'of', 'a', 'and']
class class2:
    def fonk2(self, b1 = 150):
        self.b1 = b1
    def fonk3(self, b8, b9):
        b2 = class1()
        b3 = b2.fonk1()
        b4 = [word for word in b9.split() if word not in b3]
        b5 = b8.split()
        b6 = [i for i, word in enumerate(b5) if word in b4]
        b7 = ' '.join(['"' + word + '"' if i in b6 else word for i, word in enumerate(b5)])
        return b7
b8 = "This is an example document that contains several words and we will highlight some of them."
b9 = "example document highlight"
b10 = class2()
b11 = b10.fonk3(b8, b9)
print(b11)