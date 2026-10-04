import os
import glob
import cv2
import random
import numpy as np
from scipy.spatial import distance
import ypoften as of
def fonk1(img_path, b19, b1 = True, blur_size=3, b3=100, b4=250, adaptive_threshold=True, ratio1=0.4, ratio2=0.8, save_tf=True, select_random=True, n_random=1000):
    b2 = cv2.imread(img_path, 0)
    if b1:
        b2 = cv2.GaussianBlur(b2, (blur_size, blur_size), 0)
    if adaptive_threshold:
        b3 = min(100, np.quantile(b2, q=ratio1))
        b4 = max(200, np.quantile(b2, q=ratio2))
        print(f"Edge detection thresholds: {b3}, {b4}")
    b5 = cv2.Canny(b2, b3=b3, b4=b4)
    if save_tf:
        b6 = os.path.basename(img_path)
        b7 = os.path.join(b19, "edge_canny", os.path.splitext(b6)[0] + '.png')
        of.create_path(b7)
        cv2.imwrite(b7, b5)
    b8 = np.transpose(np.nonzero(b5))
    height, b9 = b5.shape
    b10 = np.sqrt(height**2 + b9**2)
    b11 = len(b8)
    b12 = b11 / (height * b9)
    if b11 > 0:
        if select_random:
            random.seed(42)
            b8 = random.sample(list(b8), min(n_random, b11))
        b13 = distance.pdist(b8, 'euclidean')
        b14 = np.mean(b13) / b10
    else:
        b14 = -99999
    b15 = [b12, b14]
    print(f"Edge density & distribution: {b15}")
    return b15
def fonk2(b18, b19, b20):
    b16 = glob.glob(os.path.join(b18, '*'))
    for idx, img_path in enumerate(b16):
        print("-" * 100)
        b6 = os.path.basename(img_path)
        print(f"{idx}: {b6}")
        b17 = [b6] + fonk1(img_path, b19)
        of.save_list_to_txt(b17, b20)
    print("DONE" * 50)
def fonk3():
    b18 = 'img_all'
    b19 = 'img_transform'
    b20 = os.path.join('img_result', 'b5.txt')
    fonk2(b18, b19, b20)
if b21 = = "__main__":
    fonk3()