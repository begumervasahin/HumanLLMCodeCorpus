import os
import glob
import cv2
import random
import numpy as np
from scipy.spatial import distance
import ypoften as of
def fonk1(img_path, b23, b1 = True, blur_size=3,
                            b2 = 100, threshold2_default=250,
                            b3 = True, ratio1_default=0.4, ratio2_default=0.8,
                            b4 = True, select_random=True, n_random=1000):
    b5 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if b1:
        b5 = cv2.GaussianBlur(b5, (blur_size, blur_size), 0)
    if b3:
        b6 = min(100, np.quantile(b5, q=ratio1_default))
        b7 = max(200, np.quantile(b5, q=ratio2_default))
        print("Edge detection thresholds:", b6, b7)
    b8 = cv2.Canny(b5, b6=b2, b7=threshold2_default)
    if b4:
        b9 = os.path.basename(img_path)
        b10 = os.path.join(b23, "edge_canny", os.path.splitext(b9)[0] + '.png')
        of.create_path(b10)
        cv2.imwrite(b10, b8)
    b11 = np.nonzero(b8)
    b12 = np.transpose(b11)
    h, b13 = b8.shape
    b14 = np.sqrt(h**2 + b13**2)
    b15 = len(b12)
    b16 = b15 / (h * b13)
    if b15 > 0 and select_random:
        random.seed(42)
        b12 = random.sample(list(b12), min(n_random, b15))
    if b15 > 0:
        b17 = distance.pdist(b12, 'euclidean')
        b18 = np.mean(b17) / b14
    else:
        b18 = -99999
    b19 = [b16, b18]
    print("Edge density & distribution:", b19)
    return b19
def fonk2(b22, b23, b24):
    b20 = glob.glob(os.path.join(b22, '*'))
    for j, img_path in enumerate(b20):
        print("-" * 100)
        b9 = os.path.basename(img_path)
        print(j, b9)
        b19 = [b9] + fonk1(img_path, b23)
        of.save_list_to_txt(b19, b24)
    print("DONE" * 50)
if b21 = = "__main__":
    b22 = os.path.join('img_all')
    b23 = os.path.join("img_transform")
    b24 = os.path.join('img_result', 'b8.txt')
    fonk2(b22, b23, b24)