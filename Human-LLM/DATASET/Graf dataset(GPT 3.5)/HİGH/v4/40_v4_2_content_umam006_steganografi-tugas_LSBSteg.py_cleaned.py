import cv2
import docopt
import numpy as np
class class1(Exception):
    pass
class class2():
    def fonk1(self, im):
        self.b1 = im
        self.b22, self.b21, self.b2 = im.shape
        self.b3 = self.b21 * self.b22
        self.b4 = [1, 2, 4, 8, 16, 32, 64, 128]
        self.b5 = self.b4.pop(0)
        self.b6 = [254, 253, 251, 247, 239, 223, 191, 127]
        self.b7 = self.b6.pop(0)
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def fonk2(self, b9):
        for b13 in b9:
            b8 = list(self.b1[self.a2, self.a1])
            if int(b13) == 1:
                b8[self.a3] = int(b8[self.a3]) | self.b5
            else:
                b8[self.a3] = int(b8[self.a3]) & self.b7
            self.b1[self.a2, self.a1] = tuple(b8)
            self.fonk3()
    def fonk3(self):
        if self.a3 = = self.b2 - 1:
            self.a3 = 0
            if self.a1 = = self.b21 - 1:
                self.a1 = 0
                if self.a2 = = self.b22 - 1:
                    self.a2 = 0
                    if self.b5 = = 128:
                        raise class1("No available slot remaining (b1 filled)")
                    else:
                        self.b5 = self.b4.pop(0)
                        self.b7 = self.b6.pop(0)
                else:
                    self.a2 += 1
            else:
                self.a1 += 1
        else:
            self.a3 += 1
    def fonk4(self):
        b8 = self.b1[self.a2, self.a1][self.a3]
        b8 = int(b8) & self.b5
        self.fonk3()
        if b8 > 0:
            return "1"
        else:
            return "0"
    def fonk5(self):
        return self.fonk6(8)
    def fonk6(self, nb):
        b9 = ""
        for a4 in range(nb):
            b9 += self.fonk4()
        return b9
    def fonk7(self, b8):
        return self.fonk8(b8, 8)
    def fonk8(self, b8, bitsize):
        b10 = bin(b8)[2:]
        if len(b10) > bitsize:
            raise class1("Binary value larger than the expected b3")
        while len(b10) < bitsize:
            b10 = "0" + b10
        return b10
    def fonk9(self, txt):
        b11 = len(txt)
        b12 = self.fonk8(b11, 16)
        self.fonk2(b12)
        for char in txt:
            b13 = ord(char)
            self.fonk2(self.fonk7(b13))
        return self.b1
    def fonk10(self):
        b14 = self.fonk6(16)
        b11 = int(b14, 2)
        a4 = 0
        b15 = ""
        while a4 < b11:
            b16 = self.fonk5()
            a4 += 1
            b15 += chr(int(b16, 2))
        return b15
    def fonk11(self, imtohide):
        b17 = imtohide.b21
        b18 = imtohide.b22
        if self.b21 * self.b22 * self.b2 < b17 * b18 * imtohide.channels:
            raise class1("Carrier b1 not big enough to hold all the data for steganography")
        b19 = self.fonk8(b17, 16)
        b20 = self.fonk8(b18, 16)
        self.fonk2(b19)
        self.fonk2(b20)
        for b18 in range(imtohide.b22):
            for b17 in range(imtohide.b21):
                for chan in range(imtohide.channels):
                    b8 = imtohide[b18, b17][chan]
                    self.fonk2(self.fonk7(int(b8)))
        return self.b1
    def fonk12(self):
        b21 = int(self.fonk6(16), 2)
        b22 = int(self.fonk6(16), 2)
        b23 = np.zeros((b21, b22, 3), np.uint8)
        for b18 in range(b22):
            for b17 in range(b21):
                for chan in range(b23.channels):
                    b8 = list(b23[b18, b17])
                    b8[chan] = int(self.fonk5(), 2)
                    b23[b18, b17] = tuple(b8)
        return b23
    def fonk13(self, data):
        b11 = len(data)
        if self.b21 * self.b22 * self.b2 < b11 + 64:
            raise class1("Carrier b1 not big enough to hold all the data for steganography")
        self.fonk2(self.fonk8(b11, 64))
        for b24 in data:
            b24 = b24 if isinstance(b24, int) else ord(b24)
            self.fonk2(self.fonk7(b24))
        return self.b1
    def fonk14(self):
        b11 = int(self.fonk6(64), 2)
        output