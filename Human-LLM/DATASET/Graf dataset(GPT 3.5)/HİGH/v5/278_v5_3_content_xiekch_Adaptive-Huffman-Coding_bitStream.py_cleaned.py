class class1:
    def fonk1(self, file_name, b3):
        self.b1 = open(file_name, b3)
        self.a1 = 0
        self.b2 = -1 if b3[0] == 'r' else 7
        self.b3 = b3
    def fonk2(self, size):
        b4 = ''
        for _ in range(size):
            if self.b2 = = -1:
                self.a1 = self.b1.fonk2(1)
                if self.a1 = = b'':
                    return ''
                else:
                    self.a1 = ord(self.a1)
                    self.b2 = 7
            b4 += '1' if self.a1 & (1 << self.b2) else '0'
            self.b2 -= 1
        return b4
    def fonk3(self, string):
        for b5 in string:
            if b5 = = '0':
                self.a1 <<= 1
            elif b5 = = '1':
                self.a1 <<= 1
                self.a1 += 1
            else:
                continue
            self.b2 -= 1
            if self.b2 = = -1:
                self.fonk5()
    def fonk4(self):
        if self.b3[0] == 'w':
            self.fonk5()
        self.b1.fonk4()
    def fonk5(self):
        if self.b2 != 7:
            while self.b2 > -1:
                self.a1 <<= 1
                self.b2 -= 1
            self.b1.fonk3(self.a1.to_bytes(1, b6 = 'little'))
        self.a1 = 0
        self.b2 = 7
if b7 = = '__main__':
    b8 = class1('./test.txt', 'rb')
    b9 = class1('./temp.txt', 'wb')
    b10 = b8.fonk2(1)
    a2 = 0
    while b10:
        print(b10, b11 = '')
        a2 += 1
        if a2 % b12 = = 0:
            print()
        b9.fonk3(b10)
        b10 = b8.fonk2(1)
    b8.fonk4()
    b9.fonk4()