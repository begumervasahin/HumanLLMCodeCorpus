import torch
import torch.optim as optim
class class1:
    def fonk1(self, b2, b3, b4, b5, b1 = 0):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b1
    def fonk2(self):
        self.b6 += 1
        b7 = self.fonk3()
        self.fonk4(b7)
        return b7
    def fonk3(self):
        if self.b6 < self.b5:
            return (self.b3 ** -0.5) * (self.b6 * self.b5 ** -1.5) * self.b4
        else:
            return 0.5 * (self.b3 ** -0.5) * (self.b6 ** -0.5) * self.b4
    def fonk4(self, b7):
        for optimizer in self.b2:
            for param_group in optimizer.param_groups:
                param_group["lr"] = b7
if b8 = = "__main__":
    b9 = [torch.nn.Parameter(torch.randn(2, 2, requires_grad=True))]
    b10 = optim.SGD(b9, lr=0.01)
    b11 = optim.Adam(b9, lr=0.01)
    b2 = [b10, b11]
    b3 = 512
    b4 = 0.001
    b5 = 1000
    b1 = 0
    b12 = class1(b2, b3, b4, b5, b1)
    for _ in range(10):
        b13 = b12.fonk2()
        print(f"Current learning rate: {b13}")
        for optimizer in b2:
            optimizer.b6()