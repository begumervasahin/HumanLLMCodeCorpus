class class1(object):
    def fonk1(self, b1 = None, **kwargs):
        self.fonk2(b1, **kwargs)
    def fonk2(self, b1 = None, **kwargs):
        self.b1 = b1
        self.b2 = kwargs.pop('b2', None)
        self.b3 = kwargs.pop('b3', None)
b4 = class1(b1="resize", b2="rectangle", b3=1)
print("Operation Type:", b4.b1)
print("Shape:", b4.b2)
print("Number:", b4.b3)