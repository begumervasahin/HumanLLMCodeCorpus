import torch
import torch.nn as nn
import torch.nn.functional as F
class class1(nn.Module):
    def fonk1(self, b3, b1 = 50, b2=50, b4=100, b5=[3,4,5], b8=0.5):
        super(class1, self).fonk1()
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b8
        self.b7 = nn.ModuleList([nn.Conv2d(in_channels=1, out_channels=self.b4, kernel_size=(K, self.b2)) for K in self.b5])
        self.b8 = nn.Dropout(p=self.b6)
        self.b9 = nn.Linear(len(self.b5) * self.b4, self.b3)
    def fonk2(self, b10):
        b10 = b10.unsqueeze(1)
        b11 = [F.relu(conv(b10)).squeeze(3) for conv in self.b7]
        b12 = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in b11]
        b10 = torch.cat(b12, 1)
        b10 = self.b8(b10)
        b13 = self.b9(b10)
        return b13
b14 = class1(b3=10, b1=50, b2=50, b4=100, b5=[3, 4, 5], b8=0.5)
b15 = torch.randn(32, 50)
b16 = b14(b15)
print(b16.shape)
