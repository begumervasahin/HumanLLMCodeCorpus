import torch
import torch.nn as nn
from torch.nn import init
class YourModel(nn.Module):
    def __init__(self, input_features=10, output_features=5):
        super(YourModel, self).__init__()
        self.linear_layer = nn.Linear(in_features=input_features, out_features=output_features)
    def forward(self, x):
        pass
def initialize_weights(model):
    if isinstance(model, nn.Linear):
        init.xavier_uniform_(model.weight.data)
your_model = YourModel()
your_model.apply(initialize_weights)
for name, param in your_model.named_parameters():
    if 'weight' in name:
        print(f'Initialized weights for {name} with shape {param.shape}')
