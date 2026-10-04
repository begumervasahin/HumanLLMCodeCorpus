
import os
import glob
from PIL import Image
def fonk1(folder_path):
    b1 = glob.glob(os.path.join(folder_path, "*.jpg"))
    if not b1:
        raise FileNotFoundError(f"No images found in {folder_path}")
    return b1
def fonk2(b1, output_folder, b2 = None):
    if b2 is None:
        b2 = [180, 270, 350]
    for image_path in b1:
        b3 = os.path.splitext(os.path.basename(image_path))[0]
        print(f"Processing image: {b3}")
        b4 = Image.open(image_path)
        for idx, angle in enumerate(b2, b5 = 1):
            b6 = b4.rotate(angle)
            b7 = os.path.join(output_folder, f"{b3}_{idx}.jpg")
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