class class1:
    def fonk1(self, b1 = None, **kwargs):
        self.fonk2(b1, **kwargs)
    def fonk2(self, b1 = None, **kwargs):
        self.b1 = b1
        self.b2 = kwargs.pop('b2', None)
        self.b3 = kwargs.pop('b3', None)
if b4 = = "__main__":
    class class2:
        pass
    class class3(class2):
        pass
    class class4(class2):
        pass
    class class5(class2):
        pass
    class class6(class2):
        pass
    b5 = class3()
    b6 = class1(b1="create", b2=b5, b3=1)
    print(f"Operation Type: {b6.b1}")
    print(f"Shape: {b6.b2}")
    print(f"Shape Number: {b6.b3}")