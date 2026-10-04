import torch
from torch import nn
import torch.nn.functional as F
class class1(nn.Module):
    def fonk1(self, b1 = 256, nc=1):
        super(class1, self).fonk5()
        self.b2 = nn.Conv2d(nc, 16, kernel_size=3, stride=1, padding=1, bias=False)
        self.b3 = nn.BatchNorm2d(16)
        self.b4 = nn.MaxPool2d(2, 2)
        self.b5 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1, bias=False)
        self.b6 = nn.BatchNorm2d(32)
        self.b7 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1, bias=False)
        self.b8 = nn.BatchNorm2d(64)
        self.b9 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1, bias=False)
        self.b10 = nn.BatchNorm2d(128)
        self.b11 = nn.Linear(128 * 8 * 7, b1)
    def fonk2(self, b12):
        b12 = F.leaky_relu(self.b3(self.b4(self.b2(b12))))
        b12 = F.leaky_relu(self.b6(self.b4(self.b5(b12))))
        b12 = F.leaky_relu(self.b8(self.b4(self.b7(b12))))
        b12 = F.leaky_relu(self.b10(self.b4(self.b9(b12))))
        b12 = b12.view(b12.size(0), -1)
        b12 = self.b11(b12)
        return b12
class class2(nn.Module):
    def fonk3(self, b1 = 256, nc=1):
        super(class2, self).fonk5()
        self.b11 = nn.Linear(b1, 128 * 8 * 7)
        self.b2 = nn.ConvTranspose2d(128, 64, kernel_size=3, stride=1, padding=(1, 0), bias=False)
        self.b3 = nn.BatchNorm2d(64)
        self.b5 = nn.ConvTranspose2d(64, 32, kernel_size=3, stride=1, padding=1, bias=False)
        self.b6 = nn.BatchNorm2d(32)
        self.b7 = nn.ConvTranspose2d(32, 16, kernel_size=3, stride=1, padding=1, bias=False)
        self.b8 = nn.BatchNorm2d(16)
        self.b9 = nn.ConvTranspose2d(16, nc, kernel_size=3, stride=1, padding=1, bias=False)
    def fonk4(self, b12):
        b12 = self.b11(b12)
        b12 = b12.view(b12.size(0), 128, 8, 7)
        b12 = F.interpolate(b12, scale_factor=2)
        b12 = F.leaky_relu(self.b3(self.b2(b12)))
        b12 = F.interpolate(b12, scale_factor=2)
        b12 = F.leaky_relu(self.b6(self.b5(b12)))
        b12 = F.interpolate(b12, scale_factor=2)
        b12 = F.leaky_relu(self.b8(self.b7(b12)))
        b12 = F.interpolate(b12, scale_factor=2)
        b12 = torch.sigmoid(self.b9(b12))
        return b12[:, :, :, 0:-2]
class class3(nn.Module):
    def fonk5(self, b1 = 256):
        super(class3, self).fonk5()
        self.b13 = class1(b1=b1)
        self.b14 = class2(b1=b1)
    def fonk6(self, b12):
        b15 = self.b13(b12)
        b12 = self.b14(b15)
        return b12, b15
if b16 = = "__main__":
    b17 = class3(b1=256)
    b18 = torch.randn(1, 1, 64, 56)
    reconstructed, b15 = b17(b18)
    print("Input shape:", b18.shape)
    print("Reconstructed shape:", reconstructed.shape)
    print("Bottleneck shape:", b15.shape)