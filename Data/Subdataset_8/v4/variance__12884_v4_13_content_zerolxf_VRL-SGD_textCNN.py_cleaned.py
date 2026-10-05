import torch
import torch.nn as nn
import torch.nn.functional as F
class CNN_Text(nn.Module):
    def __init__(self, class_num, embed_num=50, embed_dim=50, kernel_num=100, kernel_sizes=[3,4,5], dropout=0.5):
        super(CNN_Text, self).__init__()
        self.embed_num = embed_num
        self.embed_dim = embed_dim
        self.class_num = class_num
        self.kernel_num = kernel_num
        self.kernel_sizes = kernel_sizes
        self.convs1 = nn.ModuleList([nn.Conv2d(1, kernel_num, (K, embed_dim)) for K in kernel_sizes])
        self.dropout = nn.Dropout(dropout)
        self.fc1 = nn.Linear(len(kernel_sizes) * kernel_num, class_num)
    def conv_and_pool(self, x, conv):
        x = F.relu(conv(x)).squeeze(3)
        x = F.max_pool1d(x, x.size(2)).squeeze(2)
        return x
    def forward(self, x):
        x = x.unsqueeze(1)
        x = [F.relu(conv(x)).squeeze(3) for conv in self.convs1]
        x = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in x]
        x = torch.cat(x, 1)
        x = self.dropout(x)
        logit = self.fc1(x)
        return logit