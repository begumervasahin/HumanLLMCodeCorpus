import torch
import torch.nn as nn
from encoder import OUT_DIM
class class1(nn.Module):
    def fonk1(self, b13, a1, b1 = 2, b2=32):
        super().fonk1()
        self.b1 = b1
        self.b2 = b2
        self.b3 = OUT_DIM[b1]
        self.b4 = nn.Linear(a1, b2 * self.b3 * self.b3)
        self.b5 = nn.ModuleList([
            nn.ConvTranspose2d(b2, b2, 3, b6 = 1) for _ in range(self.b1 - 1)
        ])
        self.b5.append(
            nn.ConvTranspose2d(b2, b13[0], 3, b6 = 2, output_padding=1)
        )
        self.b7 = {}
    def fonk2(self, b8):
        b8 = torch.relu(self.b4(b8))
        self.b7['b4'] = b8
        b9 = b8.view(-1, self.b2, self.b3, self.b3)
        self.b7['deconv1'] = b9
        for i in range(self.b1 - 1):
            b9 = torch.relu(self.b5[i](b9))
            self.b7[f'b9{i + 1}'] = b9
        b10 = self.b5[-1](b9)
        self.b7['b10'] = b10
        return b10
    def fonk3(self, logger, step, log_freq):
        if step % log_freq != 0:
            return
        for k, v in self.b7.items():
            logger.log_histogram(f'train_decoder/{k}_hist', v, step)
            if len(v.shape) > 2:
                logger.log_image(f'train_decoder/{k}_i', v[0], step)
        for i in range(self.b1):
            logger.log_param(f'train_decoder/b9{i + 1}', self.b5[i], step)
        logger.log_param('train_decoder/b4', self.b4, step)
b11 = {'pixel': class1}
def fonk4(decoder_type, b13, a1, b1, b2):
    assert decoder_type in b11, f"Decoder type '{decoder_type}' not available."
    return b11[decoder_type](b13, a1, b1, b2)
if b12 = = '__main__':
    b13 = (3, 64, 64)
    a1 = 128
    b1 = 2
    b2 = 32
    b14 = fonk4('pixel', b13, a1, b1, b2)
    b8 = torch.randn((1, a1))
    b15 = b14(b8)
    print("Output shape:", b15.shape)