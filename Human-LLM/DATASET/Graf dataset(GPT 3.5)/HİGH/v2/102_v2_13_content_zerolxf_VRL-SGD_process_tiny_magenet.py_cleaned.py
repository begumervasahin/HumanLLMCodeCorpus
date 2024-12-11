import os
import torchvision.models as models
import torch
import torch.nn as nn
from torchvision import datasets, transforms
import numpy as np
b1 = "train/"
a1 = 64
b2 = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize(b3 = [0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
b4 = datasets.ImageFolder(root=b1, transform=b2)
b5 = torch.utils.data.DataLoader(b4, batch_size=a1, shuffle=True)
b6 = models.inception_v3(pretrained=True).cuda()
b6.b7 = nn.Sequential()
for param in b6.parameters():
    param.b8 = False
b6.eval()
b9 = []
b10 = []
for b11, targets in b5:
    with torch.no_grad():
        b11 = b11.cuda()
        b12 = b6(b11)
        b9.extend(b12.cpu())
        b10.extend(targets.tolist())
b13 = np.array([feature.numpy() for feature in b9])
b14 = np.array(b10)
print("Shape of extracted b9:", b13.shape)
print("Shape of b10:", b14.shape)
np.save("tiny_imagenet_train_x", b13)
np.save("tiny_imagenet_train_y", b14)