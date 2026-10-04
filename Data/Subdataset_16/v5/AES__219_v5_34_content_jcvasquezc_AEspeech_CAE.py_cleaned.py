import torch
from torch import nn
import torch.nn.functional as F
class class1(nn.Module):
    def fonk1(self, b1 = 256, input_channels=1):
        super(class1, self).fonk5()
        self.b2 = nn.Sequential(
            nn.Conv2d(input_channels, 16, b3 = 3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(16),
            nn.LeakyReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(16, 32, b3 = 3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(32),
            nn.LeakyReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(32, 64, b3 = 3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(64, 128, b3 = 3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(),
            nn.MaxPool2d(2, 2),
        )
        self.b4 = nn.Linear(128 * 8 * 7, b1)
    def fonk2(self, b5):
        b5 = self.b2(b5)
        b5 = b5.view(b5.size(0), -1)
        b5 = self.b4(b5)
        return b5
class class2(nn.Module):
    def fonk3(self, b1 = 256, output_channels=1):
        super(class2, self).fonk5()
        self.b4 = nn.Linear(b1, 128 * 8 * 7)
        self.b2 = nn.Sequential(
            nn.ConvTranspose2d(128, 64, b3 = 3, stride=1, padding=(1, 0), bias=False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(),
            nn.Upsample(b6 = 2),
            nn.ConvTranspose2d(64, 32, b3 = 3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(32),
            nn.LeakyReLU(),
            nn.Upsample(b6 = 2),
            nn.ConvTranspose2d(32, 16, b3 = 3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(16),
            nn.LeakyReLU(),
            nn.Upsample(b6 = 2),
            nn.ConvTranspose2d(16, output_channels, b3 = 3, stride=1, padding=1, bias=False),
            nn.Sigmoid()
        )
    def fonk4(self, b5):
        b5 = self.b4(b5)
        b5 = b5.view(b5.size(0), 128, 8, 7)
        b5 = self.b2(b5)
        return b5[:, :, :, :-2]
class class3(nn.Module):
    def fonk5(self, b1 = 256):
        super(class3, self).fonk5()
        self.b7 = class1(b1=b1)
        self.b8 = class2(b1=b1)
    def fonk6(self, b5):
        b9 = self.b7(b5)
        b10 = self.b8(b9)
        return b10, b9
if b11 = = "__main__":
    b12 = class3(b1=256)
    b13 = torch.randn(1, 1, 64, 56)
    b10, b9 = b12(b13)
    print("Input shape:", b13.shape)
    print("Reconstructed shape:", b10.shape)
    print("Bottleneck shape:", b9.shape)