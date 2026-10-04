class class1:
    def fonk1(self, b1 = 0.0, b2=0.0, b3=0.0, b4=0.0, b5=""):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self):
        a1 = 299792458
        return a1 / (self.b1**0.5)
if b6 = = "__main__":
    b7 = class1(b1=4.0, b2=0.01, b3=1.0, b4=0.0, b5="SampleMaterial")
    b8 = b7.fonk2()
    print(f"The b8 of the electromagnetic wave in {b7.b5} is {b8:.2f} m/s")