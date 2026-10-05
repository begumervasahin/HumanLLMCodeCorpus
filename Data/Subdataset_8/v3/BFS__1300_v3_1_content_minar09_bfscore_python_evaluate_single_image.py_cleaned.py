import cv2
import numpy as np
from PIL import Image
import bfscore
import math
opencv_major_version = cv2.__version__.split('.')[0]
debug_mode = False
def fast_hist(a, b, n):
    mask = (a >= 0) & (a < n)
    indices = n * a[mask].astype(int) + b[mask]
    return np.bincount(indices, minlength=n ** 2).reshape(n, n)
def compute_hist(img_path, gt_path, num_classes=18):
    hist = np.zeros((num_classes, num_classes))
    try:
        label_image = Image.open(gt_path)
        label_array = np.array(label_image, dtype=np.int32)
        pred_image = Image.open(img_path)
        pred_array = np.array(pred_image, dtype=np.int32)
        label_shape = label_array.shape
        pred_shape = pred_array.shape
        if label_shape != pred_shape:
            pred_image = pred_image.resize((label_shape[1], label_shape[0]), Image.ANTIALIAS)
            pred_array = np.array(pred_image, dtype=np.int32)
        hist += fast_hist(label_array, pred_array, num_classes)
    except Exception as err:
        print(err)
    return hist
def show_result(hist, num_classes=18):
    class_names = [
        'background', 'hat', 'hair', 'sunglasses', 'upperclothes', 'skirt', 'pants', 'dress',
        'belt', 'leftShoe', 'rightShoe', 'face', 'leftLeg', 'rightLeg', 'leftArm', 'rightArm', 'bag', 'scarf'
    ]
    if num_classes == 23:
        class_names = [
            'bk', 'T-shirt', 'bag', 'belt', 'blazer', 'blouse', 'coat', 'dress', 'face', 'hair',
            'hat', 'jeans', 'legging', 'pants', 'scarf', 'shoe', 'shorts', 'skin', 'skirt',
            'socks', 'stocking', 'sunglass', 'sweater'
        ]
    elif num_classes == 20:
        class_names = [
            'background', 'hat', 'hair', 'glove', 'sunglasses', 'upperclothes',
            'dress', 'coat', 'socks', 'pants', 'jumpsuits', 'scarf', 'skirt',
            'face', 'leftArm', 'rightArm', 'leftLeg', 'rightLeg', 'leftShoe',
            'rightShoe'
        ]
    num_cor_pix = np.diag(hist)
    num_gt_pix = hist.sum(1)
    print('IoU for each class:')
    union = num_gt_pix + hist.sum(0) - num_cor_pix
    for i in range(num_classes):
        print('%-15s: %f' % (class_names[i], num_cor_pix[i] / union[i]))
    iu = num_cor_pix / (num_gt_pix + hist.sum(0) - num_cor_pix)
    print('Mean IoU:', np.nanmean(iu))
if __name__ == "__main__":
    label_path = "gt_0.png"
    pred_path = "pred_0.png"
    num_classes = 18
    val_hist = compute_hist(pred_path, label_path, num_classes)
    show_result(val_hist, num_classes)
    print('\n')
    bfscores, areas_gt = bfscore.bfscore(label_path, pred_path, 2)
    print("\n>>>>BFscore:\n")
    print("BFSCORE:", bfscores)
    print("Per image BFscore:", np.nanmean(bfscores))
    total_area = np.nansum(areas_gt)
    fw_bfscore = [each[0] * each[1] if not (math.isnan(each[0]) or math.isnan(each[1])) else math.nan for each in zip(bfscores, areas_gt)]
    print("\n>>>>Weighted BFscore:\n")
    print("Weighted-BFSCORE:", fw_bfscore)
    print("Per image Weighted-BFscore:", np.nansum(fw_bfscore) / total_area)