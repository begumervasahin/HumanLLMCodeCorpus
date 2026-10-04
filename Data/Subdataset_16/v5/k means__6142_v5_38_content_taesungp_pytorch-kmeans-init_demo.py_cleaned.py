import os
import torch
import numpy as np
import glob
from PIL import Image
import kmeans_init
import one_layer
import argparse
def fonk1(b11):
    b1 = ['JPEG', 'jpg', 'png', 'PNG']
    b2 = [path for ext in b1 for path in glob.glob(os.path.join(b11.source, f"*.{ext}"))]
    b3 = []
    for path in b2:
        b4 = Image.open(path).convert('RGB').resize((b11.image_size, b11.image_size))
        b4 = np.array(b4).astype(np.float32)
        b4 = np.expand_dims(b4, 0)
        b3.append(b4)
        if len(b3) >= b11.batchsize:
            break
    b5 = np.concatenate(b3, axis=0)
    b5 = b5.transpose((0, 3, 1, 2))
    b5 = b5 * 2 / 255.0 - 1
    return torch.from_numpy(b5)
def fonk2(b3):
    for i, b4 in enumerate(b3):
        b6 = f"{i:03d}.png"
        b4 = (b4.squeeze() * 255.0).astype(np.uint8)
        b4 = Image.fromarray(b4).resize((b4.shape[1] * 10, b4.shape[0] * 10))
        b4.save(b6)
        print(f"The weights were saved at {b6}")
def fonk3():
    b7 = argparse.ArgumentParser()
    b7.add_argument('--source', b8 = './b3', help='Source directory for b3')
    b7.add_argument('--image_size', b9 = int, b8=224, help='Size to which b3 are resized')
    b7.add_argument('--batchsize', b9 = int, b8=8, help='Number of b3 to process in a batch')
    b7.add_argument('--kmeans_num_iter', b9 = int, b8=3, help='Number of k-means iterations')
    b7.add_argument('--kmeans_use_whitening', b10 = 'store_true', help='Apply whitening in k-means')
    b7.add_argument('--use_gpu', b10 = 'store_true', help='Use GPU for computation')
    return b7.parse_args()
def fonk4():
    b11 = fonk3()
    b12 = one_layer.OneLayer(3, 6, 9)
    b3 = fonk1(b11)
    if b11.use_gpu:
        b12.cuda()
        b3 = b3.cuda()
    print('Running k-means initialization')
    kmeans_init.kmeans_init(b12, b3, b11.kmeans_num_iter, b11.kmeans_use_whitening)
    print('Visualizing the weights to b3')
    b13 = kmeans_init.visualize_weights(b12)
    fonk2(b13)
if b14 = = '__main__':
    fonk4()