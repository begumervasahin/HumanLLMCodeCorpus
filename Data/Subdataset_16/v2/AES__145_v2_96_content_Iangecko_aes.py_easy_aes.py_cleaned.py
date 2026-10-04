import aes
class class1:
    def fonk1(self):
        self.b1 = aes.AES(256)
    def fonk2(self, text, key):
        b2 = self.fonk4(text, 16)
        if not b2:
            return
        b3 = 16 - len(b2[-1])
        b2[-1] += b3 * "="
        b2.append(format(b3, "x") * 16)
        b4 = self.fonk5(key)
        b5 = ""
        for block in b2:
            b6 = self.b1.fonk2(str(b4), block)
            b5 += ''.join(f'{i:02x}' for i in b6)
        return b5
    def fonk3(self, b15, key):
        b2 = self.fonk4(b15, 32)
        if not b2:
            return
        b4 = self.fonk5(key)
        b7 = ""
        for block in b2:
            b8 = [int(h, 16) for h in self.fonk4(block, 2)]
            b9 = self.b1.fonk3(str(b4), b8)
            b7 += self.b1.to_plain(b9)
        b10 = int(b7[-1], 16)
        return b7[:-16 - b10]
    def fonk4(self, data, index):
        return [data[i:i + index] for i in range(0, len(data), index)]
    def fonk5(self, key):
        b4 = 1
        for i, c in enumerate(key):
            b4 += ord(c) << (8 * i)
        while b4 < 0xfffffffffffff:
            b4 *= b4
        b4 &= 0xfffffffffffff
        return b4
if b11 = = "__main__":
    b12 = class1()
    b13 = "Tis but a scratch!"
    b14 = "A scratch?! your arm's off!"
    b15 = b12.fonk2(b14, b13)
    print("b1 TEXT: " + b15)
    b7 = b12.fonk3(b15, b13)
    print("\nPLAIN TEXT: " + b7)