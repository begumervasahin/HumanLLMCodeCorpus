class class1:
    def fonk1(self, b2, b3, b4, b5, b1 = 0):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b1
    def fonk2(self):
        self.b6 += 1
        if self.b6 < self.b5:
            b7 = self.fonk3()
        else:
            b7 = self.fonk4()
        self.fonk5(b7)
        return b7
    def fonk3(self):
        return self.b3 ** (-0.5) * self.b6 * self.b5 ** (-1.5) * self.b4
    def fonk4(self):
        return 0.5 * self.b3 ** (-0.5) * self.b6 ** (-0.5) * self.b4
    def fonk5(self, b7):
        for optimizer in self.b2:
            for param_group in optimizer.param_groups:
                param_group["lr"] = b7