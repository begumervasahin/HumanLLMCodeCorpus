class class1:
    def fonk1(self, b1):
        self.a1 = 0
        self.a2 = 0
        self.a3 = 9999999
        self.b1 = b1
    def fonk2(self):
        return self.a3
b2 = class1(1)
print("Distance of class1 1:", b2.fonk2())
