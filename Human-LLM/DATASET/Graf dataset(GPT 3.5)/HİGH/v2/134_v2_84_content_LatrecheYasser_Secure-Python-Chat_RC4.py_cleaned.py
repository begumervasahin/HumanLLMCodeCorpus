class class1():
    def fonk1(self):
        self.b1 = list(range(256))
    def fonk2(self, b7):
        a1 = 0
        for b3 in range(256):
            a1 = (a1 + self.b1[b3] + ord(b7[b3 % len(b7)])) % 256
            self.b1[b3], self.b1[a1] = self.b1[a1], self.b1[b3]
    def fonk3(self, text):
        b2 = []
        b3 = a1 = 0
        for x in range(len(text)):
            b3 = (b3 + 1) % 256
            a1 = (self.b1[b3] + a1) % 256
            self.b1[b3], self.b1[a1] = self.b1[a1], self.b1[b3]
            b2.append(chr(ord(text[x]) ^ self.b1[(self.b1[b3] + self.b1[a1]) % 256]))
        return ''.join(b2)
if b4 = = "__main__":
    b5 = class1()
    b6 = class1()
    b7 = input('Enter your b7: ')
    b5.fonk2(b7)
    b6.fonk2(b7)
    while True:
        b8 = input('Enter your b8: ')
        b9 = b5.fonk3(b8)
        print('Encrypted b8:', b9)
        b10 = b6.fonk3(b9)
        print('Decrypted b8:', b10)