class class1:
    def fonk1(self, b1 = None, **kwargs):
        self.fonk2(b1, **kwargs)
    def fonk2(self, b1 = None, **kwargs):
        self.b2 = b1
        self.b3 = kwargs.pop('b3', None)
        self.b4 = kwargs.pop('b4', None)