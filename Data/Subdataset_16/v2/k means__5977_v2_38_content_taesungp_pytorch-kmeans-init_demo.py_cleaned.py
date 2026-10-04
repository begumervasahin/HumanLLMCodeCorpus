import os
import torch
import numpy as np
import glob
from PIL import Image
import argparse
import kmeans_init
import one_layer
def fonk1(b14):
    b1 = ['JPEG', 'jpg', 'png', 'PNG']
    b2 = []
    for ext in b1:
        b2.extend(glob.glob(os.path.join(b14.source, f"*.{ext}")))
    b3 = []
    for path in b2:
        b4 = Image.open(path).convert('RGB').resize((b14.image_size, b14.image_size))
        b4 = np.array(b4).astype(np.float32)
        b4 = np.expand_dims(b4, 0)
        b3.append(b4)
        if len(b3) >= b14.batchsize:
            break
    b5 = np.concatenate(b3, axis=0)
    b5 = b5.transpose((0, 3, 1, 2))
    b5 = b5 * 2 / 255.0 - 1
    return torch.from_numpy(b5)
def fonk2(b16):
    for i, b8 in enumerate(b16):
        b6 = f"{i:03d}.png"
        h, w, b7 = b8.shape
        b8 = (b8.squeeze() * 255.0).astype(np.uint8)
        b8 = Image.fromarray(b8).resize((w * 10, h * 10))
        b8.save(b6)
        print(f"The weights were saved at {b6}")
if b9 = = '__main__':
    b10 = argparse.ArgumentParser()
    b10.add_argument('--source', b11 = './b16', help='Directory of b16')
    b10.add_argument('--image_size', b12 = int, b11=224, help='Image size to resize to')
    b10.add_argument('--batchsize', b12 = int, b11=8, help='Batch size of b16 to load')
    b10.add_argument('--kmeans_num_iter', b12 = int, b11=3, help='Number of k-means iterations')
    b10.add_argument('--kmeans_use_whitening', b13 = 'store_true', help='Use whitening in k-means')
    b10.add_argument('--use_gpu', b13 = 'store_true', help='Use GPU for computations')
    b14 = b10.parse_args()
    b15 = one_layer.OneLayer(3, 6, 9)
    b16 = fonk1(b14)
    if b14.use_gpu:
        b15.cuda()
        b16 = b16.cuda()
    print('Running k-means initialization')
    kmeans_init.kmeans_init(b15, b16, b14.kmeans_num_iter, b14.kmeans_use_whitening)
    print('Visualizing the weights to b16')
    b17 = kmeans_init.visualize_weights(b15)
    fonk2(b17)