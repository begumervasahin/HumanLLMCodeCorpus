import torch
import torch.nn as nn
import torch.nn.functional as F
class class1(nn.Module):
    def fonk1(self, b3, b1 = 50, b2=50, b4=100, b5=[3,4,5], b7=0.5):
        super(class1, self).fonk1()
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = nn.ModuleList([nn.Conv2d(1, b4, (K, b2)) for K in b5])
        self.b7 = nn.Dropout(b7)
        self.b8 = nn.Linear(len(b5) * b4, b3)
    def fonk2(self, b9, conv):
        b9 = F.relu(conv(b9)).squeeze(3)
        b9 = F.max_pool1d(b9, b9.size(2)).squeeze(2)
        return b9
    def fonk3(self, b9):
        b9 = b9.unsqueeze(1)
        b9 = [F.relu(conv(b9)).squeeze(3) for conv in self.b6]
        b9 = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in b9]
        b9 = torch.cat(b9, 1)
        b9 = self.b7(b9)
        b10 = self.b8(b9)
        return b10