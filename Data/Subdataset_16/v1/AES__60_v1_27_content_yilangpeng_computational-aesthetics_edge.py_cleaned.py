import os
import glob
import cv2
import random
import numpy as np
from scipy.spatial import distance
import ypoften as of
def fonk1(imgpath, b18, b1 = True, blur_size=3, b3=100, b4=250, adaptive_threshold=True, ratio1=0.4, ratio2=0.8, savetf=True, select_random=True, n_random=1000):
    b2 = cv2.imread(imgpath, 0)
    if b1:
        b2 = cv2.GaussianBlur(b2, (blur_size, blur_size), 0)
    if adaptive_threshold:
        b3 = min(100, np.quantile(b2, q=ratio1))
        b4 = max(200, np.quantile(b2, q=ratio2))
        print("Edge detection thresholds:", b3, b4)
    b5 = cv2.Canny(b2, b3=b3, b4=b4)
    if savetf:
        b6 = os.path.basename(imgpath)
        b7 = os.path.join(b18, "edge_canny", os.path.splitext(b6)[0] + '.png')
        of.create_path(b7)
        cv2.imwrite(b7, b5)
    b8 = np.nonzero(b5)
    b9 = np.transpose(b8)
    h, b10 = b5.shape
    b11 = np.sqrt(h**2 + b10**2)
    b12 = len(b9)
    b13 = b12 / (h * b10)
    if b12 > 0:
        if select_random:
            random.seed(42)
            b9 = random.sample(list(b9), min(n_random, b12))
        b14 = distance.pdist(b9, 'euclidean')
        b15 = np.mean(b14) / b11
    else:
        b15 = -99999
    b16 = [b13, b15]
    print("Edge density & distribution:", b16)
    return b16
def fonk2():
    b17 = os.path.join('img_all', '')
    b18 = os.path.join('img_transform', '')
    b19 = os.path.join('img_result', 'b5.txt')
    b20 = glob.glob(b17 + '*')
    for j, imgpath in enumerate(b20):
        print("-" * 100)
        b6 = os.path.basename(imgpath)
        print(j, b6)
        b21 = [b6] + fonk1(imgpath, b18)
        of.save_list_to_txt(b21, b19)
    print("DONE" * 50)
if b22 = = "__main__":
    fonk2()