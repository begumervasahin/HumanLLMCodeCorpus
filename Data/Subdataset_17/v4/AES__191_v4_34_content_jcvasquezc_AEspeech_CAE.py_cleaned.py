import torch
from torch import nn
import torch.nn.functional as F
class CAEEncoder(nn.Module):
    def __init__(self, dim=256, input_channels=1):
        super(CAEEncoder, self).__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(input_channels, 16, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(16),
            nn.LeakyReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(32),
            nn.LeakyReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(),
            nn.MaxPool2d(2, 2),
        )
        self.fc = nn.Linear(128 * 8 * 7, dim)
    def forward(self, x):
        x = self.layers(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x
class CAEDecoder(nn.Module):
    def __init__(self, dim=256, output_channels=1):
        super(CAEDecoder, self).__init__()
        self.fc = nn.Linear(dim, 128 * 8 * 7)
        self.layers = nn.Sequential(
            nn.ConvTranspose2d(128, 64, kernel_size=3, stride=1, padding=(1, 0), bias=False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(),
            nn.Upsample(scale_factor=2),
            nn.ConvTranspose2d(64, 32, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(32),
            nn.LeakyReLU(),
            nn.Upsample(scale_factor=2),
            nn.ConvTranspose2d(32, 16, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(16),
            nn.LeakyReLU(),
            nn.Upsample(scale_factor=2),
            nn.ConvTranspose2d(16, output_channels, kernel_size=3, stride=1, padding=1, bias=False),
            nn.Sigmoid()
        )
    def forward(self, x):
        x = self.fc(x)
        x = x.view(x.size(0), 128, 8, 7)
        x = self.layers(x)
        return x[:, :, :, :-2]
class ConvolutionalAutoEncoder(nn.Module):
    def __init__(self, dim=256):
        super(ConvolutionalAutoEncoder, self).__init__()
        self.encoder = CAEEncoder(dim=dim)
        self.decoder = CAEDecoder(dim=dim)
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