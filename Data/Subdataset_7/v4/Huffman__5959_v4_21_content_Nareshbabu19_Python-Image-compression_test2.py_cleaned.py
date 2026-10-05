import heapq
import os
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = None
        self.b4 = None
    def fonk2(self, other):
        return self.b2 < other.b2
class class2:
    def fonk3(self, b5):
        self.b5 = b5
        self.b6 = []
        self.b7 = {}
        self.b8 = {}
    def fonk4(self, b23):
        b9 = {}
        for character in b23:
            b9[character] = b9.get(character, 0) + 1
        return b9
    def fonk5(self, b9):
        for key in b9:
            b10 = class1(key, b9[key])
            heapq.heappush(self.b6, b10)
    def fonk6(self):
        while len(self.b6) > 1:
            b11 = heapq.heappop(self.b6)
            b12 = heapq.heappop(self.b6)
            b13 = class1(None, b11.b2 + b12.b2)
            b13.b3 = b11
            b13.b4 = b12
            heapq.heappush(self.b6, b13)
    def fonk7(self, b14, b15):
        if b14 is None:
            return
        if b14.b1 is not None:
            self.b7[b14.b1] = b15
            self.b8[b15] = b14.b1
            return
        self.fonk7(b14.b3, b15 + "0")
        self.fonk7(b14.b4, b15 + "1")
    def fonk8(self):
        b14 = heapq.heappop(self.b6)
        b15 = ""
        self.fonk7(b14, b15)
    def fonk9(self, b23):
        b16 = ""
        for character in b23:
            b16 += self.b7[character]
        return b16
    def fonk10(self, b16):
        b17 = 8 - len(b16) % 8
        b18 = "{:08b}".format(b17)
        b16 = b18 + b16 + "0" * b17
        return b16
    def fonk11(self, b24):
        b19 = bytearray()
        for i in range(0, len(b24), 8):
            b20 = b24[i:i + 8]
            b19.append(int(b20, 2))
        return b19
    def fonk12(self):
        filename, b21 = os.b5.splitext(self.b5)
        b22 = filename + ".bin"
        with open(self.b5, 'r') as file, open(b22, 'wb') as output:
            b23 = file.read().rstrip()
            b9 = self.fonk4(b23)
            self.fonk5(b9)
            self.fonk6()
            self.fonk8()
            b16 = self.fonk9(b23)
            b24 = self.fonk10(b16)
            b19 = self.fonk11(b24)
            output.write(b19)
        print("Compressed")
        return b22
    def fonk13(self, b24):
        b18 = b24[:8]
        b17 = int(b18, 2)
        return b24[8:-b17]
    def fonk14(self, b16):
        b15 = ""
        b25 = ""
        for bit in b16:
            b15 += bit
            if b15 in self.b8:
                b25 += self.b8[b15]
                b15 = ""
        return b25
    def fonk15(self, input_path):
        filename, b21 = os.b5.splitext(input_path)
        b22 = filename + "_decompressed.txt"
        with open(input_path, 'rb') as file, open(b22, 'w') as output:
            b26 = "".join(format(b20, '08b') for b20 in file.read())
            b16 = self.fonk13(b26)
            b27 = self.fonk14(b16)
            output.write(b27)
        print("Decompressed")
        return b22