class class1(object):
    class class2(object):
        def fonk1(self, key, value):
            self.b1 = key
            self.b2 = value
            self.b3 = None
            self.b4 = None
    def fonk2(self):
        self.fonk3()
    def fonk3(self):
        self.b5 = None
        self.a1 = 0
        self.b6 = None
        self.b7 = "pre"
    def fonk4(self, r, b9, v):
        if not r:
            b8 = class1.class2(b9,v)
            return b8
        if b9 < r.b1:
            r.b3 = self.fonk4(r.b3, b9, v)
        else:
            r.b4 = self.fonk4(r.b4, b9, v)
        return r
    def fonk5(self, key, value):
        self.b5 = self.fonk4(self.b5, key, value)
        self.a1 += 1
    def fonk6(self, r, b9):
        if not r:
            return None
        if b9 = = r.b1:
            return r.b2
        if b9 < r.b1:
            return self.fonk6(r.b3, b9)
        else:
            return self.fonk6(r.b4, b9)
    def fonk7(self, key):
        return self.fonk6(self.b5, key)
    def fonk8(self, r, b9):
        if not r:
            return None
        if b9 = = r.b1:
            if not r.b3 and not r.b4:
                self.b6 = r.b2
                self.a1 -= 1
                return None
            if not r.b4:
                self.b6 = r.b2
                self.a1 -= 1
                return r.b3
            if not r.b3:
                self.b6 = r.b2
                self.a1 -= 1
                return r.b4
            b10 = self._minimum(r.b4)
            b11 = r.b2
            r.b1 = b10.b1
            r.b2 = b10.b2
            r.b4 = self.fonk8(r.b4, b10.b1)
            self.b6 = b11
            return r
        if b9 < r.b1:
            r.b3 = self.fonk8(r.b3, b9)
        else:
            r.b4 = self.fonk8(r.b4, b9)
        return r
    def fonk9(self, key):
        self.b6 = None
        self.b5 = self.fonk8(self.b5, key)
        return self.b6
    def fonk10(self):
        self.b7 = "pre"
        return self
    def fonk11(self):
        self.b7 = "in"
        return self
    def fonk12(self):
        self.b7 = "post"
        return self
    def fonk13(self):
        return self.fonk14(self.b5)
    def fonk14(self, r):
        if self.b7 = = "pre":
            yield r.b2
        if r.b3:
            for el in self.fonk14(r.b3):
                yield el
        if self.b7 = = "in":
            yield r.b2
        if r.b4:
            for el in self.fonk14(r.b4):
                yield el
        if self.b7 = = "post":
            yield r.b2
    def fonk15(self):
        return self.a1