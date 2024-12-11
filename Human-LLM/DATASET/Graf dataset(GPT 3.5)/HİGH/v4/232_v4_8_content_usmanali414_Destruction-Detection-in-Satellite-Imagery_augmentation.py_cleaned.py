import PIL
import glob
import os.path
import numpy as np
import cv2
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
    print(b3)
    b4 = cv2.imread(img_path)
    b5 = PIL.Image.fromarray(b4)
    b6 = os.path.join("Data", "train", "destructed")
    for angle in [180, 270, 350]:
        b7 = b5.rotate(angle)
        cv2.imwrite(os.path.join(b6, f"{b3}_{angle}.jpg"), np.array(b7))
if b8 = = "__main__":
    fonk1()