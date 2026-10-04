import os
import torch
import numpy as np
import glob
from PIL import Image
import kmeans_init
import one_layer
import argparse
def load_images(opt):
    extensions = ['JPEG', 'jpg', 'png', 'PNG']
    image_paths = []
    for ext in extensions:
        image_paths += glob.glob(os.path.join(opt.source, f"*.{ext}"))
    images = []
    for path in image_paths:
        img = Image.open(path).convert('RGB').resize((opt.image_size, opt.image_size))
        img = np.array(img).astype(np.float32)
        img = np.expand_dims(img, 0)
        images.append(img)
        if len(images) >= opt.batchsize:
            break
    img_batch = np.concatenate(images, axis=0)
    img_batch = img_batch.transpose((0, 3, 1, 2))
    img_batch = img_batch * 2 / 255.0 - 1
    return torch.from_numpy(img_batch)
def save_images(images):
    for i, img in enumerate(images):
        save_path = f"{i:03d}.png"
        img = (img.squeeze() * 255.0).astype(np.uint8)
        img = Image.fromarray(img).resize((img.shape[1] * 10, img.shape[0] * 10))
        img.save(save_path)
        print(f"The weights were saved at {save_path}")
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', default='./images')
    parser.add_argument('--image_size', type=int, default=224)
    parser.add_argument('--batchsize', type=int, default=8)
    parser.add_argument('--kmeans_num_iter', type=int, default=3)
    parser.add_argument('--kmeans_use_whitening', action='store_true')
    parser.add_argument('--use_gpu', action='store_true')
    opt = parser.parse_args()
    net = one_layer.OneLayer(3, 6, 9)
    images = load_images(opt)
    if opt.use_gpu:
        net.cuda()
        images = images.cuda()
    print('Running k-means initialization')
    kmeans_init.kmeans_init(net, images, opt.kmeans_num_iter, opt.kmeans_use_whitening)
    print('Visualizing the weights to images')
    visuals = kmeans_init.visualize_weights(net)
    save_images(visuals)
if __name__ == '__main__':
    main()