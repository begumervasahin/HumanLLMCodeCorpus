class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b1 = b1 if b1 is not None else []
    def fonk2(self, item):
        self.b1.append(item)
    def fonk3(self):
        if not self.b2 and not self.b1:
            print("Both b2 and b1 heaps are empty!")
            return None
        if not self.b2:
            return self.b1.pop(0)
        if not self.b1:
            return self.b2.pop(0)
        if self.b2[0].get_freq() <= self.b1[0].get_freq():
            return self.b2.pop(0)
        else:
            return self.b1.pop(0)