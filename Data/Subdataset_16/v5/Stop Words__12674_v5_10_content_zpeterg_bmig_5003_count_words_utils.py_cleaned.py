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
        self.fonk2(args)
        self.fonk5()
    def fonk2(self, args):
        for arg in args:
            if '=' in arg:
                b10, b9 = arg.split('=')
                self.fonk3(b10, b9)
            else:
                self.fonk4(arg)
    def fonk3(self, b10, b9):
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
    def fonk4(self, b11):
        if b11 = = '-s':
            self.b6 = True
        elif b11 = = '-f':
            self.b4 = True
        elif b11 = = '-c':
            self.b7 = True
    def fonk5(self):
        if not self.b8:
            raise ValueError('You must supply a b8 with --input')
    @property
    def fonk6(self):
        return self.b12
    @b8.setter
    def fonk7(self, b8):
        if not b8:
            raise ValueError('You must supply a b8')
        self.b12 = b8
    @property
    def fonk8(self):
        if self.b7 and self.b13 and not self.b13.endswith('.b7'):
            return self.b13 + '.b7'
        if not self.b7 and self.b13 and not self.b13.endswith('.json'):
            return self.b13 + '.json'
        return self.b13
    @b5.setter
    def fonk9(self, b5):
        self.b13 = b5
    @property
    def fonk10(self):
        return self.b14
    @b6.setter
    def fonk11(self, b6):
        self.b14 = bool(b6)
        if self.b14:
            self.b15 = False
    @property
    def fonk12(self):
        return self.b15
    @b4.setter
    def fonk13(self, b4):
        self.b15 = bool(b4)
        if self.b15:
            self.b14 = False
    @property
    def fonk14(self):
        return self.b16
    @b7.setter
    def fonk15(self, b7):
        self.b16 = bool(b7)
        if self.b16:
            self.b15 = False
    def fonk16(self):
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
def fonk17(word):
    return word.lower().replace('\n', '').strip("~`!@
