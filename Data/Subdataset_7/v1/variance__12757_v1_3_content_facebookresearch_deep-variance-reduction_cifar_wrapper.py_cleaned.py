import torch
import torchvision
import torchvision.transforms as transforms
class class1(torch.utils.data.Dataset):
    def fonk1(self, b3, b1 = True, b4=False, b7=None):
        self.b2 = torchvision.datasets.CIFAR10(
            b3 = b3, b1=b1,
            b4 = b4, b7=b7)
        self.b5 = {}
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def fonk2(self, index):
        if index in self.b5.keys():
            b6 = self.b5[index]
            self.a2 += 1
        else:
            b6 = self.b2[index]
            self.b5[index] = b6
        self.a1 += 1
        self.a3 += 1
        return b6
    def fonk3(self):
        return len(self.b2)
    def fonk4(self):
        print("total calls retransform: {}, cache hits: {}".format(
            self.a3, self.a2))
        self.b5 = {}
        self.a3 = 0
        self.a2 = 0
b7 = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])
b8 = class1(b3='./data', b1=True, b4=True, b7=b7)
b6 = b8[0]
b8.fonk4()