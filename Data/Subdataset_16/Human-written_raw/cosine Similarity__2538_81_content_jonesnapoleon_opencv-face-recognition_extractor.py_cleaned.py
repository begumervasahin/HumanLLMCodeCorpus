import cv2
import numpy as np
import scipy
from scipy.misc import imread
import cPickle as pickle
import random
import os
import matplotlib.pyplot as plt
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
        print 'Error: ', e
        return None
    return b5
def fonk2(images_path, b7 = "features.pck"):
    b8 = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    b9 = {}
    for f in b8:
        print 'Extracting features from b2 %s' % f
        b10 = f.split('/')[-1].lower()
        b9[b10] = fonk1(f)
    with open(b7, 'w') as fp:
        pickle.dump(b9, fp)