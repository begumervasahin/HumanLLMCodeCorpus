import torch
import torch.nn as nn
import torch.nn.init as init
class YourModel(nn.Module):
    def __init__(self, input_features=10, output_features=5):
        super(YourModel, self).__init__()
        self.linear_layer = nn.Linear(input_features, output_features)
    def forward(self, x):
        return self.linear_layer(x)
def initialize_weights(model):
    if isinstance(model, nn.Linear):
        init.xavier_uniform_(model.weight)
        if model.bias is not None:
            init.zeros_(model.bias)
def main():
    your_model = YourModel()
    your_model.apply(initialize_weights)
    for name, param in your_model.named_parameters():
        if 'weight' in name:
            print(f'Initialized weights for {name} with shape {param.shape}')
if __name__ == "__main__":
    main()