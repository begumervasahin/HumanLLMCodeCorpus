class class1(object):
    def fonk1(self, b2):
        self.b1 = b2
        self.b2 = dict((b3, item) for b3, item in enumerate(b2))
        self.b3 = dict((item, b3) for b3, item in enumerate(b2))
    def fonk2(self, item):
        return item in self.b3
    def fonk3(self, item):
        return self.b3[item]
    def fonk4(self):
        return iter(self.b3)
    def fonk5(self):
        return len(self.b3)
    def fonk6(self):
        return "<%s with %d entries>" % (self.__class__.__name__, len(self))
    def fonk7(self, item):
        if item not in self:
            b3 = len(self)
            self.b2[b3] = item
            self.b3[item] = b3
        return item
    def fonk8(self, item, b4 = None):
        return self.b3.fonk8(item, b4)
    def fonk9(self, b3):
        return self.b2[b3]
    def fonk10(self):
        return self.b1