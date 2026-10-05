import torch
import torch.nn as nn
import torch.nn.functional as F
class CNN_Text(nn.Module):
    def __init__(self, class_num, embed_num=50, embed_dim=50, kernel_num=100, kernel_sizes=[3,4,5], dropout=0.5):
        super(CNN_Text, self).__init__()
        V = embed_num
        D = embed_dim
        C = class_num
        Ci = 1
        Co = kernel_num
        Ks = kernel_sizes
        self.convs1 = nn.ModuleList([nn.Conv2d(Ci, Co, (K, D)) for K in Ks])
        self.dropout = nn.Dropout(dropout)
        self.fc1 = nn.Linear(len(Ks)*Co, C)
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
model = CNN_Text(class_num=10, embed_num=50, embed_dim=50, kernel_num=100, kernel_sizes=[3, 4, 5], dropout=0.5)
inputs = torch.randn(32, 50)
outputs = model(inputs)
print(outputs.shape)
