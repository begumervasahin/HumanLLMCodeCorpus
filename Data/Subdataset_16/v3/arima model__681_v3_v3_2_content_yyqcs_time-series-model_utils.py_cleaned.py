import torch
import torch.nn as nn
from torch.nn import init
class class1(nn.Module):
    def fonk1(self, b1 = 10, output_features=5):
        super(class1, self).fonk1()
        self.b2 = nn.Linear(in_features=b1, out_features=output_features)
    def fonk2(self, x):
        return self.b2(x)
def fonk3(b3):
    if isinstance(b3, nn.Linear):
        init.xavier_uniform_(b3.weight.data)
def fonk4(b3):
    for name, param in b3.named_parameters():
        if 'weight' in name:
            print(f'Initialized weights for {name} with shape {param.shape}')
def fonk5():
    b3 = class1()
    b3.apply(initialize_weights)
    fonk4(b3)
    b4 = torch.randn(1, 10)
    b5 = b3(b4)
    print(f'Output: {b5}')
if b6 = = "__main__":
    fonk5()