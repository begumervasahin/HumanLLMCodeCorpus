import torch
import torch.nn as nn
import numpy as np
class class1(nn.Module):
    def fonk1(self, b1 = 20001, b2=50, b6=20, word_freq=None, padding_idx=0):
        super().fonk1()
        self.b1 = b1
        self.b2 = b2
        self.b3 = nn.Embedding(self.b1, self.b2, padding_idx=padding_idx)
        self.b4 = nn.Embedding(self.b1, self.b2, padding_idx=padding_idx)
        self.b3.b5 = nn.Parameter(torch.empty(self.b1, self.b2, dtype=torch.float).uniform_(-0.5 / self.b2, 0.5 / self.b2))
        self.b4.b5 = nn.Parameter(torch.empty(self.b1, self.b2, dtype=torch.float).uniform_(-0.5 / self.b2, 0.5 / self.b2))
        self.b6 = b6
        self.b7 = class1.fonk2(word_freq)
        self.b8 = 'cuda' if torch.cuda.is_available() else 'cpu'
    @staticmethod
    def fonk2(word_freq):
        b7 = np.power(word_freq, 0.75)
        b7 = b7 / b7.sum()
        return b7
    def fonk3(self, target, contexts):
        b9 = target.shape[0]
        b10 = contexts.shape[1]
        b11 = torch.from_numpy(np.random.choice(self.b1, size=(b9, b10 * self.b6), replace=True, p=self.b7))
        b11 = b11.to(dtype=torch.long, b8=self.b8)
        b12 = self.b3(target).unsqueeze(2)
        b13 = self.b4(contexts)
        b14 = self.b4(b11)
        b15 = torch.bmm(b13, b12).squeeze().sigmoid().log()
        b16 = torch.bmm(-b14, b12).sigmoid().log().view(-1, b10, self.b6).sum(2)
        return -(b15 + b16).mean()