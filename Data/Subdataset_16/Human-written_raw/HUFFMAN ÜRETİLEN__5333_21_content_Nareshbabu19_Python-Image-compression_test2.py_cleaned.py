import heapq
import os
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = None
        self.b4 = None
    def fonk2(self, b5):
        if (b5 = = None):
            return -1
        if (not isinstance(b5, class1)):
            return -1
        return self.b2 > b5.b2
class class2:
    def fonk3(self, b6):
        self.b6 = b6
        self.b7 = []
        self.b8 = {}
        self.b9 = {}
    def fonk4(self, b24):
        b10 = {}
        for b27 in b24:
            if not b27 in b10:
                b10[b27] = 0
            b10[b27] += 1
        return b10
    def fonk5(self, b10):
        for key in b10:
            b11 = class1(key, b10[key])
            heapq.heappush(self.b7, b11)
    def fonk6(self):
        while (len(self.b7) > 1):
            b12 = heapq.heappop(self.b7)
            b13 = heapq.heappop(self.b7)
            b14 = class1(None, b12.b2 + b13.b2)
            b14.b3 = b12
            b14.b4 = b13
            heapq.heappush(self.b7, b14)
    def fonk7(self, b15, b16):
        if (b15 = = None):
            return
        if (b15.b1 != None):
            self.b8[b15.b1] = b16
            self.b9[b16] = b15.b1
            return
        self.fonk7(b15.b3, b16 + "0")
        self.fonk7(b15.b4, b16 + "1")
    def fonk8(self):
        b15 = heapq.heappop(self.b7)
        b16 = ""
        self.fonk7(b15, b16)
    def fonk9(self, b24):
        b17 = ""
        for b27 in b24:
            b17 += self.b8[b27]
        return b17
    def fonk10(self, b17):
        b18 = 8 - len(b17) % 8
        for i in range(b18):
            b17 += "0"
        b19 = "{0:08b}".format(b18)
        b17 = b19 + b17
        return b17
    def fonk11(self, b25):
        if (len(b25) % 8 != 0):
            print("Encoded b24 not padded properly")
            exit(0)
        b20 = bytearray()
        for i in range(0, len(b25), 8):
            b21 = b25[i:i + 8]
            b20.append(int(b21, 2))
        return b20
    def fonk12(self):
        filename, b22 = os.b6.splitext(self.b6)
        b23 = filename + ".bin"
        with open(self.b6, 'r+') as file, open(b23, 'wb') as output:
            b24 = file.read()
            b24 = b24.rstrip()
            b10 = self.fonk4(b24)
            self.fonk5(b10)
            self.fonk6()
            self.fonk8()
            b17 = self.fonk9(b24)
            b25 = self.fonk10(b17)
            b20 = self.fonk11(b25)
            output.write(bytes(b20))
        print("Compressed")
        return b23
    def fonk13(self, b25):
        b19 = b25[:8]
        b18 = int(b19, 2)
        b25 = b25[8:]
        b17 = b25[:-1 * b18]
        return b17
    def fonk14(self, b17):
        b16 = ""
        b26 = ""
        for bit in b17:
            b16 += bit
            if (b16 in self.b9):
                b27 = self.b9[b16]
                b26 += b27
                b16 = ""
        return b26
    def fonk15(self, input_path):
        filename, b22 = os.b6.splitext(self.b6)
        b23 = filename + "_decompressed" + ".txt"
        with open(input_path, 'rb') as file, open(b23, 'w') as output:
            b28 = ""
            b21 = file.read(1)
            while (b21 != ""):
                b21 = ord(b21)
                b29 = bin(b21)[2:].rjust(8, '0')
                b28 += b29
                b21 = file.read(1)
            b17 = self.fonk13(b28)
            b30 = self.fonk14(b17)
            output.write(b30)
        print("Decompressed")
        return b23