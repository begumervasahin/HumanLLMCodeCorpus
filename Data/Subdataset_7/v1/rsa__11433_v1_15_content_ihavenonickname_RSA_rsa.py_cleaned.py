class class1():
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, value):
        return pow(value, self.b1, self.b2)
def fonk3(u, v):
    a1 = 1
    b3 = u
    a2 = 0
    b4 = v
    b5 = False
    while b4:
        b6 = b3
        b7 = b3 % b4
        b8 = a1 + b6 * a2
        a1 = a2
        a2 = b8
        b3 = b4
        b4 = b7
        b5 = not b5
    if b3 != 1:
        return 0
    if b5:
        return v - a1
    return a1
def fonk4(p, b6):
    b9 = (p - 1) * (b6 - 1)
    b10 = p * b6
    a3 = 65537
    b11 = fonk3(a3, b9)
    b12 = class1(b1=a3, b2=b10)
    b13 = class1(b1=b11, b2=b10)
    return b12, b13
def fonk5():
    b12, b13 = fonk4(23, 29)
    a4 = 42
    b14 = b12.fonk2(a4)
    b15 = b13.fonk2(b14)
    print("Original:", a4)
    print("Encrypted:", b14)
    print("Decrypted:", b15)
if b16 = = '__main__':
    fonk5()