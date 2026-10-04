import torch
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.a1 = 0
    def fonk2(self, b10):
        b4 = (torch.abs(b10) > 1e-5).int().sum().item()
        self.b1.append(b4)
    def fonk3(self, b11):
        self.b2.append(b11)
    def fonk4(self):
        self.b3.append(self.a1)
    def fonk5(self, b10, b11):
        self.fonk2(b10)
        self.fonk3(b11)
        self.fonk4()
        self.a1 += 1
    def fonk6(self, b5 = ""):
        self.fonk7(self.b1, "Number of Non-Zeros", b5, "NonZeros")
        self.fonk7(self.b2, "Objective Loss", b5, "Loss", b6 = 'r')
    def fonk7(self, data, ylabel, b5, filename_suffix, b6 = 'b'):
        plt.figure()
        plt.fonk6(data, b7 = 'o', b6=b6)
        plt.xlabel("Effective Passes")
        plt.ylabel(ylabel)
        plt.b5(f"{b5} {ylabel}")
        plt.xticks(range(len(data)))
        plt.grid(True)
        plt.savefig(f"{b5}_{filename_suffix}.png")
        plt.close()
if b8 = = "__main__":
    b9 = class1()
    for _ in range(10):
        b10 = torch.randn(1, 100)
        b11 = torch.abs(torch.randn(1)).item()
        b9.fonk5(b10, b11)
    b9.fonk6("Example")