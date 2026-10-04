import os, glob, cv2, random
import numpy as np
from scipy.spatial import distance
import ypoften as of
def attr_edge(imgpath, tffolder, blur_first = True, blur_size = 3,
                    threshold1=100, threshold2=250, adaptive_threshold = True,
                    ratio1 = 0.4, ratio2 = 0.8, savetf = True,
                    select_random = True, n_random = 1000):
    img = cv2.imread(imgpath,0)
    if blur_first:
        img = cv2.GaussianBlur(img,(blur_size, blur_size),0)
    if adaptive_threshold:
        threshold1 = min(100, np.quantile(img, q=ratio1))
        threshold2 = max(200, np.quantile(img, q=ratio2))
        print("edge detection thresholds", threshold1, threshold2)
    edge = cv2.Canny(img, threshold1=threshold1, threshold2=threshold2)
    if savetf:
        imgname = os.path.basename(imgpath)
        imgsavepath = os.path.join(tffolder, "edge canny", os.path.splitext(imgname)[0]+'.png')
        of.create_path(imgsavepath)
        cv2.imwrite(imgsavepath, edge)
    epoints_twodims = np.nonzero(edge)
    epoints = np.transpose(epoints_twodims)
    h, w = edge.shape; dia = (h**2 + w**2)**0.5
    etotal = len(epoints)
    edensity = etotal/(h*w)
    if etotal > 0:
        if select_random:
            random.seed(42)
            epoints = random.sample(list(epoints), min(n_random, etotal))
        dists = distance.pdist(epoints,'euclidean')
        edist = np.mean(dists)/dia
    else:
        edist = -99999
    rlist = [edensity, edist]
    print("edge density & distribution",rlist)
    return(rlist)
def main():
    imgfolder = os.path.join('img all','')
    tffolder = os.path.join("img transform",'')
    resultpath = os.path.join('img result', 'edge.txt')
    imgpaths = glob.glob(imgfolder + '*')
    for j, imgpath in enumerate(imgpaths[:]):
        print("-"*100)
        imgname = os.path.basename(imgpath)
        print(j, imgname)
        wlist = [imgname] + attr_edge(imgpath, tffolder)
        of.save_list_to_txt(wlist, resultpath)
    print("DONE"*50)
if __name__== "__main__":
    main()