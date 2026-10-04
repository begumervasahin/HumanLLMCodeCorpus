import os
import torch
import numpy as np
import glob
from PIL import Image
import argparse
import kmeans_init
import one_layer
def load_images(opt):
    extensions = ['JPEG', 'jpg', 'png', 'PNG']
    image_paths = []
    for ext in extensions:
        image_paths.extend(glob.glob(os.path.join(opt.source, f"*.{ext}")))
    loaded_images = []
    for path in image_paths:
        image = Image.open(path).convert('RGB').resize((opt.image_size, opt.image_size))
        image = np.array(image).astype(np.float32)
        image = np.expand_dims(image, 0)
        loaded_images.append(image)
        if len(loaded_images) >= opt.batchsize:
            break
    images_array = np.concatenate(loaded_images, axis=0)
    images_array = images_array.transpose((0, 3, 1, 2))
    images_array = images_array * 2 / 255.0 - 1
    return torch.from_numpy(images_array)
def save_images(images):
    for i, img in enumerate(images):
        save_path = f"{i:03d}.png"
        h, w, c = img.shape
        img = (img.squeeze() * 255.0).astype(np.uint8)
        img = Image.fromarray(img).resize((w * 10, h * 10))
        img.save(save_path)
        print(f"The weights were saved at {save_path}")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', default='./images', help='Directory of images')
    parser.add_argument('--image_size', type=int, default=224, help='Image size to resize to')
    parser.add_argument('--batchsize', type=int, default=8, help='Batch size of images to load')
    parser.add_argument('--kmeans_num_iter', type=int, default=3, help='Number of k-means iterations')
    parser.add_argument('--kmeans_use_whitening', action='store_true', help='Use whitening in k-means')
    parser.add_argument('--use_gpu', action='store_true', help='Use GPU for computations')
    opt = parser.parse_args()
    net = one_layer.OneLayer(3, 6, 9)
    images = load_images(opt)
    if opt.use_gpu:
        net.cuda()
        images = images.cuda()
    print('Running k-means initialization')
    kmeans_init.kmeans_init(net, images, opt.kmeans_num_iter, opt.kmeans_use_whitening)
    print('Visualizing the weights to images')
    visual_weights = kmeans_init.visualize_weights(net)
    save_images(visual_weights)