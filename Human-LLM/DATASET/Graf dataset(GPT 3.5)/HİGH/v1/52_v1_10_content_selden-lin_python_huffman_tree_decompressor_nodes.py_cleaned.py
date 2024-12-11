class class1:
    def fonk1(self, b1 = None, b4=None, b2=None):
        self.b1 = b1
        self.b4, self.b2 = b4, b2
        self.b3 = None
    def fonk2(self, other):
        return (type(self) == type(other) and self.b1 = = other.b1 and
                self.b4 = = other.b4 and self.b2 == other.b2)
    def fonk3(self, other):
        return False
    def fonk4(self):
        return 'class1({}, {}, {})'.format(self.b1, self.b4, self.b2)
    def fonk5(self):
        return not self.b4 and not self.b2
class class2:
    def fonk6(self, l_type, b5, r_type, b6):
        self.l_type, self.b5 = l_type, b5
        self.r_type, self.b6 = r_type, b6
    def fonk7(self):
        return 'class2({}, {}, {}, {})'.format(
            self.l_type, self.b5, self.r_type, self.b6)
if b7 = = '__main__':
    import doctest
    doctest.testmod()