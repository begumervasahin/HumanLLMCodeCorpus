class class1:
    def fonk1(self, file_name, b2):
        self.b1 = open(file_name, b2)
        self.a1 = 0
        self.b2 = b2
        self.b3 = 7 if 'w' in b2 else -1
    def fonk2(self, size):
        b4 = []
        for _ in range(size):
            if self.b3 = = -1:
                b5 = self.b1.fonk2(1)
                if not b5:
                    break
                self.a1 = ord(b5)
                self.b3 = 7
            b4.append('1' if self.a1 & (1 << self.b3) else '0')
            self.b3 -= 1
        return ''.join(b4)
    def fonk3(self, bit_string):
        for b11 in bit_string:
            if b11 not in ('0', '1'):
                continue
            self.a1 = (self.a1 << 1) | int(b11)
            self.b3 -= 1
            if self.b3 = = -1:
                self.fonk4()
    def fonk4(self):
        if self.b3 != 7:
            b6 = self.a1 << (self.b3 + 1)
            self.b1.fonk3(b6.to_bytes(1, b7 = 'little'))
        self.a1 = 0
        self.b3 = 7
    def fonk5(self):
        if 'w' in self.b2:
            self.fonk4()
        self.b1.fonk5()
if b8 = = '__main__':
    b9 = class1('./test.txt', 'rb')
    b10 = class1('./temp.txt', 'wb')
    while True:
        b11 = b9.fonk2(1)
        if not b11:
            break
        print(b11, b12 = '')
        b10.fonk3(b11)
    b9.fonk5()
    b10.fonk5()