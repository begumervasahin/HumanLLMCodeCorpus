import torch
from torch import nn
import torch.nn.functional as F
class Encoder(nn.Module):
    def __init__(self, dim=256, nc=1):
        super(Encoder, self).__init__()
        self.conv1 = nn.Conv2d(nc, 16, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(16)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(32)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn3 = nn.BatchNorm2d(64)
        self.conv4 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn4 = nn.BatchNorm2d(128)
        self.fc = nn.Linear(128 * 8 * 7, dim)
    def forward(self, x):
        x = F.leaky_relu(self.bn1(self.pool(self.conv1(x))))
        x = F.leaky_relu(self.bn2(self.pool(self.conv2(x))))
        x = F.leaky_relu(self.bn3(self.pool(self.conv3(x))))
        x = F.leaky_relu(self.bn4(self.pool(self.conv4(x))))
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x
class Decoder(nn.Module):
    def __init__(self, dim=256, nc=1):
        super(Decoder, self).__init__()
        self.fc = nn.Linear(dim, 128 * 8 * 7)
        self.conv1 = nn.ConvTranspose2d(128, 64, kernel_size=3, stride=1, padding=(1, 0), bias=False)
        self.bn1 = nn.BatchNorm2d(64)
        self.conv2 = nn.ConvTranspose2d(64, 32, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(32)
        self.conv3 = nn.ConvTranspose2d(32, 16, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn3 = nn.BatchNorm2d(16)
        self.conv4 = nn.ConvTranspose2d(16, nc, kernel_size=3, stride=1, padding=1, bias=False)
    def forward(self, x):
        x = self.fc(x)
        x = x.view(x.size(0), 128, 8, 7)
        x = F.interpolate(x, scale_factor=2)
        x = F.leaky_relu(self.bn1(self.conv1(x)))
        x = F.interpolate(x, scale_factor=2)
        x = F.leaky_relu(self.bn2(self.conv2(x)))
        x = F.interpolate(x, scale_factor=2)
        x = F.leaky_relu(self.bn3(self.conv3(x)))
        x = F.interpolate(x, scale_factor=2)
        x = torch.sigmoid(self.conv4(x))
        return x[:, :, :, :-2]
class ConvolutionalAutoEncoder(nn.Module):
    def __init__(self, dim=256):
        super(ConvolutionalAutoEncoder, self).__init__()
        self.encoder = Encoder(dim=dim)
        self.decoder = Decoder(dim=dim)
    def forward(self, x):
        bottleneck = self.encoder(x)
        reconstructed = self.decoder(bottleneck)
        return reconstructed, bottleneck
if __name__ == "__main__":
    model = ConvolutionalAutoEncoder(dim=256)
    input_tensor = torch.randn(1, 1, 64, 56)
    reconstructed, bottleneck = model(input_tensor)
    print("Input shape:", input_tensor.shape)
    print("Reconstructed shape:", reconstructed.shape)
    print("Bottleneck shape:", bottleneck.shape)