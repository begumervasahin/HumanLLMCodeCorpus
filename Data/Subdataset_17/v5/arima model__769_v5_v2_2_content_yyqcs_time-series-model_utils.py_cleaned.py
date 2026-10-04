import torch
import torch.nn as nn
from torch.nn import init
class YourModel(nn.Module):
    def __init__(self):
        super(YourModel, self).__init__()
        self._initialize_layers()
    def _initialize_layers(self):
        self.linear_layer = nn.Linear(in_features=10, out_features=5)
    def forward(self, x):
        return self.linear_layer(x)
def initialize_weights(m):
    if isinstance(m, nn.Linear):
        init.xavier_uniform_(m.weight.data)
def print_initialized_weights(model):
    for name, param in model.named_parameters():
        if 'weight' in name:
            print(f'Initialized weights for {name} with shape {param.shape}')
def main():
    your_model = YourModel()
    your_model.apply(initialize_weights)
    print_initialized_weights(your_model)
    example_input = torch.randn(1, 10)
    output = your_model(example_input)
    print(f"Output from the model: {output}")
if __name__ == "__main__":
    main()