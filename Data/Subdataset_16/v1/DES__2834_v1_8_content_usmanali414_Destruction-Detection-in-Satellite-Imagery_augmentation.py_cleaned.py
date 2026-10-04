
import os
import glob
import numpy as np
import cv2
from PIL import Image
def fonk1(folder_path):
    b1 = glob.glob(os.path.join(folder_path, "*.jpg"))
    if not b1:
        raise FileNotFoundError("Error: Path not found to train data folder.")
    return b1
def fonk2(b1, output_folder):
    for image_path in b1:
        b2 = os.path.splitext(os.path.basename(image_path))[0]
        print(f"Processing image: {b2}")
        b3 = cv2.imread(image_path)
        b4 = Image.fromarray(b3)
        b5 = [180, 270, 350]
        for idx, angle in enumerate(b5, b6 = 1):
            b7 = b4.rotate(angle)
            b8 = os.path.join(output_folder, f"{b2}_{idx}.jpg")
            cv2.imwrite(b8, np.array(b7))
            print(f"Saved rotated image: {b8}")
def fonk3():
    b9 = os.path.join("Data", "train", "destructed")
    try:
        b10 = fonk1(b9)
        print("Successfully read train data folder path!")
        print("Total images:", len(b10))
        fonk2(b10, b9)
    except FileNotFoundError as e:
        print(e)
if b11 = = "__main__":
    fonk3()