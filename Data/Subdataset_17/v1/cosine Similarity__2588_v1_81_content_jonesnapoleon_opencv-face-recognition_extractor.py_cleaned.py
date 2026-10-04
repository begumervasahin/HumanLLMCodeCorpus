import cv2
import numpy as np
import pickle
import random
import os
import matplotlib.pyplot as plt
from scipy.misc import imread
def extract_features(image_path, vector_size=32):
    image = imread(image_path, mode="RGB")
    try:
        alg = cv2.KAZE_create()
        kps = alg.detect(image)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        kps, dsc = alg.compute(image, kps)
        dsc = dsc.flatten()
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print('Error: ', e)
        return None
    return dsc
def batch_extractor(images_path, pickled_db_path="features.pck"):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    result = {}
    for f in files:
        print(f'Extracting features from image {f}')
        name = os.path.basename(f).lower()
        result[name] = extract_features(f)
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp, protocol=pickle.HIGHEST_PROTOCOL)
if __name__ == '__main__':
    images_path = 'path/to/images'
    pickled_db_path = 'features.pck'
    batch_extractor(images_path, pickled_db_path)