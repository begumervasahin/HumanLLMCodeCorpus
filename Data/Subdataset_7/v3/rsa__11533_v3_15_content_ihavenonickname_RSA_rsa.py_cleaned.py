class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, value):
        return pow(value, self.b1, self.b2)
def fonk3(u, v):
    u1, b3 = 1, u
    b9, b4 = 0, v
    b5 = False
    while b4:
        b6 = b3
        b7 = b3 % b4
        b8 = u1 + b6 * b9
        u1, b9 = b9, b8
        b3, b4 = b4, b7
        b5 = not b5
    if b3 != 1:
        return 0
    return v - u1 if b5 else u1
def fonk4(p, b6):
    b10 = (p - 1) * (b6 - 1)
    b2 = p * b6
    a1 = 65537
    b11 = fonk3(a1, b10)
    b12 = class1(b1=a1, b2=b2)
    b13 = class1(b1=b11, b2=b2)
    return b12, b13
def fonk5():
    b12, b13 = fonk4(23, 29)
    a2 = 42
    b14 = b12.fonk2(a2)
    b15 = b13.fonk2(b14)
    print("Original:", a2)
    print("Encrypted:", b14)
    print("Decrypted:", b15)
if b16 = = '__main__':
    fonk5()