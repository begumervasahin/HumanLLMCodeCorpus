import numpy as np
from my_augmentations import zero_pad, random_crop, horizontal_flip
def fonk1(b1):
    b1 = zero_pad(b1, (40, 40, 3), 4)
    b1 = random_crop(b1, 32)
    b1 = horizontal_flip(b1, 0.5)
    return b1
def fonk2(path, b2 = False):
    b3 = []
    b4 = []
    for slice in range(1, 6):
        b5 = 'test_batch' if b2 else f'data_batch_{slice}'
        b6 = np.load(path + b5)
        b7 = b6['b3'].reshape((len(b6['b3']), 3, 32, 32)).transpose(0, 2, 3, 1)
        b3.extend(b7)
        b4.extend(b6['b4'])
        if b2:
            break
    return b3, b4
def fonk3(optimizer, lr):
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr
        print(f"LR CHANGED: {param_group['lr']}")
class class1:
    def fonk4(self):
        self.fonk5()
    def fonk5(self):
        self.a1 = 0.0
        self.a2 = 0.0
        self.a3 = 0.0
        self.a4 = 0.0
    def fonk6(self, a1, b8 = 1):
        self.a1 = a1
        self.a3 += a1 * b8
        self.a4 += b8
        self.a2 = self.a3 / self.a4