
import PIL
import glob
import os.path
import numpy as np
import cv2
b1 = []
b2 = os.path.join("Data","train","destructed","*.jpg")
b1.extend(glob.glob(b2))
if (b1 = = None):
    print("Error: Path not found to train data folder..")
else:
    print("Successfully read train data folder path..!")
    print("Total images: ",len(b1))
for i in range(len(b1)):
    b3 = b1[i].split("/")[-1].split('.')[0]
    print(b3)
    b4 = cv2.imread(b1[i])
    b5 = PIL.Image.fromarray(b4)
    b6 = os.path.join("Data","train","destructed")
    cv2.imwrite(b6+b3+"_1.jpg",np.array(b5.rotate(180)))
    cv2.imwrite(b6+b3+"_2.jpg",np.array(b5.rotate(270)))
    cv2.imwrite(b6+b3+"_3.jpg",np.array(b5.rotate(350)))