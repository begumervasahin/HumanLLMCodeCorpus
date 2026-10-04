class class1:
    def fonk1(self, iFrom, iTo, iRate):
        self.b1 = iFrom
        self.b2 = iTo
        self.b3 = float(iRate)
    def fonk2(self):
        return self.b1 + "->" + self.b2 + ": " + self.b3
    def fonk3(self):
        return self.fonk2()
    @property
    def fonk4(self):
        return self.b1
    @property
    def fonk5(self):
        return self.b2
    @property
    def fonk6(self):
        return self.b3