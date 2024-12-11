import heapq
import os
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
        self.b3 = {}
        self.b4 = {}
    class class2:
        def fonk2(self, b5, b6):
            self.b5 = b5
            self.b6 = b6
            self.b7 = None
            self.b8 = None
        def fonk3(self, other):
            return self.b6 < other.b6
        def fonk4(self, other):
            if other is None:
                return False
            if not isinstance(other, class1.class2):
                return False
            return self.b6 = = other.b6
    def fonk5(self, b23):
        b9 = {}
        for b27 in b23:
            b9[b27] = b9.get(b27, 0) + 1
        return b9
    def fonk6(self, b9):
        for key in b9:
            b10 = self.class2(key, b9[key])
            heapq.heappush(self.b2, b10)
    def fonk7(self):
        while len(self.b2) > 1:
            b11 = heapq.heappop(self.b2)
            b12 = heapq.heappop(self.b2)
            b13 = self.class2(None, b11.b6 + b12.b6)
            b13.b7 = b11
            b13.b8 = b12
            heapq.heappush(self.b2, b13)
    def fonk8(self, b14, b15):
        if b14 is None:
            return
        if b14.b5 is not None:
            self.b3[b14.b5] = b15
            self.b4[b15] = b14.b5
            return
        self.fonk8(b14.b7, b15 + "0")
        self.fonk8(b14.b8, b15 + "1")
    def fonk9(self):
        b14 = heapq.heappop(self.b2)
        b15 = ""
        self.fonk8(b14, b15)
    def fonk10(self, b23):
        b16 = ""
        for b27 in b23:
            b16 += self.b3[b27]
        return b16
    def fonk11(self, b16):
        b17 = 8 - len(b16) % 8
        for b21 in range(b17):
            b16 += "0"
        b18 = "{0:08b}".format(b17)
        b16 = b18 + b16
        return b16
    def fonk12(self, b24):
        if len(b24) % 8 != 0:
            raise ValueError("Encoded b23 not padded properly")
        b19 = bytearray()
        for i in range(0, len(b24), 8):
            b20 = b24[i:i+8]
            b19.append(int(b20, 2))
        return b19
    def fonk13(self):
        filename, b21 = os.b1.splitext(self.b1)
        b22 = filename + ".bin"
        with open(self.b1, 'r') as file, open(b22, 'wb') as output:
            b23 = file.read().rstrip()
            b9 = self.fonk5(b23)
            self.fonk6(b9)
            self.fonk7()
            self.fonk9()
            b16 = self.fonk10(b23)
            b24 = self.fonk11(b16)
            b25 = self.fonk12(b24)
            output.write(b25)
        print("Compressed")
        return b22
    def fonk14(self, b24):
        b18 = b24[:8]
        b17 = int(b18, 2)
        b16 = b24[8:]
        return b16[:-1 * b17]
    def fonk15(self, b16):
        b15 = ""
        b26 = ""
        for bit in b16:
            b15 += bit
            if b15 in self.b4:
                b27 = self.b4[b15]
                b26 += b27
                b15 = ""
        return b26
    def fonk16(self, input_path):
        filename, b21 = os.b1.splitext(self.b1)
        b22 = filename + "_decompressed" + ".txt"
        with open(input_path, 'rb') as file, open(b22, 'w') as output:
            b28 = ""
            b20 = file.read(1)
            while b20:
                b20 = ord(b20)
                b29 = bin(b20)[2:].rjust(8, '0')
                b28 += b29
                b20 = file.read(1)
            b16 = self.fonk14(b28)
            b30 = self.fonk15(b16)
            output.write(b30)
        print("Decompressed")
        return b22