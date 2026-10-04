import cv2
import numpy as np
import pickle
import random
import os
import matplotlib.pyplot as plt
from scipy.misc import imread
def fonk1(image_path, b1 = 32):
    b2 = imread(image_path, mode="RGB")
    try:
        b3 = cv2.KAZE_create()
        b4 = b3.detect(b2)
        b4 = sorted(b4, key=lambda x: -x.response)[:b1]
        b4, b5 = b3.compute(b2, b4)
        b5 = b5.flatten()
        b6 = (b1 * 64)
        if b5.size < b6:
            b5 = np.concatenate([b5, np.zeros(b6 - b5.size)])
    except cv2.error as e:
        print('Error: ', e)
        return None
    return b5
def fonk2(b13, b7 = "features.pck"):
    b8 = [os.path.join(b13, p) for p in sorted(os.listdir(b13))]
    b9 = {}
    for f in b8:
        print(f'Extracting features from b2 {f}')
        b10 = os.path.basename(f).lower()
        b9[b10] = fonk1(f)
    with open(b7, 'wb') as fp:
        pickle.dump(b9, fp, b11 = pickle.HIGHEST_PROTOCOL)
if b12 = = '__main__':
    b13 = 'path/to/images'
    b7 = 'features.pck'
    fonk2(b13, b7)