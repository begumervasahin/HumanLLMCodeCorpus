class class1:
    class class2:
        def fonk1(self, b1, b2):
            self.b1 = b1
            self.b2 = b2
            self.b3 = None
            self.b4 = None
    def fonk2(self):
        self.b5 = None
        self.a1 = 0
        self.b6 = None
        self.b7 = "pre"
    def fonk3(self, b1, b2):
        self.b5 = self.fonk10(self.b5, b1, b2)
        self.a1 += 1
    def fonk4(self, b1):
        return self.fonk11(self.b5, b1)
    def fonk5(self, b1):
        self.b6 = None
        self.b5 = self.fonk12(self.b5, b1)
        return self.b6
    def fonk6(self):
        self.b7 = "pre"
        return self
    def fonk7(self):
        self.b7 = "in"
        return self
    def fonk8(self):
        self.b7 = "post"
        return self
    def fonk9(self):
        return self.fonk13(self.b5)
    def fonk10(self, r, b8, v):
        if not r:
            return class1.class2(b8, v)
        if b8 < r.b1:
            r.b3 = self.fonk10(r.b3, b8, v)
        else:
            r.b4 = self.fonk10(r.b4, b8, v)
        return r
    def fonk11(self, r, b8):
        if not r:
            return None
        if b8 = = r.b1:
            return r.b2
        if b8 < r.b1:
            return self.fonk11(r.b3, b8)
        else:
            return self.fonk11(r.b4, b8)
    def fonk12(self, r, b8):
        if not r:
            return None
        if b8 = = r.b1:
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
            b9 = self._minimum(r.b4)
            b10 = r.b2
            r.b1 = b9.b1
            r.b2 = b9.b2
            r.b4 = self.fonk12(r.b4, b9.b1)
            self.b6 = b10
            return r
        if b8 < r.b1:
            r.b3 = self.fonk12(r.b3, b8)
        else:
            r.b4 = self.fonk12(r.b4, b8)
        return r
    def fonk13(self, r):
        if self.b7 = = "pre":
            yield r.b2
        if r.b3:
            for el in self.fonk13(r.b3):
                yield el
        if self.b7 = = "in":
            yield r.b2
        if r.b4:
            for el in self.fonk13(r.b4):
                yield el
        if self.b7 = = "post":
            yield r.b2
    def fonk14(self):
        return self.a1