import cv2
class class1(BaseException):
    pass
def fonk1(i, l):
    b1 = bin(i)[2:]
    if len(b1) > l:
        raise class1("Bit size is larger than expected.")
    while len(b1) < l:
        b1 = "0" + b1
    return b1
def fonk2(b10):
    return fonk1(ord(b10), 8)
class class2:
    a1 = 16
    def fonk3(self, img):
        self.size_x, self.size_y, self.b2 = img.shape
        self.b3 = img
        self.a2 = 0
        self.a3 = 0
        self.a4 = 0
    def fonk4(self):
        if self.a4 != self.b2 - 1:
            self.a4 += 1
        else:
            self.a4 = 0
            if self.a3 != self.size_y - 1:
                self.a3 += 1
            else:
                self.a3 = 0
                if self.a2 != self.size_x - 1:
                    self.a2 += 1
                else:
                    raise class1("Need larger b3")
    def fonk5(self, bit):
        b4 = self.b3[self.a2, self.a3][self.a4]
        b5 = bin(b4)[2:]
        if b5[-1] != bit:
            b5 = b5[:-1] + bit
        self.b3[self.a2, self.a3][self.a4] = int(b5, 2)
        self.fonk4()
    def fonk6(self, b6):
        for bit in b6:
            self.fonk5(bit)
    def fonk7(self):
        b4 = self.b3[self.a2, self.a3][self.a4]
        return bin(b4)[-1]
    def fonk8(self, b8):
        b6 = ""
        for _ in range(0, b8):
            b6 += self.fonk7()
            self.fonk4()
        return b6
    def fonk9(self, b9):
        b7 = fonk1(len(b9), self.a1)
        self.fonk6(b7)
        for b10 in b9:
            b6 = fonk2(b10)
            self.fonk6(b6)
    def fonk10(self):
        b8 = int(self.fonk8(self.a1), 2)
        b9 = ""
        for _ in range(0, b8):
            b10 = int(self.fonk8(8), 2)
            b9 += chr(b10)
        return b9
    def fonk11(self, dstPath):
        cv2.imwrite(dstPath, self.b3)
if b11 = = "__main__":
    b12 = class2(cv2.imread('dst.png'))
    b9 = b12.fonk10()
    print(b9)