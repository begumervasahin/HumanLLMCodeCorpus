import torch.nn as nn
from torch.nn import init
def fonk1(m):
    if isinstance(m, nn.Linear):
        init.xavier_uniform_(m.weight.data)