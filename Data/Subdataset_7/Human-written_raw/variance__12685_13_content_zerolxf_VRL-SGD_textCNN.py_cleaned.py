import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
class class1(nn.Module):
    def fonk1(self, class_num, b1 = 50, embed_dim=50, kernel_num=100, kernel_sizes=[3,4,5], b11=0.5):
        super(class1, self).fonk1()
        b2 = b1
        b3 = embed_dim
        b4 = class_num
        a1 = 1
        b5 = kernel_num
        b6 = kernel_sizes
        self.b7 = nn.ModuleList([nn.Conv2d(a1, b5, (K, b3)) for K in b6])
        '''
        self.b8 = nn.Conv2d(a1, b5, (3, b3))
        self.b9 = nn.Conv2d(a1, b5, (4, b3))
        self.b10 = nn.Conv2d(a1, b5, (5, b3))
        '''
        self.b11 = nn.Dropout(b11)
        self.b12 = nn.Linear(len(b6)*b5, b4)
    def fonk2(self, b13, conv):
        b13 = F.relu(conv(b13)).squeeze(3)
        b13 = F.max_pool1d(b13, b13.size(2)).squeeze(2)
        return b13
    def fonk3(self, b13):
        b13 = b13.unsqueeze(1)
        b13 = [F.relu(conv(b13)).squeeze(3) for conv in self.b7]
        b13 = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in b13]
        b13 = torch.cat(b13, 1)
        '''
        b14 = self.fonk2(b13,self.b8)
        b15 = self.fonk2(b13,self.b9)
        b16 = self.fonk2(b13,self.b10)
        b13 = torch.cat((b14, b15, b16), 1)
        '''
        b13 = self.b11(b13)
        b17 = self.b12(b13)
        return b17