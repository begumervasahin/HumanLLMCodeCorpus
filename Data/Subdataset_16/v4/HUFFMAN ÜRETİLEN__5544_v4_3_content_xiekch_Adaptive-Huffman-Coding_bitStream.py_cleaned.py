class class1:
    def fonk1(self, file_name, b3):
        self.b1 = open(file_name, b3)
        self.a1 = 0
        self.b2 = 7 if b3.startswith('w') else -1
        self.b3 = b3
    def fonk2(self, size):
        b4 = []
        for _ in range(size):
            if self.b2 = = -1:
                b5 = self.b1.fonk2(1)
                if not b5:
                    return ''.join(b4)
                self.a1 = ord(b5)
                self.b2 = 7
            b4.append('1' if self.a1 & (1 << self.b2) else '0')
            self.b2 -= 1
        return ''.join(b4)
    def fonk3(self, bit_string):
        for b10 in bit_string:
            self.a1 = (self.a1 << 1) | int(b10)
            self.b2 -= 1
            if self.b2 = = -1:
                self.fonk5()
    def fonk4(self):
        if self.b3.startswith('w'):
            self.fonk5()
        self.b1.fonk4()
    def fonk5(self):
        if self.b2 != 7:
            self.a1 <<= self.b2 + 1
            self.b1.fonk3(self.a1.to_bytes(1, b6 = 'little'))
        self.a1 = 0
        self.b2 = 7
if b7 = = '__main__':
    b8 = class1('./test.txt', 'rb')
    b9 = class1('./temp.txt', 'wb')
    a2 = 0
    while True:
        b10 = b8.fonk2(1)
        if not b10:
            break
        print(b10, b11 = '')
        if a2 % b12 = = 7:
            print()
        b9.fonk3(b10)
        a2 += 1
    b8.fonk4()
    b9.fonk4()