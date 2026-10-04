import aes
class class1():
    def fonk1(self):
        self.b1 = aes.aes(256)
    def fonk2(self, text, key):
        b2 = self.fonk4(text, 16)
        if not b2: return
        b3 = (16 - len(b2[-1]))
        b2[-1] += b3 * "="
        b2.append(format(b3, "x")*16)
        b4 = self.fonk5(key)
        b5 = ""
        for block in b2:
            for i in self.b1.fonk2(str(b4), block):
                b6 = hex(i)[2:]
                if len(b6) == 1: b6 = "0" + b6
                b5 += b6
        return b5
    def fonk3(self, b13, key):
        b2 = self.fonk4(b13, 32)
        if not b2: return
        b4 = self.fonk5(key)
        b7 = ""
        for block in b2:
            b8 = []
            for h in self.fonk4(block, 2):
                b8.append(int(h, 16))
            b7 += self.b1.to_plain(self.b1.fonk3(str(b4), b8))
        return b7[:-16-int(b7[-1], 16)]
    def fonk4(self, data, index):
        return [data[i:i+index] for i in range(0, len(data), index)]
    def fonk5(self, key):
        b4 = 1
        for i, c in enumerate(key): b4 += ord(c) << (8*i)
        while b4 < 0xfffffffffffff:
            b4 *= b4
        b4 &= 0xfffffffffffff
        return b4
if b9 = = "__main__":
    b10 = class1()
    b11 = "Tis but a scratch!"
    b12 = "A scratch?! your arm's off!"
    b13 = b10.fonk2(b12, b11)
    print("b1 TEXT: " + b13)
    b7 = b10.fonk3(b13, b11)
    print("\nPLAIN TEXT TEXT: " + b7)