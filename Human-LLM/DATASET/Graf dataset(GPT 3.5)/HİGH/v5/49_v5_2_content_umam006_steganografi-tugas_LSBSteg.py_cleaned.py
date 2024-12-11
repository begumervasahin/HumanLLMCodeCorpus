import cv2
import docopt
import numpy as np
class class1(Exception):
    pass
class class2():
    def fonk1(self, b1):
        self.b1 = b1
        self.b18, self.b17, self.b2 = b1.shape
        self.b3 = self.b17 * self.b18
        self.b4 = [1, 2, 4, 8, 16, 32, 64, 128]
        self.b5 = self.b4.pop(0)
        self.b6 = [254, 253, 251, 247, 239, 223, 191, 127]
        self.b7 = self.b6.pop(0)
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def fonk2(self, b9):
        for bit in b9:
            b8 = list(self.b1[self.a2, self.a1])
            if int(bit) == 1:
                b8[self.a3] |= self.b5
            else:
                b8[self.a3] &= self.b7
            self.b1[self.a2, self.a1] = tuple(b8)
            self.fonk3()
    def fonk3(self):
        if self.a3 = = self.b2 - 1:
            self.a3 = 0
            if self.a1 = = self.b17 - 1:
                self.a1 = 0
                if self.a2 = = self.b18 - 1:
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
        return "1" if b8 > 0 else "0"
    def fonk5(self):
        return self.fonk6(8)
    def fonk6(self, num_bits):
        b9 = ""
        for _ in range(num_bits):
            b9 += self.fonk4()
        return b9
    def fonk7(self, value):
        return self.fonk8(value, 8)
    def fonk8(self, value, bitsize):
        b10 = bin(value)[2:]
        if len(b10) > bitsize:
            raise class1("Binary value larger than the expected b3")
        return b10.zfill(bitsize)
    def fonk9(self, text):
        b11 = len(text)
        b12 = self.fonk8(b11, 16)
        self.fonk2(b12)
        for char in text:
            b13 = ord(char)
            self.fonk2(self.fonk7(b13))
        return self.b1
    def fonk10(self):
        b14 = self.fonk6(16)
        b11 = int(b14, 2)
        b15 = ""
        for _ in range(b11):
            b16 = self.fonk5()
            b15 += chr(int(b16, 2))
        return b15
    def fonk11(self, image_to_hide):
        b17 = image_to_hide.b17
        b18 = image_to_hide.b18
        if self.b3 < b17 * b18 * image_to_hide.channels:
            raise class1("Carrier b1 not big enough to hold all the data for steganography")
        b19 = self.fonk8(b17, 16)
        b20 = self.fonk8(b18, 16)
        self.fonk2(b19)
        self.fonk2(b20)
        for h in range(b18):
            for w in range(b17):
                for chan in range(image_to_hide.channels):
                    b21 = image_to_hide[h, w][chan]
                    self.fonk2(self.fonk7(int(b21)))
        return self.b1
    def fonk12(self):
        b17 = int(self.fonk6(16), 2)
        b18 = int(self.fonk6(16), 2)
        b22 = np.zeros((b17, b18, 3), np.uint8)
        for h in range(b18):
            for w in range(b17):
                for chan in range(b22.channels):
                    b21 = list(b22[h, w])
                    b21[chan] = int(self.fonk5(), 2)
                    b22[h, w] = tuple(b21)
        return b22
    def fonk13(self, data):
        b23 = len(data)
        if self.b3 < b23 + 64:
            raise class1("Carrier b1 not big enough to hold all the data for steganography")
        self.fonk2(self.fonk8(b23, 64))
        for b16 in data:
            b16 = b16 if isinstance(b16, int) else ord(b16)
            self.fonk2(self.fonk7(b16))
        return self.b1
    def fonk14(self):
        b24 = self.fonk6(64)
        b23 = int(b24, 2)
        b25 = b""
        for _ in range(b23):
            b25 += chr(int(self.fonk5(), 2)).encode("utf-8")
        return b25
def fonk15():
    b26 = docopt.docopt(__doc__, version="0.2")
    b27 = b26["--in"]
    b28 = b26["--out"]
    b29 = cv2.imread(b27)
    b30 = class2(b29)
    if b26['encode']:
        b31 = open(b26["--file"], "rb").read()
        b32 = b30.fonk13(b31)
        cv2.imwrite(b28, b32)
    elif b26["decode"]:
        b25 = b30.fonk14()
        with open(b28, "wb") as f:
            f.write(b25)
if b33 = = "__main__":
    fonk15()