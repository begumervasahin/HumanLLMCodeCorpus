import torch
import torch.nn as nn
import torch.nn.functional as F
class class1(nn.Module):
    def fonk1(self, class_num, b1 = 50, embed_dim=50, kernel_num=100, kernel_sizes=[3,4,5], b8=0.5):
        super(class1, self).fonk1()
        b2 = b1
        b3 = embed_dim
        b4 = class_num
        a1 = 1
        b5 = kernel_num
        b6 = kernel_sizes
        self.b7 = nn.ModuleList([nn.Conv2d(a1, b5, (K, b3)) for K in b6])
        self.b8 = nn.Dropout(b8)
        self.b9 = nn.Linear(len(b6)*b5, b4)
    def fonk2(self, b10, conv):
        b10 = F.relu(conv(b10)).squeeze(3)
        b10 = F.max_pool1d(b10, b10.size(2)).squeeze(2)
        return b10
    def fonk3(self, b10):
        b10 = b10.unsqueeze(1)
        b10 = [F.relu(conv(b10)).squeeze(3) for conv in self.b7]
        b10 = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in b10]
        b10 = torch.cat(b10, 1)
        b10 = self.b8(b10)
        b11 = self.b9(b10)
        return b11
b12 = class1(class_num=10, b1=50, embed_dim=50, kernel_num=100, kernel_sizes=[3, 4, 5], b8=0.5)
b13 = torch.randn(32, 50)
b14 = b12(b13)
print(b14.shape)
