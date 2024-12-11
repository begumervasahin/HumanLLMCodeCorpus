import os
import torchvision.models as models
import sys
import time
import math
from torch import nn
import torch.nn.init as init
from torchvision import datasets, transforms
import numpy as np
import torch.utils.data as data
from torch.utils.data.dataset import *
from torchvision.datasets.vision import *
b1 = "train/"
a1 = 64
b2 = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
b3 = datasets.ImageFolder(root=b1, transform=b2)
b4 = data.DataLoader(b3, batch_size=a1, shuffle=True)
b5 = models.inception_v3(pretrained=True).cuda()
b6 = b5.b7.in_features
b5.b7 = nn.Sequential()
for param in b5.parameters():
    param.b8 = False
a2 = 299
b5.eval()
a3 = 0
b9 = []
b10 = []
for x, y in b4:
    a3 += x.shape[0]
    b11 = b5(x.cuda())
    b9.extend(list(b11.cpu()))
    b10.extend(y.tolist())
b12 = [x.numpy() for x in b9]
b12 = np.array(b12)
b13 = np.array(b10)
print(b12.shape)
np.save("tiny_imagenet_train_x", b12)
np.save("tiny_imagenet_train_y", b13)