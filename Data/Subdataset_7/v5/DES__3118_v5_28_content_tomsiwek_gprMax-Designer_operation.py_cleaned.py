class class1:
    def fonk1(self, b1 = None, **kwargs):
        self.fonk2(b1, **kwargs)
    def fonk2(self, b1 = None, **kwargs):
        self.b1 = b1
        self.b2 = kwargs.pop('b2', None)
        self.b3 = kwargs.pop('b3', None)