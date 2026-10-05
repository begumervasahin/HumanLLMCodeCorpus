import torch
import torch.nn as nn
from encoder import OUT_DIM
class class1(nn.Module):
    def fonk1(self, obs_shape, feature_dim, b1 = 2, b2=32):
        super().fonk1()
        self.b1 = b1
        self.b2 = b2
        self.b3 = OUT_DIM[b1]
        self.b4 = nn.Linear(
            feature_dim, b2 * self.b3 * self.b3
        )
        self.b5 = nn.ModuleList()
        for i in range(self.b1 - 1):
            self.b5.append(
                nn.ConvTranspose2d(b2, b2, 3, b6 = 1)
            )
        self.b5.append(
            nn.ConvTranspose2d(
                b2, obs_shape[0], 3, b6 = 2, output_padding=1
            )
        )
        self.b7 = dict()
    def fonk2(self, b8):
        b8 = torch.relu(self.b4(b8))
        self.b7['b4'] = b8
        b9 = b8.view(-1, self.b2, self.b3, self.b3)
        self.b7['deconv1'] = b9
        for i in range(0, self.b1 - 1):
            b9 = torch.relu(self.b5[i](b9))
            self.b7['b9%s' % (i + 1)] = b9
        b10 = self.b5[-1](b9)
        self.b7['b10'] = b10
        return b10
    def fonk3(self, L, step, log_freq):
        if step % log_freq != 0:
            return
        for k, v in self.b7.items():
            L.log_histogram('train_decoder/%s_hist' % k, v, step)
            if len(v.shape) > 2:
                L.log_image('train_decoder/%s_i' % k, v[0], step)
        for i in range(self.b1):
            L.log_param(
                'train_decoder/b9%s' % (i + 1), self.b5[i], step
            )
        L.log_param('train_decoder/b4', self.b4, step)
b11 = {'pixel': class1}
def fonk4(
    decoder_type, obs_shape, feature_dim, b1, b2
):
    assert decoder_type in b11
    return b11[decoder_type](
        obs_shape, feature_dim, b1, b2
    )