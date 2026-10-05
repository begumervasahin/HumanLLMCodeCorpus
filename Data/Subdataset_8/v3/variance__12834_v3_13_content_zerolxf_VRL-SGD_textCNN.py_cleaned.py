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
        self.dropout_rate = dropout
        self.convolution_layers = nn.ModuleList([
            nn.Conv2d(in_channels=1, out_channels=self.kernel_num, kernel_size=(K, self.embed_dim)) for K in self.kernel_sizes
        ])
        self.dropout = nn.Dropout(p=self.dropout_rate)
        self.fc = nn.Linear(len(self.kernel_sizes) * self.kernel_num, self.class_num)
    def forward(self, x):
        x = x.unsqueeze(1)
        convolution_results = [F.relu(conv(x)).squeeze(3) for conv in self.convolution_layers]
        pooled_results = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in convolution_results]
        x = torch.cat(pooled_results, 1)
        x = self.dropout(x)
        logits = self.fc(x)
        return logits
model = CNN_Text(class_num=10, embed_num=50, embed_dim=50, kernel_num=100, kernel_sizes=[3, 4, 5], dropout=0.5)
inputs = torch.randn(32, 50)
outputs = model(inputs)
print(outputs.shape)
