
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
        print(f"Error: {err}")
    return hist
def show_result(hist, n_cl=18):
    classes = get_class_names(n_cl)
    num_cor_pix = np.diag(hist)
    num_gt_pix = hist.sum(1)
    union = num_gt_pix + hist.sum(0) - num_cor_pix
    print('IoU for each class:')
    for i in range(n_cl):
        iou = num_cor_pix[i] / union[i] if union[i] != 0 else float('nan')
        print(f'{classes[i]:<15}: {iou:.6f}')
    mean_iou = np.nanmean(num_cor_pix / union)
    print('>>> Mean IoU:', mean_iou)
def get_class_names(num_classes):
    if num_classes == 23:
        return ['bk', 'T-shirt', 'bag', 'belt', 'blazer', 'blouse', 'coat', 'dress', 'face', 'hair',
                'hat', 'jeans', 'legging', 'pants', 'scarf', 'shoe', 'shorts', 'skin', 'skirt',
                'socks', 'stocking', 'sunglass', 'sweater']
    elif num_classes == 20:
        return ['background', 'hat', 'hair', 'glove', 'sunglasses', 'upperclothes',
                'dress', 'coat', 'socks', 'pants', 'jumpsuits', 'scarf', 'skirt',
                'face', 'leftArm', 'rightArm', 'leftLeg', 'rightLeg', 'leftShoe',
                'rightShoe']
    else:
        return ['background', 'hat', 'hair', 'sunglasses', 'upperclothes', 'skirt', 'pants', 'dress',
                'belt', 'leftShoe', 'rightShoe', 'face', 'leftLeg', 'rightLeg', 'leftArm', 'rightArm', 'bag', 'scarf']
def compute_and_display_bfscore(label_path, pred_path):
    bfscores, areas_gt = bfscore.bfscore(label_path, pred_path, 2)
    print("\n>>>> BFscore:\n")
    print("BFSCORE:", bfscores)
    print("Per image BFscore:", np.nanmean(bfscores))
    total_area = np.nansum(areas_gt)
    fw_bfscore = [
        score * area if not (math.isnan(score) or math.isnan(area)) else float('nan')
        for score, area in zip(bfscores, areas_gt)
    ]
    print("\n>>>> Weighted BFscore:\n")
    print("Weighted-BFSCORE:", fw_bfscore)
    print("Per image Weighted-BFscore:", np.nansum(fw_bfscore) / total_area)
if __name__ == "__main__":
    label_path = "gt_0.png"
    pred_path = "pred_0.png"
    n_classes = 18
    val_hist = compute_hist(pred_path, label_path, n_classes)
    show_result(val_hist, n_classes)
    print('\n')
    compute_and_display_bfscore(label_path, pred_path)