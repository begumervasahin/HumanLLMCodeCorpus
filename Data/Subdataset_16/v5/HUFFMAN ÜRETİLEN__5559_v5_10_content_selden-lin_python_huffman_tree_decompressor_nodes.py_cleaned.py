class class1:
    def fonk1(self, b1 = None, b2=None, b3=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = None
    def fonk2(self, other):
        if not isinstance(other, class1):
            return False
        return (
            self.b1 = = other.b1 and
            self.b2 = = other.b2 and
            self.b3 = = other.b3
        )
    def fonk3(self, other):
        return False
    def fonk4(self):
        return (
            f"class1(b1 = {self.b1}, "
            f"b2 = {self.b2}, b3={self.b3})"
        )
    def fonk5(self):
        return self.b2 is None and self.b3 is None
class class2:
    def fonk6(self, b5, b6, b7, b8):
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
    def fonk7(self):
        return (
            f"class2(b5 = {self.b5}, b6={self.b6}, "
            f"b7 = {self.b7}, b8={self.b8})"
        )
if b9 = = '__main__':
    import doctest
    doctest.testmod()