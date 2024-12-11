class class1():
    def fonk1(self):
        self.b1 = list(range(256))
    def fonk2(self, b7):
        a1 = 0
        for b3 in range(256):
            a1 = (a1 + self.b1[b3] + ord(b7[b3 % len(b7)])) % 256
            self.b1[b3], self.b1[a1] = self.b1[a1], self.b1[b3]
    def fonk3(self, text):
        b2 = list()
        b3 = a1 = 0
        for b4 in range(len(text)):
            b3 = (b3+1) % 256
            a1 = (self.b1[b3]+a1) % 256
            self.b1[b3], self.b1[a1] = self.b1[a1], self.b1[b3]
            b2.append(
                chr(ord(text[b4]) ^ self.b1[(self.b1[b3]+self.b1[a1]) % 256]))
        b4 = ''.join(b2)
        return b4
if b5 = = "__main__":
    b6 = class1()
    b7 = input('Enter your b7: ')
    b6.fonk2(b7)
    b8 = class1()
    b8.fonk2(b7)
    while True:
        b9 = input('Enter your b9: ')
        print('Initial b1:', b6.b1)
        b10 = b6.fonk3(b9)
        print('Encrypted b9:', b10)
        b11 = b8.fonk3(b10)
        print('Decrypted b9:', b11)