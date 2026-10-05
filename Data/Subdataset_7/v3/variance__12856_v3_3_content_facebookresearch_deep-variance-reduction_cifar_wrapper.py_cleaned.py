import torch
import torchvision
import torchvision.transforms as transforms
class class1(torch.utils.data.Dataset):
    def fonk1(self, b3, b1 = True, b4=False, b5=None):
        self.b2 = torchvision.datasets.CIFAR10(
            b3 = b3,
            b1 = b1,
            b4 = b4,
            b5 = b5
        )
        self.b6 = {}
        self.a1 = 0
        self.a2 = 0
    def fonk2(self, index):
        if index in self.b6:
            b7 = self.b6[index]
            self.a1 += 1
        else:
            b7 = self.b2[index]
            self.b6[index] = b7
        self.fonk5()
        return b7
    def fonk3(self):
        return len(self.b2)
    def fonk4(self):
        print(f"Total calls to retransform: {self.a2}, cache hits: {self.a1}")
        self.fonk6()
    def fonk5(self):
        self.a2 += 1
    def fonk6(self):
        self.b6 = {}
        self.a2 = 0
        self.a1 = 0
b5 = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])
b8 = class1(b3='./data', b1=True, b4=True, b5=b5)
b7 = b8[0]
b8.fonk4()