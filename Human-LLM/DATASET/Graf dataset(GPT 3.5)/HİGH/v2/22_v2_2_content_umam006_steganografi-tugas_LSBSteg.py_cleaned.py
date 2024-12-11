import cv2
import numpy as np
import argparse
class class1(Exception):
    pass
class class2:
    def fonk1(self, im):
        self.b1 = im
        self.height, self.width, self.b2 = im.shape
        self.b3 = self.width * self.height
        self.b4 = [1, 2, 4, 8, 16, 32, 64, 128]
        self.b5 = [254, 253, 251, 247, 239, 223, 191, 127]
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.b6 = self.b4.pop(0)
        self.b7 = self.b5.pop(0)
    def fonk2(self, b10):
        for bit in b10:
            b8 = list(self.b1[self.a2, self.a1])
            if int(bit) == 1:
                b8[self.a3] |= self.b6
            else:
                b8[self.a3] &= self.b7
            self.b1[self.a2, self.a1] = tuple(b8)
            self.fonk3()
    def fonk3(self):
        if self.a3 = = self.b2 - 1:
            self.a3 = 0
            if self.a1 = = self.width - 1:
                self.a1 = 0
                if self.a2 = = self.height - 1:
                    self.a2 = 0
                    if self.b6 = = 128:
                        raise class1("No available slot remaining (b1 filled)")
                    else:
                        self.b6 = self.b4.pop(0)
                        self.b7 = self.b5.pop(0)
                else:
                    self.a2 += 1
            else:
                self.a1 += 1
        else:
            self.a3 += 1
    def fonk4(self):
        b8 = self.b1[self.a2, self.a1][self.a3]
        b9 = int(b8) & self.b6
        self.fonk3()
        return "1" if b9 > 0 else "0"
    def fonk5(self):
        return self.fonk6(8)
    def fonk6(self, nb):
        b10 = ""
        for _ in range(nb):
            b10 += self.fonk4()
        return b10
    def fonk7(self, txt):
        b11 = len(txt)
        b12 = bin(b11)[2:].zfill(16)
        self.fonk2(b12)
        for char in txt:
            b13 = bin(ord(char))[2:].zfill(8)
            self.fonk2(b13)
        return self.b1
    def fonk8(self):
        b12 = self.fonk6(16)
        b11 = int(b12, 2)
        b14 = ""
        for _ in range(b11):
            b13 = self.fonk5()
            b14 += chr(int(b13, 2))
        return b14
    def fonk9(self, imtohide):
        b18, b17, b15 = imtohide.shape
        if self.width * self.height * self.b2 < b17 * b18 * b15:
            raise class1("Carrier b1 not big enough to hold all the data for steganography")
        self.fonk2(bin(b17)[2:].zfill(16))
        self.fonk2(bin(b18)[2:].zfill(16))
        for i in range(b18):
            for j in range(b17):
                for chan in range(b15):
                    b16 = bin(imtohide[i, j][chan])[2:].zfill(8)
                    self.fonk2(b16)
        return self.b1
    def fonk10(self):
        b17 = int(self.fonk6(16), 2)
        b18 = int(self.fonk6(16), 2)
        b19 = np.zeros((b18, b17, 3), np.uint8)
        for i in range(b18):
            for j in range(b17):
                for chan in range(b19.shape[2]):
                    b20 = self.fonk5()
                    b19[i, j][chan] = int(b20, 2)
        return b19
    def fonk11(self, data):
        b21 = len(data)
        if self.width * self.height * self.b2 < b21 + 64:
            raise class1("Carrier b1 not big enough to hold all the data for steganography")
        self.fonk2(bin(b21)[2:].zfill(64))
        for byte in data:
            b22 = bin(byte)[2:].zfill(8)
            self.fonk2(b22)
        return self.b1
    def fonk12(self):
        b23 = self.fonk6(64)
        b21 = int(b23, 2)