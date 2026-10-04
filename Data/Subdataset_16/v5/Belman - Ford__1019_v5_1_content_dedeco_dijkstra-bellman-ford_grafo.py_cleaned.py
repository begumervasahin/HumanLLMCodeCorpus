class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = {}
        self.b3 = float('inf')
        self.b4 = False
    def fonk2(self, neighbor, b5 = 0):
        self.b2[neighbor] = b5
    def fonk3(self):
        return self.b2.keys()
    def fonk4(self):
        return self.b1
    def fonk5(self, neighbor):
        return self.b2[neighbor]
    def fonk6(self, b3):
        self.b3 = b3
    def fonk7(self):
        return self.b3
    def fonk8(self, b4 = True):
        self.b4 = b4
    def fonk9(self):
        return self.b4