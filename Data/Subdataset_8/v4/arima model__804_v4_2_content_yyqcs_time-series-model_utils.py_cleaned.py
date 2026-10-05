import torch.nn as nn
from torch.nn import init
def initialize_weights(module):
    if isinstance(module, nn.Linear):
        init.xavier_uniform_(module.weight.data)