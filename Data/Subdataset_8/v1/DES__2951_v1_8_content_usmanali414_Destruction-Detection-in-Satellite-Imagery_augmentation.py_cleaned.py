import os
import glob
import cv2
import numpy as np
from PIL import Image
train_data_folder = os.path.join("Data", "train", "destructed", "*.jpg")
train_destructed_paths = glob.glob(train_data_folder)
if not train_destructed_paths:
    print("Error: Path not found to train data folder..")
else:
    print("Successfully read train data folder path..!")
    print("Total images:", len(train_destructed_paths))
for img_path in train_destructed_paths:
    img_name = os.path.splitext(os.path.basename(img_path))[0]
    img = cv2.imread(img_path)
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    write_path = os.path.join("Data", "train", "destructed")
    cv2.imwrite(os.path.join(write_path, img_name + "_1.jpg"), np.array(pil_img.rotate(180)))
    cv2.imwrite(os.path.join(write_path, img_name + "_2.jpg"), np.array(pil_img.rotate(270)))
    cv2.imwrite(os.path.join(write_path, img_name + "_3.jpg"), np.array(pil_img.rotate(350)))