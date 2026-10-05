import torch.nn as nn
from torch.nn import init
def fonk1(module):
    if isinstance(module, nn.Linear):
        init.xavier_uniform_(module.weight.data)