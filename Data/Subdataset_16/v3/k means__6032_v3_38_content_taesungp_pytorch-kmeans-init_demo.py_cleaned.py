import os
import glob
import torch
import numpy as np
from PIL import Image
import argparse
import kmeans_init
import one_layer
def fonk1(b13):
    b1 = ['JPEG', 'jpg', 'png', 'PNG']
    b2 = []
    for ext in b1:
        b2.extend(glob.glob(os.path.join(b13.source, f"*.{ext}")))
    b3 = []
    for path in b2:
        b4 = Image.open(path).convert('RGB').resize((b13.image_size, b13.image_size))
        b4 = np.array(b4).astype(np.float32)
        b4 = np.expand_dims(b4, 0)
        b3.append(b4)
        if len(b3) >= b13.batchsize:
            break
    b5 = np.concatenate(b3, axis=0)
    b5 = b5.transpose((0, 3, 1, 2))
    b5 = b5 * 2 / 255.0 - 1
    return torch.from_numpy(b5)
def fonk2(b15):
    for i, b8 in enumerate(b15):
        b6 = f"{i:03d}.png"
        h, w, b7 = b8.shape
        b8 = (b8.squeeze() * 255.0).astype(np.uint8)
        b8 = Image.fromarray(b8).resize((w * 10, h * 10))
        b8.save(b6)
        print(f"The weights were saved at {b6}")
def fonk3():
    b9 = argparse.ArgumentParser(description="Image loading, processing, and k-means initialization")
    b9.add_argument('--source', b10 = './b15', help='Directory of b15')
    b9.add_argument('--image_size', b11 = int, b10=224, help='Image size to resize to')
    b9.add_argument('--batchsize', b11 = int, b10=8, help='Batch size of b15 to load')
    b9.add_argument('--kmeans_num_iter', b11 = int, b10=3, help='Number of k-means iterations')
    b9.add_argument('--kmeans_use_whitening', b12 = 'store_true', help='Use whitening in k-means')
    b9.add_argument('--use_gpu', b12 = 'store_true', help='Use GPU for computations')
    b13 = b9.parse_args()
    b14 = one_layer.OneLayer(3, 6, 9)
    b15 = fonk1(b13)
    if b13.use_gpu:
        b14.cuda()
        b15 = b15.cuda()
    print('Running k-means initialization')
    kmeans_init.kmeans_init(b14, b15, b13.kmeans_num_iter, b13.kmeans_use_whitening)
    print('Visualizing the weights to b15')
    b16 = kmeans_init.visualize_weights(b14)
    fonk2(b16)
if b17 = = '__main__':
    fonk3()