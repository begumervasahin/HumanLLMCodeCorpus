import os
import torch
import numpy as np
import kmeans_init
import one_layer
import glob
import torchvision
from PIL import Image
def fonk1(b12):
    b1 = ['JPEG', 'jpg', 'png', 'PNG']
    b2 = []
    for ext in b1:
        b2 += list(glob.glob(os.path.join(b12.source, "*." + ext)))
    b3 = []
    for path in b2:
        b4 = Image.open(path).convert('RGB').resize((b12.image_size, b12.image_size))
        b4 = np.array(b4).astype(np.float32)
        b4 = np.expand_dims(b4, 0)
        b3.append(b4)
        if len(b3) > b12.batchsize:
            break
    b4 = np.concatenate(b3, axis=0)
    b4 = b4.transpose((0, 3, 1, 2))
    b4 = b4 * 2 / 255.0 - 1
    return torch.from_numpy(b4)
def fonk2(b2):
    for i, b4 in enumerate(b2):
        b5 = "%03d.png" % i
        h, w, b6 = b4.shape
        b4 = (b4.squeeze() * 255.0).astype(np.uint8)
        b4 = Image.fromarray(b4).resize((w * 10, h * 10))
        b4.save(b5)
        print("Saved image at:", b5)
if b7 = = '__main__':
    import argparse
    b8 = argparse.ArgumentParser()
    b8.add_argument('--source', b9 = './b2', help='Directory containing b2')
    b8.add_argument('--image_size', b10 = int, b9=224, help='Target image size')
    b8.add_argument('--batchsize', b10 = int, b9=8, help='Batch size for loading b2')
    b8.add_argument('--kmeans_num_iter', b10 = int, b9=3, help='Number of iterations for k-means')
    b8.add_argument('--kmeans_use_whitening', b11 = 'store_true', help='Whether to use whitening in k-means')
    b8.add_argument('--use_gpu', b11 = 'store_true', help='Whether to use GPU')
    b12 = b8.parse_args()
    b13 = one_layer.OneLayer(3, 6, 9)
    b2 = fonk1(b12)
    if b12.use_gpu:
        b13.cuda()
        b2 = b2.cuda()
    print('Running k-means initialization')
    kmeans_init.kmeans_init(b13, b2, b12.kmeans_num_iter, b12.kmeans_use_whitening)
    print('Visualizing the weights as b2')
    b14 = kmeans_init.visualize_weights(b13)
    fonk2(b14)