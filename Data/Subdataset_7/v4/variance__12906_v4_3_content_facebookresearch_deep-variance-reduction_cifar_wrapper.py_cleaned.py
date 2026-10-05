import torchvision
from torch.utils.data import Dataset
class class1(Dataset):
    def fonk1(self, root, train, download, transform):
        self.b1 = torchvision.datasets.CIFAR10(root=root, train=train, download=download, transform=transform)
        self.b2 = {}
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def fonk2(self, index):
        if index in self.b2:
            b3 = self.b2[index]
            self.a2 += 1
        else:
            b3 = self.b1[index]
            self.b2[index] = b3
        self.a1 += 1
        self.a3 += 1
        return b3
    def fonk3(self):
        return len(self.b1)
    def fonk4(self):
        print(f"Total calls to retransform: {self.a3}, Cache hits: {self.a2}")
        self.b2 = {}
        self.a3 = 0
        self.a2 = 0