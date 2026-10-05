import torch.nn as nn
from torch.nn import init
def initialize_linear_weights(linear_layer):
    if isinstance(linear_layer, nn.Linear):
        init.xavier_uniform_(linear_layer.weight.data)