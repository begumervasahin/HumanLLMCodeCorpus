class class1:
    def fonk1(self, b2, b3, b4, b1 = None):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b1 = b1 if b1 is not None else []
    def fonk2(self, other):
        if not isinstance(other, class1):
            return False
        return (
            self.b2 = = other.b2 and
            self.b3 = = other.b3 and
            self.b4 = = other.b4
        )