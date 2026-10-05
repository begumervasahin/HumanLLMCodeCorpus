import torchvision
from torch.utils.data import Dataset
class class1(Dataset):
    def fonk1(self, root, b1 = True, download=False, transform=None):
        self.b2 = torchvision.datasets.CIFAR10(root=root, b1=b1, download=download, transform=transform)
        self.b3 = {}
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def fonk2(self, index):
        if index in self.b3:
            b4 = self.b3[index]
            self.a2 += 1
        else:
            b4 = self.b2[index]
            self.b3[index] = b4
        self.a1 += 1
        self.a3 += 1
        return b4
    def fonk3(self):
        return len(self.b2)
    def fonk4(self):
        print(f"Total calls to retransform: {self.a3}, Cache hits: {self.a2}")
        self.b3 = {}
        self.a3 = 0
        self.a2 = 0