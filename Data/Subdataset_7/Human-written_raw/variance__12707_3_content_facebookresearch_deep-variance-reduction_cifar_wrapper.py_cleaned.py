from torchvision import datasets, transforms
from torch.utils.data.sampler import RandomSampler
import torchvision
import torchvision.transforms as transforms
import torch.utils.data
import pdb
class class1(torch.utils.data.Dataset):
    def fonk1(self, b2, train, b3, transform):
        self.b1 = torchvision.datasets.CIFAR10(
            b2 = b2, train=train,
            b3 = b3, transform=transform)
        self.b4 = {}
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def fonk2(self, index):
        if index in self.b4.keys():
            b5 = self.b4[index]
            self.a2 += 1
        else:
            b5 = self.b1[index]
            self.b4[index] = b5
        self.a1 += 1
        self.a3 += 1
        return b5
    def fonk3(self):
        return len(self.b1)
    def fonk4(self):
        print("total calls retransform: {}, cache hits: {}".format(
            self.a3, self.a2))
        self.b4 = {}
        self.a3 = 0
        self.a2 = 0