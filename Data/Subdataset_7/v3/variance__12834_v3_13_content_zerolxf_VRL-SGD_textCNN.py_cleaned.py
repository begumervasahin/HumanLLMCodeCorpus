import torch
import torch.nn as nn
import torch.nn.functional as F
class class1(nn.Module):
    def fonk1(self, b3, b1 = 50, b2=50, b4=100, b5=[3,4,5], b9=0.5):
        super(class1, self).fonk1()
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b9
        self.b7 = nn.ModuleList([
            nn.Conv2d(b8 = 1, out_channels=self.b4, kernel_size=(K, self.b2)) for K in self.b5
        ])
        self.b9 = nn.Dropout(p=self.b6)
        self.b10 = nn.Linear(len(self.b5) * self.b4, self.b3)
    def fonk2(self, b11):
        b11 = b11.unsqueeze(1)
        b12 = [F.relu(conv(b11)).squeeze(3) for conv in self.b7]
        b13 = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in b12]
        b11 = torch.cat(b13, 1)
        b11 = self.b9(b11)
        b14 = self.b10(b11)
        return b14
b15 = class1(b3=10, b1=50, b2=50, b4=100, b5=[3, 4, 5], b9=0.5)
b16 = torch.randn(32, 50)
b17 = b15(b16)
print(b17.shape)
