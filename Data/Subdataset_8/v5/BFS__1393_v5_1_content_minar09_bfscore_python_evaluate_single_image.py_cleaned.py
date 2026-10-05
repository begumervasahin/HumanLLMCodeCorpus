import cv2
import numpy as np
from PIL import Image
import bfscore
import math
opencv_major_version = cv2.__version__.split('.')[0]
debug_mode = False
def fast_hist(true_labels, pred_labels, num_classes):
    mask = (true_labels >= 0) & (true_labels < num_classes)
    return np.bincount(num_classes * true_labels[mask].astype(int) + pred_labels[mask], minlength=num_classes**2).reshape(num_classes, num_classes)
def compute_hist(img_path, gt_path, num_classes=18):
    hist = np.zeros((num_classes, num_classes))
    try:
        label_img = Image.open(gt_path)
        label_array = np.array(label_img, dtype=np.int32)
        pred_img = Image.open(img_path)
        pred_array = np.array(pred_img, dtype=np.int32)
        gt_size = label_array.shape
        pred_size = pred_array.shape
        if not gt_size == pred_size:
            pred_img = pred_img.resize((gt_size[1], gt_size[0]), Image.ANTIALIAS)
            pred_array = np.array(pred_img, dtype=np.int32)
        hist += fast_hist(label_array, pred_array, num_classes)
    except Exception as e:
        print(e)
    return hist
def show_result(hist, num_classes=18):
    class_names = {
        18: ['background', 'hat', 'hair', 'sunglasses', 'upperclothes', 'skirt', 'pants', 'dress',
             'belt', 'leftShoe', 'rightShoe', 'face', 'leftLeg', 'rightLeg', 'leftArm', 'rightArm', 'bag', 'scarf'],
        23: ['bk', 'T-shirt', 'bag', 'belt', 'blazer', 'blouse', 'coat', 'dress', 'face', 'hair',
             'hat', 'jeans', 'legging', 'pants', 'scarf', 'shoe', 'shorts', 'skin', 'skirt',
             'socks', 'stocking', 'sunglass', 'sweater'],
        20: ['background', 'hat', 'hair', 'glove', 'sunglasses', 'upperclothes',
             'dress', 'coat', 'socks', 'pants', 'jumpsuits', 'scarf', 'skirt',
             'face', 'leftArm', 'rightArm', 'leftLeg', 'rightLeg', 'leftShoe',
             'rightShoe']
    }.get(num_classes, ['Unknown'] * num_classes)
    correct_pixels = np.diag(hist)
    gt_pixels = hist.sum(1)
    print('IoU for each class:')
    union = gt_pixels + hist.sum(0) - correct_pixels
    for i in range(num_classes):
        print('%-15s: %f' % (class_names[i], correct_pixels[i] / union[i]))
    mean_iou = np.nanmean(correct_pixels / (gt_pixels + hist.sum(0) - correct_pixels))
    print('>>>', 'mean IoU', mean_iou)
if __name__ == "__main__":
    label_path = "gt_0.png"
    pred_path = "pred_0.png"
    num_classes = 18
    hist = compute_hist(pred_path, label_path, num_classes)
    show_result(hist, num_classes)
    print('\n')
    bfscores, areas_gt = bfscore.bfscore(label_path, pred_path, 2)
    print("\n>>>>BFscore:\n")
    print("BFSCORE:", bfscores)
    print("Per image BFscore:", np.nanmean(bfscores))
    total_area = np.nansum(areas_gt)
    weighted_bfscore = [bfscore * area_gt if not (math.isnan(bfscore) or math.isnan(area_gt)) else math.nan for bfscore, area_gt in zip(bfscores, areas_gt)]
    print("\n>>>>Weighted BFscore:\n")
    print("Weighted-BFSCORE:", weighted_bfscore)
    print("Per image Weighted-BFscore:", np.nansum(weighted_bfscore) / total_area)