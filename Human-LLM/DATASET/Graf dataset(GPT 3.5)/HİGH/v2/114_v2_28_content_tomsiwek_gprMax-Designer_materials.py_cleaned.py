class class1:
    def fonk1(self, b1 = 0.0, sigma=0.0, mu_r=0.0, sigma_mag=0.0, name=""):
        self.b2 = b1
        self.b3 = sigma
        self.b4 = mu_r
        self.b5 = sigma_mag
        self.b6 = name
    def fonk2(self):
        a1 = 299792458
        return a1 / (self.b2 ** 0.5)
b7 = class1(b1=4.0, sigma=0.01, mu_r=1.0, sigma_mag=0.005, name="Material1")
b8 = class1(b1=3.5, sigma=0.02, mu_r=1.2, sigma_mag=0.007, name="Material2")
print("class1 1 Wave Velocity:", b7.fonk2())
print("class1 2 Wave Velocity:", b8.fonk2())