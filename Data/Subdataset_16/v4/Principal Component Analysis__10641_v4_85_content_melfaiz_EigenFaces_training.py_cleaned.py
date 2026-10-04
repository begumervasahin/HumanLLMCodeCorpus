import cv2
import os
from PIL import Image
b1 = "C:/melfaiz/eigenfaces/faces"
def fonk1(name, b2):
    b2 = os.b2.join(b1, b2)
    os.makedirs(b2, b3 = True)
    os.chdir(b2)
    b4 = cv2.VideoCapture(0)
    a1 = 0
    b5 = []
    b6 = (100, 100)
    b7 = cv2.CascadeClassifier("C:/melfaiz/eigenfaces/haarcascade_frontalface_alt.xml")
    while True:
        ret, b8 = b4.read()
        if not ret:
            break
        b8 = cv2.flip(b8, 1)
        b9 = cv2.cvtColor(b8, cv2.COLOR_BGR2GRAY)
        b10 = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(b8, f"Capture {a1}", (240, 50), b10, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        b11 = b7.detectMultiScale(b9, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in b11:
            cv2.rectangle(b8, (x, y), (x + w, y + h), (255, 0, 0), 2)
            b12 = b8[y + 2:y + h - 2, x + 2:x + w - 2]
            b12 = cv2.resize(b12, b6)
        cv2.imshow("Training", b8)
        b13 = cv2.waitKey(1)
        if b13 % b14 = = 27 or cv2.getWindowProperty('Training', 0) < 0:
            print("Escape hit, closing...")
            break
        elif b13 % b14 = = 32:
            b15 = f"opencv_frame_{a1}.png"
            b5.append(b12)
            b16 = f"{name}_{a1}.png"
            cv2.imwrite(b16, b12)
            a1 += 1
    b4.release()
    cv2.destroyAllWindows()