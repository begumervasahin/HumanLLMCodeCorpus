import cv2
import os
b1 = "images"
b2 = "cropped_images/"
def fonk1(b14):
    b3 = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
    b4 = cv2.imread(b14)
    b5 = (b4.shape[1], b4.shape[0])
    b6 = cv2.resize(b4, b5)
    b7 = b3.detectMultiScale(b6)
    for (x, y, w, h) in b7:
        b8 = b4[y:y+h, x:x+w]
        b9 = os.path.basename(b14)
        b10 = os.path.join(b2, b9)
        cv2.imwrite(b10, b8)
        print(f"Detected and saved face: {b10}")
if b11 = = '__main__':
    b12 = os.listdir(b1)
    for i, image_file in enumerate(b12, b13 = 1):
        b14 = os.path.join(b1, image_file)
        print(f"Processing image {i}/{len(b12)}: {image_file}")
        fonk1(b14)