class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b1 = b1
    def fonk2(self, b3):
        self.b1.append(b3)
    def fonk3(self):
        if len(self.b2) == 0 and len(self.b1) != 0:
            b3 = self.b1.pop(0)
        elif len(self.b1) == 0 and len(self.b2) != 0:
            b3 = self.b2.pop(0)
        elif len(self.b1) != 0 and len(self.b2) != 0:
            if self.b2[0].get_freq() >= self.b1[0].get_freq():
                b3 = self.b1.pop(0)
            else:
                b3 = self.b2.pop(0)
        else:
            print("Both b2 and b1 lists are empty!")
            return None
        return b3