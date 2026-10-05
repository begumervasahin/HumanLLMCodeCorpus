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
class ImageLabelDataset(Dataset):
    def __init__(self, data_path, transform=None):
        self.data_path = data_path['data']
        self.label_path = data_path['labels']
        self.data_files = sorted(os.listdir(self.data_path))
        self.label_files = sorted(os.listdir(self.label_path))
        self.transform = transform
        if len(self.data_files) != len(self.label_files):
            raise ValueError("The number of images and labels must match.")
    def __len__(self):
        return len(self.data_files)
    def __getitem__(self, index):
        if index >= self.__len__():
            raise IndexError("Index out of range")
        image_path = os.path.join(self.data_path, self.data_files[index])
        label_path = os.path.join(self.label_path, self.label_files[index])
        image = Image.open(image_path).convert('RGB')
        label = cv2.imread(label_path)
        label = cv2.cvtColor(label, cv2.COLOR_BGR2RGB)
        label = cv2.resize(label, (480, 480))
        label = Image.fromarray(label)
        if self.transform is not None:
            image = self.transform(image)
            label = self.transform(label)
        return image, label
if __name__ == "__main__":
    data_paths = {
        'data': '<path_to_image_data>',
        'labels': '<path_to_label_data>'
    }
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    dataset = ImageLabelDataset(data_paths, transform=transform)
    dataloader = DataLoader(dataset, batch_size=4, shuffle=True)
    for images, labels in dataloader:
        print(f'Images batch shape: {images.size()}, Labels batch shape: {labels.size()}')
        break
