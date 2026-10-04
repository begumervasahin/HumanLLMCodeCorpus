import torch
import torch.nn as nn
from torch.nn import init
class SimpleNNModel(nn.Module):
    def __init__(self, input_features=10, output_features=5):
        super(SimpleNNModel, self).__init__()
        self.linear_layer = nn.Linear(in_features=input_features, out_features=output_features)
    def forward(self, x):
        return self.linear_layer(x)
def initialize_weights(model):
    if isinstance(model, nn.Linear):
        init.xavier_uniform_(model.weight.data)
def print_initialized_weights(model):
    for name, param in model.named_parameters():
        if 'weight' in name:
            print(f'Initialized weights for {name} with shape {param.shape}')
def main():
    model = SimpleNNModel()
    model.apply(initialize_weights)
    print_initialized_weights(model)
    example_input = torch.randn(1, 10)
    output = model(example_input)
    print(f'Output: {output}')
if __name__ == "__main__":
    main()