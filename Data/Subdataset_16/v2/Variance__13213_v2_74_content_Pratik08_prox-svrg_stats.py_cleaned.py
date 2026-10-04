import torch
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.a1 = 0
    def fonk2(self, w):
        b4 = int((torch.abs(w) > 1e-5).int().sum().cpu().numpy())
        self.b1.append(b4)
    def fonk3(self, b10):
        self.b2.append(b10)
    def fonk4(self):
        self.b3.append(self.a1)
    def fonk5(self, w, b10):
        self.fonk2(w)
        self.fonk3(b10)
        self.fonk4()
        self.a1 += 1
    def fonk6(self, b5 = ""):
        plt.figure()
        plt.fonk6(self.b1, b6 = 'o')
        plt.xlabel("Effective Passes")
        plt.ylabel("Number of Non-Zeros")
        plt.b5(f"{b5} Number of Non-Zeros")
        plt.xticks(range(len(self.b1)))
        plt.grid(True)
        plt.savefig(f"{b5}_NonZeros.png")
        plt.close()
        plt.figure()
        plt.fonk6(self.b2, b6 = 'o', color='r')
        plt.xlabel("Effective Passes")
        plt.ylabel("Objective Loss")
        plt.b5(f"{b5} Objective Loss")
        plt.xticks(range(len(self.b2)))
        plt.grid(True)
        plt.savefig(f"{b5}_Loss.png")
        plt.close()
if b7 = = "__main__":
    b8 = class1()
    for _ in range(10):
        b9 = torch.randn(1, 100)
        b10 = torch.abs(torch.randn(1)).item()
        b8.fonk5(b9, b10)
    b8.fonk6("Example")