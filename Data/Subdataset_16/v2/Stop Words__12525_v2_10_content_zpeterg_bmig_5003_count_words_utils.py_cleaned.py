class class1:
    def fonk1(self, args):
        self.b1 = ''
        self.b2 = ''
        self.b3 = ''
        self.b4 = False
        self.b5 = ''
        self.b6 = False
        self.b7 = False
        for arg in args:
            b8 = arg.split('=')
            b9 = b8[0]
            b10 = b8[1] if len(b8) > 1 else None
            if b9 = = '--input' and b10:
                self.b11 = b10
            elif b9 = = '--b1':
                self.b1 = b10
            elif b9 = = '--b2':
                self.b2 = b10
            elif b9 = = '--b3':
                self.b3 = b10
            elif b9 = = '--b12':
                self.b12 = b10
        if not hasattr(self, 'b11'):
            raise ValueError('You must supply a b11 with --input')
        if '-s' in args:
            self.b13 = True
        elif '-f' in args:
            self.b14 = True
        if '-c' in args:
            self.b15 = True
    @property
    def fonk2(self):
        return self.b16
    @b11.setter
    def fonk3(self, b11):
        if not b11:
            raise ValueError('You must supply a b11')
        self.b16 = b11
    @property
    def fonk4(self):
        if self.b15 and self.b5 and not self.b5.endswith('.b15'):
            return self.b5 + '.b15'
        if not self.b15 and self.b5 and not self.b5.endswith('.json'):
            return self.b5 + '.json'
        return self.b5
    @b12.setter
    def fonk5(self, b12):
        self.b5 = b12
    @property
    def fonk6(self):
        return self.b6
    @b13.setter
    def fonk7(self, b13):
        self.b6 = bool(b13)
        if self.b6:
            self.b4 = False
    @property
    def fonk8(self):
        return self.b4
    @b14.setter
    def fonk9(self, format_flag):
        self.b4 = bool(format_flag)
    @property
    def fonk10(self):
        return self.b7
    @b15.setter
    def fonk11(self, csv_flag):
        self.b7 = bool(csv_flag)
        if self.b7:
            self.b4 = False
    def fonk12(self):
        return {
            "b11": self.b11,
            "b1": self.b1,
            "b2": self.b2,
            "b3": self.b3,
            "b14": self.b14,
            "b12": self.b12,
            "b13": self.b13,
            "b15": self.b15,
        }
def fonk13(b17):
    b17 = b17.lower()
    b17 = b17.replace('\n', '')
    return b17.strip("~`!@
