import cv2
import os
b1 = "/b11"
b2 = "/b11/cropped/"
def fonk1(b12):
    b3 = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    b4 = cv2.imread(b12)
    try:
        b5 = (b4.shape[1], b4.shape[0])
        b6 = cv2.resize(b4, b5)
        b7 = b3.detectMultiScale(b6)
        for (x, y, w, h) in b7:
            cv2.rectangle(b4, (x, y), (x + w, y + h), (0, 255, 0), 2)
            b8 = b4[y:y + h, x:x + w]
            b9 = os.path.basename(b12)
            cv2.imwrite(os.path.join(b2, b9), b8)
            print("Saved cropped face:", b9)
    except Exception as e:
        print("Error:", e)
if b10 = = '__main__':
    b11 = os.listdir(b1)
    for i, b4 in enumerate(b11, 1):
        b12 = os.path.join(b1, b4)
        print(f"Processing image {i}/{len(b11)}: {b12}")
        fonk1(b12)