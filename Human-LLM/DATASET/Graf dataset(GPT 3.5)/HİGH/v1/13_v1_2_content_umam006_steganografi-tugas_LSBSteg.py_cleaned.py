import cv2
import numpy as np
import argparse
class class1(Exception):
    pass
class class2():
    def fonk1(self, im):
        self.b1 = im
        self.b22, self.b21, self.b2 = im.shape
        self.b3 = self.b21 * self.b22
        self.b4 = [1,2,4,8,16,32,64,128]
        self.b5 = self.b4.pop(0)
        self.b6 = [254,253,251,247,239,223,191,127]
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
        if self.a3 = = self.b2-1:
            self.a3 = 0
            if self.a1 = = self.b21-1:
                self.a1 = 0
                if self.a2 = = self.b22-1:
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
            raise class1("binary value larger than the expected b3")
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
        b17 = imtohide.shape[1]
        b18 = imtohide.shape[0]
        if self.b21 * self.b22 * self.b2 < b17 * b18 * imtohide.shape[2]:
            raise class1("Carrier b1 not big enough to hold all the b33 to steganography")
        b19 = self.fonk8(b17, 16)
        b20 = self.fonk8(b18, 16)
        self.fonk2(b19)
        self.fonk2(b20)
        for a4 in range(b18):
            for j in range(b17):
                for chan in range(imtohide.shape[2]):
                    b8 = imtohide[a4, j][chan]
                    self.fonk2(self.fonk7(int(b8)))
        return self.b1
    def fonk12(self):
        b21 = int(self.fonk6(16), 2)
        b22 = int(self.fonk6(16), 2)
        b23 = np.zeros((b22, b21, 3), np.uint8)
        for a4 in range(b22):
            for j in range(b21):
                for chan in range(b23.shape[2]):
                    b8 = list(b23[a4, j])
                    b8[chan] = int(self.fonk5(), 2)
                    b23[a4, j] = tuple(b8)
        return b23
    def fonk13(self, b33):
        b11 = len(b33)
        if self.b21 * self.b22 * self.b2 < b11 + 64:
            raise class1("Carrier b1 not big enough to hold all the b33 to steganography")
        self.fonk2(self.fonk8(b11, 64))
        for b24 in b33:
            b24 = b24 if isinstance(b24, int) else ord(b24)
            self.fonk2(self.fonk7(b24))
        return self.b1
    def fonk14(self):
        b11 = int(self.fonk6(64), 2)
        b25 = b""
        for a4 in range(b11):
            b25 += chr(int(self.fonk5(), 2)).encode("utf-8")
        return b25
def fonk15():
    b26 = argparse.ArgumentParser(description="LSB Steganography")
    b26.add_argument("b32", b27 = ["encode", "decode"], b28="Select encode or decode b32")
    b26.add_argument("-a4", "--input", b28 = "Input b1 (carrier)")
    b26.add_argument("-o", "--b25", b28 = "Output b1 (or extracted file)")
    b26.add_argument("-f", "--file", b28 = "File to hide")
    b29 = b26.parse_args()
    b30 = cv2.imread(b29.input)
    b31 = class2(b30)
    if b29.b32 = = "encode":
        b33 = open(b29.file, "rb").read()
        b34 = b31.fonk13(b33)
        cv2.imwrite(b29.b25, b34)
    elif b29.b32 = = "decode":
        b35 = b31.fonk14()
        with open(b29.b25, "wb") as f:
            f.write(b35)
if b36 = = "__main__":
    fonk15()