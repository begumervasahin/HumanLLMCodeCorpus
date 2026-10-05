import os
import cv2
import torch
from PIL import Image
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))
else:
    print("CUDA device not available.")
class class1(Dataset):
    def fonk1(self, b2, b1 = None):
        self.b2 = b2['data']
        self.b3 = b2['labels']
        self.b4 = sorted(os.listdir(self.b2))
        self.b5 = sorted(os.listdir(self.b3))
        self.b1 = b1
        if len(self.b4) != len(self.b5):
            raise ValueError("The number of images and labels must match.")
    def fonk2(self):
        return len(self.b4)
    def fonk3(self, index):
        if index >= self.fonk2():
            raise IndexError("Index out of range")
        b6 = os.path.join(self.b2, self.b4[index])
        b3 = os.path.join(self.b3, self.b5[index])
        b7 = Image.open(b6).convert('RGB')
        b8 = cv2.imread(b3)
        b8 = cv2.cvtColor(b8, cv2.COLOR_BGR2RGB)
        b8 = cv2.resize(b8, (480, 480))
        b8 = Image.fromarray(b8)
        if self.b1 is not None:
            b7 = self.b1(b7)
            b8 = self.b1(b8)
        return b7, b8
if b9 = = "__main__":
    b10 = {
        'data': '<path_to_image_data>',
        'labels': '<path_to_label_data>'
    }
    b1 = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(b11 = [0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    b12 = class1(b10, b1=b1)
    b13 = DataLoader(b12, batch_size=4, shuffle=True)
    for images, labels in b13:
        print(f'Images batch shape: {images.size()}, Labels batch shape: {labels.size()}')
        break
