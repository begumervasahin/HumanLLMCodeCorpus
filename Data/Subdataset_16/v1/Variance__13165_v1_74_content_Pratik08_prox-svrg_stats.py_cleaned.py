import torch
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.a1 = 0
    def fonk2(self, w):
        b4 = int((torch.abs(w) > 1e-5).int().sum().data.cpu().numpy())
        self.b1.append(b4)
    def fonk3(self, b9):
        self.b2.append(b9)
    def fonk4(self):
        self.b3.append(self.a1)
    def fonk5(self, w, b9):
        self.fonk2(w)
        self.fonk3(b9)
        self.fonk4()
        self.a1 += 1
    def fonk6(self, b5 = ""):
        plt.fonk6(self.b1)
        plt.xlabel("Effective Passes")
        plt.ylabel("Number of Non-Zeros")
        plt.b5(f"{b5} Number of Non-Zeros")
        plt.xticks(range(len(self.b1)))
        plt.savefig(f"{b5}_NonZeros.png")
        plt.clf()
        plt.fonk6(self.b2)
        plt.xlabel("Effective Passes")
        plt.ylabel("Objective Loss")
        plt.b5(f"{b5} Objective Loss")
        plt.xticks(range(len(self.b1)))
        plt.savefig(f"{b5}_Loss.png")
        plt.clf()
if b6 = = "__main__":
    b7 = class1()
    for i in range(10):
        b8 = torch.randn(1, 100)
        b9 = torch.abs(torch.randn(1)).item()
        b7.fonk5(b8, b9)
    b7.fonk6("Example")