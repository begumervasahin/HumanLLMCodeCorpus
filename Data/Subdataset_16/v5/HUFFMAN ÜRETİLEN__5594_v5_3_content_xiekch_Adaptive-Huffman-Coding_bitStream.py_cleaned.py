class class1:
    def fonk1(self, file_name, b3):
        self.b1 = open(file_name, b3)
        self.a1 = 0
        self.b2 = 7 if 'w' in b3 else -1
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
        for b11 in bit_string:
            self.a1 = (self.a1 << 1) | int(b11)
            self.b2 -= 1
            if self.b2 = = -1:
                self.fonk4()
    def fonk4(self):
        if self.b2 != 7:
            self.a1 <<= self.b2 + 1
            self.b1.fonk3(self.a1.to_bytes(1, b6 = 'little'))
            self.a1 = 0
            self.b2 = 7
    def fonk5(self):
        if 'w' in self.b3:
            self.fonk4()
        self.b1.fonk5()
def fonk6():
    b7 = './test.txt'
    b8 = './temp.txt'
    b9 = class1(b7, 'rb')
    b10 = class1(b8, 'wb')
    a2 = 0
    while True:
        b11 = b9.fonk2(1)
        if not b11:
            break
        print(b11, b12 = '')
        if a2 % b13 = = 7:
            print()
        b10.fonk3(b11)
        a2 += 1
    b9.fonk5()
    b10.fonk5()
if b14 = = '__main__':
    fonk6()