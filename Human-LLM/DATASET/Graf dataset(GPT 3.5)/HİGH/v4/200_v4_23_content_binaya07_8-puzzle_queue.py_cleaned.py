class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = set()
    def fonk2(self, b3):
        self.b1.append(b3)
        self.b2.add(tuple(b3.list))
    def fonk3(self):
        if not self.fonk4():
            b3 = self.b1.pop(0)
            self.b2.remove(tuple(b3.list))
            return b3
    def fonk4(self):
        return len(self.b1) == 0