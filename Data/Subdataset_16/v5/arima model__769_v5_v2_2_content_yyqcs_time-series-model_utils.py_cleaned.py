import torch
import torch.nn as nn
from torch.nn import init
class class1(nn.Module):
    def fonk1(self):
        super(class1, self).fonk1()
        self.fonk2()
    def fonk2(self):
        self.b1 = nn.Linear(in_features=10, out_features=5)
    def fonk3(self, x):
        return self.b1(x)
def fonk4(m):
    if isinstance(m, nn.Linear):
        init.xavier_uniform_(m.weight.data)
def fonk5(model):
    for name, param in model.named_parameters():
        if 'weight' in name:
            print(f'Initialized weights for {name} with shape {param.shape}')
def fonk6():
    b2 = class1()
    b2.apply(initialize_weights)
    fonk5(b2)
    b3 = torch.randn(1, 10)
    b4 = b2(b3)
    print(f"Output from the model: {b4}")
if b5 = = "__main__":
    fonk6()