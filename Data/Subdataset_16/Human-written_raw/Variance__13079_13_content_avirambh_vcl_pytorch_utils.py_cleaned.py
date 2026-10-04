import numpy as np
from my_augmentations import zero_pad, random_crop, horizontal_flip
def fonk1(b1):
    b1 = zero_pad(b1, (40,40,3), 4)
    b1 = random_crop(b1, 32)
    b1 = horizontal_flip(b1, 0.5)
    return b1
def fonk2(path, b2 = False):
    b3 = []
    b4 = []
    for slice in range(1,6):
        if b2:
            b5 = np.load(path + 'test_batch')
        else:
            b5 = np.load(path + 'data_batch_' + str(slice))
        b3.extend(b5['b3'].
                    reshape((len(b5['b3']), 3, 32, 32)).
                    transpose(0, 2, 3, 1))
        b4.extend(b5['b4'])
        if b2: break
    return b3, b4
def fonk3(optimizer, lr):
    for g in optimizer.param_groups:
        g['lr'] = lr
        print "LR CHANGED: ", g['lr']
class class1(object):
    def fonk4(self):
        self.fonk5()
    def fonk5(self):
        self.a1 = 0.0
        self.a2 = 0.0
        self.a3 = 0.0
        self.a4 = 0.0
    def fonk6(self, a1, b6 = 1):
        self.a1 = a1
        self.a3 += a1 * b6
        self.a4 += b6
        self.a2 = self.a3 / self.a4