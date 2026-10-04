
import cv2
import numpy as np
from PIL import Image
import bfscore
import math
major = cv2.__version__.split('.')[0]
bDebug = False
def fast_hist(a, b, n):
    k = (a >= 0) & (a < n)
    return np.bincount(n * a[k].astype(int) + b[k], minlength=n**2).reshape(n, n)
def compute_hist(img_path, gt_path, num_classes=18):
    hist = np.zeros((num_classes, num_classes))
    try:
        label = Image.open(gt_path)
        label_array = np.array(label, dtype=np.int32)
        image = Image.open(img_path)
        image_array = np.array(image, dtype=np.int32)
        gtsz = label_array.shape
        imgsz = image_array.shape
        if gtsz != imgsz:
            image = image.resize((gtsz[1], gtsz[0]), Image.ANTIALIAS)
            image_array = np.array(image, dtype=np.int32)
        hist += fast_hist(label_array, image_array, num_classes)
    except Exception as err:
        print(f"Error processing images: {err}")
    return hist
def show_result(hist, n_cl=18):
    classes = {
        18: ['background', 'hat', 'hair', 'sunglasses', 'upperclothes', 'skirt', 'pants', 'dress',
             'belt', 'leftShoe', 'rightShoe', 'face', 'leftLeg', 'rightLeg', 'leftArm', 'rightArm', 'bag', 'scarf'],
        23: ['bk', 'T-shirt', 'bag', 'belt', 'blazer', 'blouse', 'coat', 'dress', 'face', 'hair',
             'hat', 'jeans', 'legging', 'pants', 'scarf', 'shoe', 'shorts', 'skin', 'skirt',
             'socks', 'stocking', 'sunglass', 'sweater'],
        20: ['background', 'hat', 'hair', 'glove', 'sunglasses', 'upperclothes', 'dress', 'coat', 'socks',
             'pants', 'jumpsuits', 'scarf', 'skirt', 'face', 'leftArm', 'rightArm', 'leftLeg', 'rightLeg',
             'leftShoe', 'rightShoe']
    }
    if n_cl not in classes:
        print(f"Unsupported number of classes: {n_cl}")
        return
    class_names = classes[n_cl]
    num_cor_pix = np.diag(hist)
    num_gt_pix = hist.sum(1)
    print('IoU for each class:')
    union = num_gt_pix + hist.sum(0) - num_cor_pix
    iu = num_cor_pix / union
    for i in range(n_cl):
        print(f'{class_names[i]:-15s}: {iu[i]:.6f}')
    print('>>> mean IoU:', np.nanmean(iu))
if __name__ == "__main__":
    label_path = "gt_0.png"
    pred_path = "pred_0.png"
    n_classes = 18
    val_hist = compute_hist(pred_path, label_path, n_classes)
    show_result(val_hist, n_classes)
    print('\n')
    bfscores, areas_gt = bfscore.bfscore(label_path, pred_path, 2)
    print("\n>>>>BFscore:\n")
    print("BFSCORE:", bfscores)
    print("Per image BFscore:", np.nanmean(bfscores))
    total_area = np.nansum(areas_gt)
    fw_bfscore = [(each[0] * each[1]) if not math.isnan(each[0]) and not math.isnan(each[1]) else math.nan for each in zip(bfscores, areas_gt)]
    print("\n>>>>Weighted BFscore:\n")
    print("Weighted-BFSCORE:", fw_bfscore)
    print("Per image Weighted-BFscore:", np.nansum(fw_bfscore) / total_area)