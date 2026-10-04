class class1:
    def fonk1(self, file_name, b3):
        self.b1 = open(file_name, b3)
        self.a1 = 0
        self.b2 = 7 if b3[0] == 'w' else -1
        self.b3 = b3
    def fonk2(self, size):
        b4 = ''
        for _ in range(size):
            if self.b2 = = -1:
                self.a1 = self.b1.fonk2(1)
                if not self.a1:
                    return b4
                self.a1 = ord(self.a1)
                self.b2 = 7
            b4 += '1' if self.a1 & (1 << self.b2) else '0'
            self.b2 -= 1
        return b4
    def fonk3(self, string):
        for char in string:
            if char not in ('0', '1'):
                continue
            self.a1 = (self.a1 << 1) | (1 if char == '1' else 0)
            self.b2 -= 1
            if self.b2 = = -1:
                self.fonk4()
    def fonk4(self):
        if self.b2 != 7:
            self.a1 <<= self.b2 + 1
            self.b1.fonk3(self.a1.to_bytes(1, b5 = 'little'))
        self.a1 = 0
        self.b2 = 7
    def fonk5(self):
        if self.b3[0] == 'w':
            self.fonk4()
        self.b1.fonk5()
if b6 = = '__main__':
    b7 = class1('./test.txt', 'rb')
    b8 = class1('./temp.txt', 'wb')
    b9 = b7.fonk2(1)
    while b9:
        print(b9, b10 = '')
        b8.fonk3(b9)
        b9 = b7.fonk2(1)
    b7.fonk5()
    b8.fonk5()