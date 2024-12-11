class class1:
    def fonk1(self, b1 = 0.0, b2=0.0, b3=0.0, b4=0.0, b5=""):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self):
        a1 = 299792458
        return a1 / (self.b1 ** 0.5)
b6 = class1(b1=4.0, b2=0.01, b3=1.0, b4=0.005, b5="Material1")
b7 = class1(b1=3.5, b2=0.02, b3=1.2, b4=0.007, b5="Material2")
print("Material 1 Velocity:", b6.fonk2())
print("Material 2 Velocity:", b7.fonk2())