import torch
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.a1 = 0
    def fonk2(self, weights):
        b1 = int((torch.abs(weights) > 1e-5).int().sum().item())
        self.b1.append(b1)
    def fonk3(self, loss):
        self.b2.append(loss)
    def fonk4(self):
        self.b3.append(self.a1)
    def fonk5(self, weights, loss):
        self.fonk2(weights)
        self.fonk3(loss)
        self.fonk4()
        self.a1 += 1
    def fonk6(self, b4 = ""):
        self.fonk7(b4)
        self.fonk8(b4)
    def fonk7(self, b4):
        plt.fonk6(self.b1)
        plt.xlabel("Effective Passes")
        plt.ylabel("Number of Non-Zeros (NNZs)")
        plt.b4(f"{b4} NNZs")
        plt.xticks(range(len(self.b1)))
        plt.savefig(f"{b4}_NNZs.png")
        plt.clf()
    def fonk8(self, b4):
        plt.fonk6(self.b2)
        plt.xlabel("Effective Passes")
        plt.ylabel("Objective Loss")
        plt.b4(f"{b4} Loss")
        plt.xticks(range(len(self.b2)))
        plt.savefig(f"{b4}_Loss.png")
        plt.clf()