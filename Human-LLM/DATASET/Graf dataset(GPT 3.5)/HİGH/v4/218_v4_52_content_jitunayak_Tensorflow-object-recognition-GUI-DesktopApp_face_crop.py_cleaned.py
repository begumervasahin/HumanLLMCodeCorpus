import cv2
import os
b1 = "/b13"
b2 = "/b13/cropped/"
def fonk1(b14):
    b3 = "haarcascade_frontalface_alt.xml"
    b4 = cv2.CascadeClassifier(b3)
    b5 = cv2.imread(b14)
    try:
        b6 = (b5.shape[1], b5.shape[0])
        b7 = cv2.resize(b5, b6)
        b8 = b4.detectMultiScale(b7)
        for f in b8:
            x, y, w, b9 = f
            cv2.rectangle(b5, (x, y), (x + w, y + b9), (0, 255, 0), 2)
            b10 = b5[y:y + b9, x:x + w]
            b11 = os.path.basename(b14)
            cv2.imwrite(b2 + b11, b10)
            print("Writing: " + b11)
    except Exception as e:
        print("Error:", e)
if b12 = = '__main__':
    b13 = os.listdir(b1)
    for i, b5 in enumerate(b13, 1):
        b14 = os.path.join(b1, b5)
        print(i)
        fonk1(b14)