import os
import numpy as np
import torch
import torch.nn as nn
import torch.utils.data as data
import torchvision.models as models
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
b1 = "train/"
a1 = 64
b2 = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize(b3 = [0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
b4 = ImageFolder(root=b1, transform=b2)
b5 = data.DataLoader(b4, batch_size=a1, shuffle=True)
b6 = models.inception_v3(pretrained=True).cuda()
b7 = b6.b8.in_features
b6.b8 = nn.Sequential()
for param in b6.parameters():
    param.b9 = False
b6.eval()
a2 = 0
b10 = []
b11 = []
for x, y in b5:
    a2 += x.shape[0]
    b12 = b6(x.cuda())
    b10.extend(list(b12.cpu()))
    b11.extend(y.tolist())
b13 = np.array([x.numpy() for x in b10])
b14 = np.array(b11)
print("Shape of b13:", b13.shape)
np.save("tiny_imagenet_train_x", b13)
np.save("tiny_imagenet_train_y", b14)