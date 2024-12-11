class class1:
    def fonk1(self, b2, a1, b4, b5, b1 = 0):
        self.b2 = b2
        self.b3 = a1
        self.b4 = b4
        self.b5 = b5
        self.b6 = b1
    def fonk2(self):
        self.b6 += 1
        if self.b6 < self.b5:
            b7 = self.b3 ** (-0.5) * self.b6 * self.b5 ** (-1.5) * self.b4
        else:
            b7 = 0.5 * self.b3 ** (-0.5) * self.b6 ** (-0.5) * self.b4
        for optimizer in self.b2:
            for param_group in optimizer.param_groups:
                param_group["lr"] = b7
        return b7
b2 = [optimizer1, optimizer2]
a1 = 512
b4 = 0.001
b5 = 1000
b1 = 0
b8 = class1(b2, a1, b4, b5, b1)
b9 = b8()
print("Current learning rate:", b9)