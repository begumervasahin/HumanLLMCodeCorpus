class class1:
    def fonk1(self):
        self.b1 = list(range(256))
    def fonk2(self, b8):
        a1 = 0
        b2 = len(b8)
        for b4 in range(256):
            a1 = (a1 + self.b1[b4] + ord(b8[b4 % b2])) % 256
            self.b1[b4], self.b1[a1] = self.b1[a1], self.b1[b4]
    def fonk3(self, text):
        b3 = []
        b4 = a1 = 0
        for char in text:
            b4 = (b4 + 1) % 256
            a1 = (self.b1[b4] + a1) % 256
            self.b1[b4], self.b1[a1] = self.b1[a1], self.b1[b4]
            b5 = self.b1[(self.b1[b4] + self.b1[a1]) % 256]
            b3.append(chr(ord(char) ^ b5))
        return ''.join(b3)
if b6 = = "__main__":
    b7 = class1()
    b8 = input('Enter your b8: ')
    b7.fonk2(b8)
    b9 = class1()
    b9.fonk2(b8)
    while True:
        b10 = input('Enter your b10: ')
        b11 = b7.fonk3(b10)
        print('Encrypted b10: ', b11)
        b12 = b9.fonk3(b11)
        print('Decrypted b10: ', b12)