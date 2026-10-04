import torch
import torch.nn as nn
from torch.nn import init
class YourModel(nn.Module):
    def __init__(self):
        super(YourModel, self).__init__()
        self.linear_layer = nn.Linear(in_features=10, out_features=5)
    def forward(self, x):
        return self.linear_layer(x)
def initialize_weights(m):
    if isinstance(m, nn.Linear):
        init.xavier_uniform_(m.weight)
def main():
    model = YourModel()
    model.apply(initialize_weights)
    for name, param in model.named_parameters():
        if 'weight' in name:
            print(f'Initialized {name} with shape {param.shape}')
if __name__ == "__main__":
    main()