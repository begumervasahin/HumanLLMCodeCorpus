import torch
import torch.nn as nn
from torch.nn import init
class class1(nn.Module):
    def fonk1(self):
        super(class1, self).fonk1()
        self.b1 = nn.Linear(in_features=10, out_features=5)
    def fonk2(self, x):
        pass
def fonk3(m):
    if isinstance(m, nn.Linear):
        init.xavier_uniform_(m.weight.data)
b2 = class1()
b2.apply(initialize_weights)
for name, param in b2.named_parameters():
    if 'weight' in name:
        print(f'Initialized weights for {name} with shape {param.shape}')
