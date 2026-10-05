import torch
import torch.nn as nn
from encoder import OUT_DIM
class class1(nn.Module):
    def fonk1(self, obs_shape, feature_dim, b1 = 2, b2=32):
        super().fonk1()
        self.b1 = b1
        self.b2 = b2
        self.b3 = OUT_DIM[b1]
        self.b4 = nn.Linear(feature_dim, b2 * self.b3 * self.b3)
        self.b5 = self.fonk4(b1, b2, obs_shape[0])
        self.b6 = {}
    def fonk2(self, b7):
        b7 = torch.relu(self.b4(b7))
        self.b6['b4'] = b7
        b8 = b7.view(-1, self.b2, self.b3, self.b3)
        self.b6['deconv1'] = b8
        for i, deconv_layer in enumerate(self.b5[:-1]):
            b8 = torch.relu(deconv_layer(b8))
            self.b6[f'b8{i + 1}'] = b8
        b9 = self.b5[-1](b8)
        self.b6['b9'] = b9
        return b9
    def fonk3(self, L, step, log_freq):
        if step % log_freq != 0:
            return
        for name, value in self.b6.items():
            L.log_histogram(f'train_decoder/{name}_hist', value, step)
            if len(value.shape) > 2:
                L.log_image(f'train_decoder/{name}_i', value[0], step)
        for i, deconv_layer in enumerate(self.b5):
            L.log_param(f'train_decoder/b8{i + 1}', deconv_layer, step)
        L.log_param('train_decoder/b4', self.b4, step)
    def fonk4(self, b1, b2, num_channels):
        b5 = nn.ModuleList([
            nn.ConvTranspose2d(b2, b2, b10 = 3, stride=1)
            for _ in range(b1 - 1)
        ])
        b5.append(nn.ConvTranspose2d(b2, num_channels, b10 = 3, stride=2, output_padding=1))
        return b5
b11 = {'pixel': class1}
def fonk5(decoder_type, obs_shape, feature_dim, b1, b2):
    assert decoder_type in b11
    return b11[decoder_type](
        obs_shape, feature_dim, b1, b2
    )