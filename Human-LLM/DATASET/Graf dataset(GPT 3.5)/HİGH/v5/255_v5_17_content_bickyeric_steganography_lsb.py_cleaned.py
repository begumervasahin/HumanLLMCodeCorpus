import cv2
class class1(BaseException):
    pass
def fonk1(i, length):
    b1 = bin(i)[2:]
    if len(b1) > length:
        raise class1("Bit size is larger than expected.")
    return b1.zfill(length)
def fonk2(c):
    return fonk1(ord(c), 8)
class class2:
    a1 = 16
    def fonk3(self, b2):
        self.b2 = b2
        self.size_x, self.size_y, self.b3 = b2.shape
        self.b6, self.b5, self.b4 = 0, 0, 0
    def fonk4(self):
        self.b4 = (self.b4 + 1) % self.b3
        if self.b4 = = 0:
            self.b5 = (self.b5 + 1) % self.size_y
            if self.b5 = = 0:
                self.b6 = (self.b6 + 1) % self.size_x
                if self.b6 = = 0:
                    raise class1("Need larger b2")
    def fonk5(self, bit):
        b7 = self.b2[self.b6, self.b5][self.b4]
        b8 = bin(b7)[2:].zfill(8)
        b8 = b8[:-1] + bit
        self.b2[self.b6, self.b5][self.b4] = int(b8, 2)
        self.fonk4()
    def fonk6(self, b9):
        for bit in b9:
            self.fonk5(bit)
    def fonk7(self):
        b7 = self.b2[self.b6, self.b5][self.b4]
        return bin(b7)[-1]
    def fonk8(self, length):
        b9 = ""
        for _ in range(length):
            b9 += self.fonk7()
            self.fonk4()
        return b9
    def fonk9(self, b13):
        b10 = fonk1(len(b13), self.a1)
        self.fonk6(b10)
        for c in b13:
            b11 = fonk2(c)
            self.fonk6(b11)
    def fonk10(self):
        b12 = int(self.fonk8(self.a1), 2)
        b13 = ""
        for _ in range(b12):
            b14 = int(self.fonk8(8), 2)
            b13 += chr(b14)
        return b13
    def fonk11(self, dst_path):
        cv2.imwrite(dst_path, self.b2)
if b15 = = "__main__":
    b16 = class2(cv2.imread('dst.png'))
    b17 = b16.fonk10()
    print(b17)