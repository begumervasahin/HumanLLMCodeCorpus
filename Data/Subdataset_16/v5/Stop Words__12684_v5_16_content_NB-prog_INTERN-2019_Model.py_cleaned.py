import torch
import torch.nn as nn
import numpy as np
class class1(nn.Module):
    def fonk1(self, b1 = 20001, b2=50, b3=20, word_freq=None, padding_idx=0):
        super(class1, self).fonk1()
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = nn.Embedding(b1, b2, padding_idx=padding_idx)
        self.b5 = nn.Embedding(b1, b2, padding_idx=padding_idx)
        self.fonk2()
        self.b6 = self.fonk3(word_freq)
        self.b7 = torch.b7('cuda' if torch.cuda.is_available() else 'cpu')
    def fonk2(self):
        b8 = 0.5 / self.b2
        self.b4.weight.data.uniform_(-b8, b8)
        self.b5.weight.data.uniform_(-b8, b8)
    @staticmethod
    def fonk3(word_freq):
        if word_freq is None:
            raise ValueError("word_freq must be provided for negative sampling distribution.")
        b6 = np.power(word_freq, 0.75)
        b6 /= b6.sum()
        return b6
    def fonk4(self, target, contexts):
        batch_size, b9 = target.size(0), contexts.size(1)
        b10 = self.fonk5(batch_size, b9)
        b11 = self.b4(target).unsqueeze(2)
        b12 = self.b5(contexts)
        b13 = self.b5(b10)
        b14 = torch.bmm(b12, b11).squeeze().sigmoid().log()
        b15 = torch.bmm(-b13, b11).sigmoid().log().view(-1, b9, self.b3).sum(2)
        b16 = -(b14 + b15).mean()
        return b16
    def fonk5(self, batch_size, b9):
        b10 = np.random.choice(self.b1, size=(batch_size, b9 * self.b3), replace=True, p=self.b6)
        return torch.tensor(b10, b17 = torch.long, b7=self.b7)