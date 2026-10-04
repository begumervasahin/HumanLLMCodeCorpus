class class1:
    def fonk1(self, args):
        self.b1 = ''
        self.b2 = ''
        self.b3 = ''
        self.b4 = False
        self.b5 = ''
        self.b6 = False
        self.b7 = False
        self.b8 = ''
        for arg in args:
            b10, b9 = arg.split('=')
            if b10 = = '--input':
                self.b8 = b9
            elif b10 = = '--b1':
                self.b1 = b9
            elif b10 = = '--b2':
                self.b2 = b9
            elif b10 = = '--b3':
                self.b3 = b9
            elif b10 = = '--b5':
                self.b5 = b9
        if not self.b8:
            raise ValueError('You must supply a b8 with --input')
        self.b6 = '-s' in args
        self.b4 = '-f' in args
        self.b7 = '-c' in args
    @property
    def fonk2(self):
        return self.b11
    @b8.setter
    def fonk3(self, b8):
        if not b8:
            raise ValueError('You must supply a b8')
        self.b11 = b8
    @property
    def fonk4(self):
        if self.b7 and self.b12 and not self.b12.endswith('.b7'):
            return self.b12 + '.b7'
        if not self.b7 and self.b12 and not self.b12.endswith('.json'):
            return self.b12 + '.json'
        return self.b12
    @b5.setter
    def fonk5(self, b5):
        self.b12 = b5
    @property
    def fonk6(self):
        return self.b13
    @b6.setter
    def fonk7(self, b6):
        self.b13 = bool(b6)
        if self.b13:
            self.b14 = False
    @property
    def fonk8(self):
        return self.b14
    @b4.setter
    def fonk9(self, b4):
        self.b14 = bool(b4)
        if self.b14:
            self.b13 = False
    @property
    def fonk10(self):
        return self.b15
    @b7.setter
    def fonk11(self, b7):
        self.b15 = bool(b7)
        if self.b15:
            self.b14 = False
    def fonk12(self):
        return {
            "b8": self.b8,
            "b1": self.b1,
            "b2": self.b2,
            "b3": self.b3,
            "b4": self.b4,
            "b5": self.b5,
            "b6": self.b6,
            "b7": self.b7,
        }
def fonk13(b16):
    b16 = b16.lower().replace('\n', '').strip("~`!@
    return b16.strip()