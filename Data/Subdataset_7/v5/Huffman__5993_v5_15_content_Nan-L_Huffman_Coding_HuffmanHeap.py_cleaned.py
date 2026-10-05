class class1:
    def fonk1(self, b1 = None, b2=None):
        self.b1 = b1 or []
        self.b2 = b2 or []
    def fonk2(self, item):
        self.b2.append(item)
    def fonk3(self):
        if not self.b1 and not self.b2:
            print("Both b1 and b2 lists are empty!")
            return None
        if not self.b1:
            return self.b2.pop(0)
        if not self.b2:
            return self.b1.pop(0)
        if self.b1[0].get_freq() >= self.b2[0].get_freq():
            return self.b2.pop(0)
        else:
            return self.b1.pop(0)