import os
import glob
import cv2
import numpy as np
from PIL import Image
def fonk1():
    b1 = os.path.join("Data", "train", "destructed", "*.jpg")
    b2 = glob.glob(b1)
    if not b2:
        print("Error: Path not found to train data folder..")
        return
    print("Successfully read train data folder path..!")
    print("Total images:", len(b2))
    for img_path in b2:
        fonk2(img_path)
def fonk2(img_path):
    b3 = os.path.splitext(os.path.basename(img_path))[0]
    b4 = cv2.imread(img_path)
    b5 = Image.fromarray(cv2.cvtColor(b4, cv2.COLOR_BGR2RGB))
    b6 = os.path.join("Data", "train", "destructed")
    b7 = [
        b5.rotate(180),
        b5.rotate(270),
        b5.rotate(350)
    ]
    for i, rotated_img in enumerate(b7, b8 = 1):
        cv2.imwrite(os.path.join(b6, f"{b3}_{i}.jpg"), np.array(rotated_img))
if b9 = = "__main__":
    fonk1()