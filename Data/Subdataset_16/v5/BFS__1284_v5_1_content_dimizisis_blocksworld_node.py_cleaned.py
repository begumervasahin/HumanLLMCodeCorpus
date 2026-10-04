class class1:
    def fonk1(self, b1 = None, b2=None, b3=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, other):
        if self.b3 is None or other.b3 is None:
            raise ValueError("Priority values must be set for comparison.")
        return self.b3 < other.b3