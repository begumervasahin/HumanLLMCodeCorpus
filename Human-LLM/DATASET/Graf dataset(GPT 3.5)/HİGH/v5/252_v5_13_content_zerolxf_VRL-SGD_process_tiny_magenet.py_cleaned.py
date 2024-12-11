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
b6.b7 = nn.Sequential()
for param in b6.parameters():
    param.b8 = False
b6.eval()
a2 = 0
b9 = []
b10 = []
for images, labels_batch in b5:
    a2 += images.shape[0]
    with torch.no_grad():
        b11 = b6(images.cuda())
    b9.extend(b11.cpu().numpy())
    b10.extend(labels_batch.numpy())
b12 = np.array(b9)
b13 = np.array(b10)
print("Shape of b9 array:", b12.shape)
np.save("tiny_imagenet_features.npy", b12)
np.save("tiny_imagenet_labels.npy", b13)