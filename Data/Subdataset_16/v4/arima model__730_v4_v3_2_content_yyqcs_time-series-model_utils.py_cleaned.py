import torch
import torch.nn as nn
import torch.nn.init as init
class class1(nn.Module):
    def fonk1(self, b1 = 10, output_features=5):
        super(class1, self).fonk1()
        self.b2 = nn.Linear(in_features=b1, out_features=output_features)
    def fonk2(self, x):
        return self.b2(x)
def fonk3(model):
    if isinstance(model, nn.Linear):
        init.xavier_uniform_(model.weight.data)
        if model.bias is not None:
            init.zeros_(model.bias.data)
b3 = class1()
b3.apply(initialize_weights)
for name, param in b3.named_parameters():
    if 'weight' in name:
        print(f'Initialized weights for {name} with shape {param.shape}')
