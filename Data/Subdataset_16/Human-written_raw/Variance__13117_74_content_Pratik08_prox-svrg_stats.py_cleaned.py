import torch
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.a1 = 0
    def fonk2(self, w):
        self.b1.append(int((torch.abs(w) > 1e-5).int().sum().data.cpu().numpy()))
    def fonk3(self, loss):
        self.b2.append(loss)
    def fonk4(self):
        self.b3.append(self.a1)
    def fonk5(self, w, loss):
        self.fonk2(w)
        self.fonk3(loss)
        self.fonk4()
        self.a1 += 1
    def fonk6(self,b4 = ""):
        plt.fonk6(self.b1)
        plt.xlabel("Effective Passes")
        plt.ylabel("NNZs")
        plt.b4(b4+" NNZs")
        plt.xticks(range(len(self.b1)))
        plt.savefig(b4+"_NNZs.png")
        plt.clf()
        plt.fonk6(self.b2)
        plt.xlabel("Effective Passes")
        plt.ylabel("Objective Loss")
        plt.b4(b4+" Loss")
        plt.xticks(range(len(self.b1)))
        plt.savefig(b4+"_Loss.png")
        plt.clf()