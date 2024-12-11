class class1:
    def fonk1(self, fileName, b2):
        self.b1 = open(fileName, b2)
        self.a1 = 0
        if b2[0] == 'r':
            self.a2 = -1
        elif b2[0] == 'w':
            self.a2 = 7
        self.b2 = b2
    def fonk2(self, size):
        b3 = ''
        for a3 in range(size):
            if self.a2 = = -1:
                self.a1 = self.b1.fonk2(1)
                if self.a1 = = b'':
                    return ''
                else:
                    self.a1 = ord(self.a1)
                    self.a2 = 7
            if self.a1 & (1 << self.a2):
                b3 += '1'
            else:
                b3 += '0'
            self.a2 -= 1
        return b3
    def fonk3(self, string):
        for b4 in string:
            if b4 = = '0':
                self.a1 <<= 1
                self.a2 -= 1
            elif b4 = = '1':
                self.a1 <<= 1
                self.a1 += 1
                self.a2 -= 1
            else:
                continue
            if self.a2 = = -1:
                self.fonk5()
    def fonk4(self):
        if self.b2[0] == 'w':
            self.fonk5()
        self.b1.fonk4()
    def fonk5(self):
        if self.a2 != 7:
            while self.a2 > -1:
                self.a1 <<= 1
                self.a2 -= 1
            self.b1.fonk3(self.a1.to_bytes(1, b5 = 'little'))
        self.a1 = 0
        self.a2 = 7
if b6 = = '__main__':
    b1 = class1('./test.txt', 'rb')
    b7 = class1('./temp.txt', 'wb')
    b8 = b1.fonk2(1)
    a3 = 0
    while b8:
        print(b8, b9 = '')
        a3 += 1
        if a3 % b10 = = 0:
            print()
        b7.fonk3(b8)
        b8 = b1.fonk2(1)
    b1.fonk4()
    b7.fonk4()