
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
        b3 = Image.open(image_path)
        b4 = [180, 270, 350]
        for idx, angle in enumerate(b4, b5 = 1):
            b6 = b3.rotate(angle)
            b7 = os.path.join(output_folder, f"{b2}_{idx}.jpg")
            b6.save(b7)
            print(f"Saved rotated image: {b7}")
def fonk3():
    b8 = os.path.join("Data", "train", "destructed")
    try:
        b9 = fonk1(b8)
        print("Successfully read train data folder path!")
        print("Total images:", len(b9))
        fonk2(b9, b8)
    except FileNotFoundError as e:
        print(e)
if b10 = = "__main__":
    fonk3()