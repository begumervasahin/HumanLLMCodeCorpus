class class1:
    def fonk1(self, b2, b1 = None, b3=None, b4=0, b5=0, b6=None):
        self.b2 = b2
        self.b1 = b1
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = self.fonk2(b2)
    def fonk2(self, b2):
        return ''.join(str(e) for e in b2) if b2 else ''
    def fonk3(self, other):
        if not isinstance(other, class1):
            return NotImplemented
        return self.b7 = = other.b7
    def fonk4(self, other):
        if not isinstance(other, class1):
            return NotImplemented
        return self.b7 < other.b7