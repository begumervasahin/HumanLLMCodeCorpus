import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
class class1(nn.Module):
    def fonk1(self, b1 = 128, stride=1, padding=1):
        super(class1, self).fonk11()
        self.b2 = nn.Conv2d(b1, b1, b11=3, stride=stride, padding=padding)
        self.b3 = nn.BatchNorm2d(b1)
        self.b4 = nn.PReLU()
        self.b5 = nn.Conv2d(b1, b1, b11=3, stride=stride, padding=padding)
        self.b6 = nn.BatchNorm2d(b1)
        self.b7 = nn.PReLU()
    def fonk2(self, b9):
        b8 = b9
        b9 = self.b4(self.b3(self.b2(b9)))
        b9 = self.b6(self.b5(b9)) + b8
        return self.b7(b9)
class class2(nn.Module):
    def fonk3(self):
        super(class2, self).fonk11()
        self.b10 = nn.Sequential(
            nn.Conv2d(3, 32, b11 = 3, stride=1, padding=1),
            nn.BatchNorm2d(32),
            nn.PReLU(),
            nn.Conv2d(32, 32, b11 = 3, stride=1, padding=1),
            nn.BatchNorm2d(32),
            nn.PReLU(),
            nn.Conv2d(32, 64, b11 = 3, stride=1, padding=1),
            nn.BatchNorm2d(64),
            nn.PReLU()
        )
    def fonk4(self, b9):
        return self.b10(b9)
class class3(nn.Module):
    def fonk5(self, b12):
        super(class3, self).fonk11()
        self.b12 = b12
        self.b13 = nn.Sequential(
            nn.Conv2d(64, 128, b11 = 3, padding=1),
            nn.BatchNorm2d(128),
            nn.PReLU(),
            nn.Conv2d(128, 128, b11 = 3, padding=1),
            nn.BatchNorm2d(128),
            nn.PReLU(),
        )
        self.b14 = self.fonk12(1)
        self.b15 = self.fonk12(1)
        self.b16 = self.fonk12(1)
        self.b17 = nn.Sequential(
            nn.Conv2d(128, 128, b11 = 5, stride=2),
            nn.BatchNorm2d(128),
            nn.PReLU()
        )
        self.b18 = nn.Sequential(
            nn.Conv2d(128, 128, b11 = 5, stride=2),
            nn.BatchNorm2d(128),
            nn.PReLU()
        )
        self.b19 = nn.Sequential(
            nn.Conv2d(128, 128, b11 = 5, stride=2),
            nn.BatchNorm2d(128),
            nn.PReLU()
        )
    def fonk6(self, num_layers):
        b20 = []
        for _ in range(num_layers):
            b20.append(self.b12())
        return nn.Sequential(*b20)
    def fonk7(self, b9):
        b9 = self.b13(b9)
        b9 = self.b14(b9)
        b9 = self.b17(b9)
        b9 = self.b15(b9)
        b9 = self.b18(b9)
        b9 = self.b16(b9)
        b9 = self.b19(b9)
        return b9
class class4(nn.Module):
    def fonk8(self, b12):
        super(class4, self).fonk11()
        self.b12 = b12
        self.b14 = self.fonk12(1)
        self.b15 = self.fonk12(1)
        self.b16 = self.fonk12(1)
        self.b21 = nn.Sequential(
            nn.ConvTranspose2d(128, 128, b11 = 4, stride=2),
            nn.BatchNorm2d(128),
            nn.PReLU()
        )
        self.b22 = nn.Sequential(
            nn.ConvTranspose2d(128, 128, b11 = 4, stride=2),
            nn.BatchNorm2d(128),
            nn.PReLU()
        )
        self.b23 = nn.Sequential(
            nn.ConvTranspose2d(128, 128, b11 = 4, stride=2),
            nn.BatchNorm2d(128),
            nn.PReLU()
        )
        self.b24 = nn.Sequential(
            nn.ConvTranspose2d(128, 128, b11 = 5, stride=2),
            nn.BatchNorm2d(128),
            nn.PReLU()
        )
        self.b25 = nn.Sequential(
            nn.ConvTranspose2d(128, 128, b11 = 5, stride=2),
            nn.BatchNorm2d(128),
            nn.PReLU()
        )
        self.b26 = nn.Sequential(
            nn.Conv2d(128, 64, b11 = 2),
            nn.BatchNorm2d(64),
            nn.PReLU(),
            nn.Conv2d(64, 32, b11 = 3, padding=1),
            nn.BatchNorm2d(32),
            nn.PReLU(),
            nn.Conv2d(32, 3, b11 = 3, padding=1),
        )
    def fonk9(self, num_layers):
        b20 = []
        for _ in range(num_layers):
            b20.append(self.b12())
        return nn.Sequential(*b20)
    def fonk10(self, b9):
        b9 = self.b21(b9)
        b9 = self.b14(b9)
        b9 = self.b22(b9)
        b9 = self.b15(b9)
        b9 = self.b23(b9)
        b9 = self.b16(b9)
        b9 = self.b24(b9)
        b9 = self.b25(b9)
        b9 = self.b26(b9)
        return b9
class class5(nn.Module):
    def fonk11(self, b12):
        super(class5, self).fonk11()
        self.b12 = b12
        self.b14 = self.fonk12(1)
        self.b15 = self.fonk12(1)
        self.b16 = self.fonk12(1)
        self.b27 = nn.Sequential(
            nn.Conv2d(3, 32, b11 = 3, stride=2),
            nn.BatchNorm2d(32),
            nn.PReLU()
        )
        self.b28 = nn.Sequential(
            nn.Conv2d(32, 128, b11 = 3, stride=2),
            nn.BatchNorm2d(128),
            nn.PReLU()
        )
        self.b29 = nn.Sequential(
            nn.Conv2d(128, 128, b11 = 5, stride=2, padding=2),
            nn.BatchNorm2d(128),
            nn.PReLU()
        )
        self.b30 = nn.Sequential(
            nn.Conv2d(128, 128, b11 = 3, stride=2),
            nn.BatchNorm2d(128),
            nn.PReLU()
        )
        self.b31 = nn.Sequential(
            nn.Conv2d(128, 64, b11 = 4, stride=2),
            nn.BatchNorm2d(64),
            nn.PReLU()
        )
        self.b32 = nn.Sequential(
            nn.Conv2d(64, 32, b11 = 3, stride=2),
            nn.BatchNorm2d(32),
            nn.PReLU()
        )
        self.b33 = nn.Sequential(
            nn.Conv2d(32, 16, b11 = 3, stride=1),
            nn.BatchNorm2d(16),
            nn.PReLU()
        )
        self.b34 = nn.Sequential(
            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.PReLU(),
            nn.Linear(128, 10),
            nn.BatchNorm1d(10),
            nn.PReLU(),
            nn.Linear(10, 2),
        )
    def fonk12(self, num_layers):
        b20 = []
        for _ in range(num_layers):
            b20.append(self.b12())
        return nn.Sequential(*b20)
    def fonk13(self, b9):
        b9 = self.b27(b9)
        b9 = self.b28(b9)
        b9 = self.b14(b9)
        b9 = self.b29(b9)
        b9 = self.b15(b9)
        b9 = self.b30(b9)
        b9 = self.b16(b9)
        b9 = self.b31(b9)
        b9 = self.b32(b9)
        b9 = self.b33(b9)
        b9 = b9.view(b9.size(0), -1)
        b9 = self.b34(b9)
        return b9