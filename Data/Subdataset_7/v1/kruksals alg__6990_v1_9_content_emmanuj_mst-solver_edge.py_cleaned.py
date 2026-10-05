class class1:
    def fonk1(self, b, e, w):
        self.b1 = b
        self.b2 = e
        self.b3 = w
    def fonk2(self):
        return "e " + str(self.b1) + " " + str(self.b2) + " " + str(self.b3)
b4 = class1('a', 'b', 5)
b5 = class1('b', 'c', 7)
b6 = class1('c', 'd', 3)
print(b4)
print(b5)
print(b6)
