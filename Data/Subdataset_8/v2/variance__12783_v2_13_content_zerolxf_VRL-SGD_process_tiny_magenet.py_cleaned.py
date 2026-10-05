import os
import torchvision.models as models
import torch
import torch.nn as nn
from torchvision import datasets, transforms
import numpy as np
DATA_PATH = "train/"
BATCH_SIZE = 64
image_transform = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
test_data = datasets.ImageFolder(root=DATA_PATH, transform=image_transform)
data_loader = torch.utils.data.DataLoader(test_data, batch_size=BATCH_SIZE, shuffle=True)
model_pre = models.inception_v3(pretrained=True).cuda()
model_pre.fc = nn.Sequential()
for param in model_pre.parameters():
    param.requires_grad = False
model_pre.eval()
features = []
labels = []
for images, targets in data_loader:
    with torch.no_grad():
        images = images.cuda()
        outputs = model_pre(images)
        features.extend(outputs.cpu())
        labels.extend(targets.tolist())
features_array = np.array([feature.numpy() for feature in features])
labels_array = np.array(labels)
print("Shape of extracted features:", features_array.shape)
print("Shape of labels:", labels_array.shape)
np.save("tiny_imagenet_train_x", features_array)
np.save("tiny_imagenet_train_y", labels_array)