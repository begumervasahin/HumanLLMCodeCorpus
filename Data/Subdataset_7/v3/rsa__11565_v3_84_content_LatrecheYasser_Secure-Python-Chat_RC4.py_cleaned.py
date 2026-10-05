class class1:
    def fonk1(self):
        self.b1 = list(range(256))
    def fonk2(self, b8):
        a1 = 0
        for b2 in range(256):
            a1 = (a1 + self.b1[b2] + ord(b8[b2 % len(b8)])) % 256
            self.b1[b2], self.b1[a1] = self.b1[a1], self.b1[b2]
    def fonk3(self, text):
        b2 = a1 = 0
        b3 = []
        for _ in range(len(text)):
            b2 = (b2 + 1) % 256
            a1 = (self.b1[b2] + a1) % 256
            self.b1[b2], self.b1[a1] = self.b1[a1], self.b1[b2]
            b3.append(self.b1[(self.b1[b2] + self.b1[a1]) % 256])
        return b3
    def fonk4(self, text, b3):
        b4 = []
        for char, keystream_byte in zip(text, b3):
            b4.append(chr(ord(char) ^ keystream_byte))
        return ''.join(b4)
if b5 = = "__main__":
    b6 = class1()
    b7 = class1()
    b8 = input('Enter your b8: ')
    b6.fonk2(b8)
    b7.fonk2(b8)
    while True:
        b9 = input('Enter your b9: ')
        b3 = b6.fonk3(b9)
        b10 = b6.fonk4(b9, b3)
        print('Encrypted b9:', b10)
        b11 = b7.fonk4(b10, b3)
        print('Decrypted b9:', b11)