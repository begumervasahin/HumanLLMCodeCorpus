class class1:
    def fonk1(self, file_name, b2):
        self.b1 = open(file_name, b2)
        self.a1 = 0
        if b2[0] == 'r':
            self.a2 = -1
        elif b2[0] == 'w':
            self.a2 = 7
        self.b2 = b2
    def fonk2(self, size):
        b3 = ''
        for _ in range(size):
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
    b7 = class1('./test.txt', 'rb')
    b8 = class1('./temp.txt', 'wb')
    b9 = b7.fonk2(1)
    a3 = 0
    while b9:
        print(b9, b10 = '')
        a3 += 1
        if a3 % b11 = = 0:
            print()
        b8.fonk3(b9)
        b9 = b7.fonk2(1)
    b7.fonk4()
    b8.fonk4()