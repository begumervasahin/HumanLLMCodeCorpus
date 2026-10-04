import torch
import torch.nn as nn
import numpy as np
class class1(nn.Module):
    def fonk1(self, b1 = 20001, b2=50, b3=20, b21=None, padding_idx=0):
        super(class1, self).fonk1()
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = nn.Embedding(self.b1, self.b2, padding_idx=padding_idx)
        self.b5 = nn.Embedding(self.b1, self.b2, padding_idx=padding_idx)
        self.b4.b6 = nn.Parameter(
            torch.empty(self.b1, self.b2, b7 = torch.float).uniform_(-0.5 / self.b2, 0.5 / self.b2)
        )
        self.b5.b6 = nn.Parameter(
            torch.empty(self.b1, self.b2, b7 = torch.float).uniform_(-0.5 / self.b2, 0.5 / self.b2)
        )
        self.b8 = self.fonk2(b21)
        self.b9 = 'cuda' if torch.cuda.is_available() else 'cpu'
    @staticmethod
    def fonk2(b21):
        b8 = np.power(b21, 0.75)
        b8 = b8 / b8.sum()
        return b8
    def fonk3(self, b23, b24):
        b10 = b23.shape[0]
        b11 = b24.shape[1]
        b12 = torch.from_numpy(
            np.random.choice(self.b1, b13 = (b10, b11 * self.b3), replace=True, p=self.b8)
        )
        b12 = b12.to(b7=torch.long, b9=self.b9)
        b14 = self.b4(b23).unsqueeze(2)
        b15 = self.b5(b24)
        b16 = self.b5(b12)
        b17 = torch.bmm(b15, b14).squeeze().sigmoid().log()
        b18 = torch.bmm(-b16, b14).sigmoid().log().view(-1, b11, self.b3).sum(2)
        b19 = -(b17 + b18).mean()
        return b19
if b20 = = "__main__":
    b21 = np.array([1, 2, 3, 4, 5])
    b21 = b21 / b21.sum()
    b22 = class1(b1=6, b2=10, b3=5, b21=b21)
    b23 = torch.tensor([1, 2, 3])
    b24 = torch.tensor([[2, 3], [3, 4], [4, 5]])
    b19 = b22(b23, b24)
    print("Loss:", b19.item())