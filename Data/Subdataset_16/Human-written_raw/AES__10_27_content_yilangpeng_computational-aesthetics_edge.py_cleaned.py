import os, glob, cv2, random
import numpy as np
from scipy.spatial import distance
import ypoften as of
def fonk1(imgpath, b19, b1 = True, blur_size = 3,
                    b2 = 100, b6=250, adaptive_threshold = True,
                    b3 = 0.4, ratio2 = 0.8, savetf = True,
                    b4 = True, n_random = 1000):
    b5 = cv2.imread(imgpath,0)
    if b1:
        b5 = cv2.GaussianBlur(b5,(blur_size, blur_size),0)
    if adaptive_threshold:
        b2 = min(100, np.quantile(b5, q=b3))
        b6 = max(200, np.quantile(b5, q=ratio2))
        print("b7 detection thresholds", b2, b6)
    b7 = cv2.Canny(b5, b2=b2, b6=b6)
    if savetf:
        b8 = os.path.basename(imgpath)
        b9 = os.path.join(b19, "b7 canny", os.path.splitext(b8)[0]+'.png')
        of.create_path(b9)
        cv2.imwrite(b9, b7)
    b10 = np.nonzero(b7)
    b11 = np.transpose(b10)
    h, b12 = b7.shape; dia = (h**2 + b12**2)**0.5
    b13 = len(b11)
    b14 = b13/(h*b12)
    if b13 > 0:
        if b4:
            random.seed(42)
            b11 = random.sample(list(b11), min(n_random, b13))
        b15 = distance.pdist(b11,'euclidean')
        b16 = np.mean(b15)/dia
    else:
        b16 = -99999
    b17 = [b14, b16]
    print("b7 density & distribution",b17)
    return(b17)
def fonk2():
    b18 = os.path.join('b5 all','')
    b19 = os.path.join("b5 transform",'')
    b20 = os.path.join('b5 result', 'b7.txt')
    b21 = glob.glob(b18 + '*')
    for j, imgpath in enumerate(b21[:]):
        print("-"*100)
        b8 = os.path.basename(imgpath)
        print(j, b8)
        b22 = [b8] + fonk1(imgpath, b19)
        of.save_list_to_txt(b22, b20)
    print("DONE"*50)
if b23 = = "__main__":
    fonk2()