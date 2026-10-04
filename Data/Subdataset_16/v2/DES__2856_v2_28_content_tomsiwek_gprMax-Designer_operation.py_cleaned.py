class class1:
    def fonk1(self, b1 = None, **kwargs):
        self.fonk2(b1, **kwargs)
    def fonk2(self, b1 = None, **kwargs):
        self.b1 = b1
        self.b2 = kwargs.get('b2', None)
        self.b3 = kwargs.get('b3', None)
def fonk3():
    class class2:
        def fonk4(self):
            return self.__class__.b6
    class class3(class2):
        pass
    class class4(class2):
        pass
    class class5(class2):
        pass
    class class6(class2):
        pass
    b4 = class3()
    b5 = class1(b1="create", b2=b4, b3=1)
    print(f"Operation Type: {b5.b1}")
    print(f"Shape: {b5.b2}")
    print(f"Shape Number: {b5.b3}")
if b6 = = "__main__":
    fonk3()