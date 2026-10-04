class class1:
    def fonk1(self, args):
        self.b1 = ''
        self.b2 = ''
        self.b3 = ''
        self.b4 = False
        self.b5 = ''
        self.b6 = False
        self.b7 = False
        for b8 in args:
            b8 = b8.split('=')
            if b8[0] == '--input':
                self.b9 = b8[1]
            elif b8[0] == '--b1':
                self.b1 = b8[1]
            elif b8[0] == '--b2':
                self.b2 = b8[1]
            elif b8[0] == '--b3':
                self.b3 = b8[1]
            elif b8[0] == '--b5':
                self.b5 = b8[1]
        if not hasattr(self, 'b9'):
            raise ValueError('You must supply b8 b9 with --input')
        if '-s' in args:
            self.b6 = True
        elif '-f' in args:
            self.b4 = True
        if '-c' in args:
            self.b7 = True
    @property
    def fonk2(self):
        return self.b10
    @b9.setter
    def fonk3(self, b9):
        if b9 = = '':
            raise ValueError('You must supply b8 b9')
        self.b10 = b9
    @property
    def fonk4(self):
        if self.b7 and self.b11 and self.b11[-4:] != '.b7':
            return self.b11 + '.b7'
        if not self.b7 and self.b11 and self.b11[-5:] != '.json':
            return self.b11 + '.json'
        return self.b11
    @b5.setter
    def fonk5(self, b5):
        self.b11 = b5
    @property
    def fonk6(self):
        return self.b13
    @b6.setter
    def fonk7(self, b6):
        if not isinstance(b6, bool):
            b6 = False
        if b6:
            self.b12 = False
        self.b13 = b6
    @property
    def fonk8(self):
        return self.b12
    @b4.setter
    def fonk9(self, b14):
        if not isinstance(b14, bool):
            b14 = False
        self.b12 = b14
    @property
    def fonk10(self):
        return self.b15
    @b7.setter
    def fonk11(self, b7):
        if not isinstance(b7, bool):
            b7 = False
        if b7:
            self.b12 = False
        self.b15 = b7
    def fonk12(self):
        return {
            "b9": self.b9,
            "b1": self.b1,
            "b2": self.b2,
            "b3": self.b3,
            "b4": self.b4,
            "b5": self.b5,
            "b6": self.b6,
            "b7": self.b7,
        }
def fonk13(b16):
    b16 = b16.lower()
    b16 = b16.replace('\n', '')
    return b16.strip("~`!@