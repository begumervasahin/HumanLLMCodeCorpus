import numpy as np
from my_augmentations import zero_pad, random_crop, horizontal_flip
def run_augmentation_v1(image):
    image = zero_pad(image, (40, 40, 3), 4)
    image = random_crop(image, 32)
    image = horizontal_flip(image, 0.5)
    return image
def load_data(path, test=False):
    data = []
    labels = []
    file_prefix = 'test_batch' if test else 'data_batch_'
    file_suffix = '' if test else str(slice)
    for slice in range(1, 6):
        data_dict = np.load(f"{path}{file_prefix}{file_suffix}")
        data.extend(data_dict['data'].reshape((len(data_dict['data']), 3, 32, 32)).transpose(0, 2, 3, 1))
        labels.extend(data_dict['labels'])
        if test:
            break
    return np.array(data), np.array(labels)
def change_lr(optimizer, lr):
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr
        print(f"LR CHANGED: {param_group['lr']}")
class AverageMeter:
    def __init__(self):
        self.reset()
    def reset(self):
        self.val = 0.0
        self.avg = 0.0
        self.sum = 0.0
        self.count = 0.0
    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count