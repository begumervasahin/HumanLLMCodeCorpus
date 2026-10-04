import aes
class class1:
    def fonk1(self):
        self.b1 = aes.AES(256)
    def fonk2(self, text, key):
        b2 = self.fonk4(text, 16)
        if not b2:
            return None
        b3 = 16 - len(b2[-1])
        b2[-1] += b3 * "="
        b4 = format(b3, "x") * 16
        b2.append(b4)
        b5 = self.fonk5(key)
        b6 = ""
        for block in b2:
            b7 = self.b1.fonk2(str(b5), block)
            b6 += ''.join(f'{i:02x}' for i in b7)
        return b6
    def fonk3(self, cipher_text, key):
        b2 = self.fonk4(cipher_text, 32)
        if not b2:
            return None
        b5 = self.fonk5(key)
        b8 = ""
        for block in b2:
            b9 = [int(h, 16) for h in self.fonk4(block, 2)]
            b10 = self.b1.fonk3(str(b5), b9)
            b8 += self.b1.to_plain(b10)
        b11 = int(b8[-1], 16)
        return b8[:-16 - b11]
    def fonk4(self, data, chunk_size):
        return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    def fonk5(self, key):
        b5 = 1
        for i, char in enumerate(key):
            b5 += ord(char) << (8 * i)
        while b5 < 0xfffffffffffff:
            b5 *= b5
        b5 &= 0xfffffffffffff
        return b5
if b12 = = "__main__":
    b13 = class1()
    b14 = "Tis but a scratch!"
    b15 = "A scratch?! your arm's off!"
    b16 = b13.fonk2(b15, b14)
    if b16:
        print("b1 TEXT: " + b16)
    b17 = b13.fonk3(b16, b14)
    if b17:
        print("\nPLAIN TEXT: " + b17)