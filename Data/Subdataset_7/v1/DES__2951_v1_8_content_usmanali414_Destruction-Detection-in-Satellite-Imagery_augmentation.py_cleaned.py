import os
import glob
import cv2
import numpy as np
from PIL import Image
b1 = os.path.join("Data", "train", "destructed", "*.jpg")
b2 = glob.glob(b1)
if not b2:
    print("Error: Path not found to train data folder..")
else:
    print("Successfully read train data folder path..!")
    print("Total images:", len(b2))
for img_path in b2:
    b3 = os.path.splitext(os.path.basename(img_path))[0]
    b4 = cv2.imread(img_path)
    b5 = Image.fromarray(cv2.cvtColor(b4, cv2.COLOR_BGR2RGB))
    b6 = os.path.join("Data", "train", "destructed")
    cv2.imwrite(os.path.join(b6, b3 + "_1.jpg"), np.array(b5.rotate(180)))
    cv2.imwrite(os.path.join(b6, b3 + "_2.jpg"), np.array(b5.rotate(270)))
    cv2.imwrite(os.path.join(b6, b3 + "_3.jpg"), np.array(b5.rotate(350)))