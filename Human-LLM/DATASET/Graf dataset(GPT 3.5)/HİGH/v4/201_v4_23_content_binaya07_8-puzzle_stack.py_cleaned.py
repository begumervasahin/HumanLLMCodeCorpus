class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = set()
    def fonk2(self, item):
        self.b1.append(item)
        self.b2.add(tuple(item.b1))
    def fonk3(self):
        if not self.fonk4():
            b3 = self.b1[-1]
            del self.b1[-1]
            self.b2.remove(tuple(b3.b1))
            return b3
        else:
            return 0
    def fonk4(self):
        return len(self.b1) == 0
    def fonk5(self):
        self.b1.clear()
        self.b2.clear()
