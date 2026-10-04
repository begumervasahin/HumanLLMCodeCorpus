class class1:
    def fonk1(self, args):
        self.b1 = ''
        self.b2 = ''
        self.b3 = ''
        self.b4 = False
        self.b5 = ''
        self.b6 = False
        self.b7 = False
        self.fonk2(args)
    def fonk2(self, args):
        for arg in args:
            b9, b8 = (arg.split('=') + [None])[:2]
            if b9 = = '--input' and b8:
                self.b10 = b8
            elif b9 = = '--b1':
                self.b1 = b8
            elif b9 = = '--b2':
                self.b2 = b8
            elif b9 = = '--b3':
                self.b3 = b8
            elif b9 = = '--b11':
                self.b11 = b8
        if not hasattr(self, 'b10'):
            raise ValueError('You must supply a b10 with --input')
        self.b12 = '-s' in args
        self.b13 = '-f' in args
        self.b14 = '-c' in args
    @property
    def fonk3(self):
        return self.b15
    @b10.setter
    def fonk4(self, b10):
        if not b10:
            raise ValueError('You must supply a b10')
        self.b15 = b10
    @property
    def fonk5(self):
        if self.b14 and self.b5 and not self.b5.endswith('.b14'):
            return self.b5 + '.b14'
        if not self.b14 and self.b5 and not self.b5.endswith('.json'):
            return self.b5 + '.json'
        return self.b5
    @b11.setter
    def fonk6(self, b11):
        self.b5 = b11
    @property
    def fonk7(self):
        return self.b6
    @b12.setter
    def fonk8(self, b12):
        self.b6 = bool(b12)
        if self.b6:
            self.b4 = False
    @property
    def fonk9(self):
        return self.b4
    @b13.setter
    def fonk10(self, format_flag):
        self.b4 = bool(format_flag)
    @property
    def fonk11(self):
        return self.b7
    @b14.setter
    def fonk12(self, csv_flag):
        self.b7 = bool(csv_flag)
        if self.b7:
            self.b4 = False
    def fonk13(self):
        return {
            "b10": self.b10,
            "b1": self.b1,
            "b2": self.b2,
            "b3": self.b3,
            "b13": self.b13,
            "b11": self.b11,
            "b12": self.b12,
            "b14": self.b14,
        }
def fonk14(word):
    return word.lower().replace('\n', '').strip("~`!@
