import cv2
import os
from PIL import Image
b1 = "C:/melfaiz/eigenfaces/faces"
def fonk1(path):
    os.makedirs(path, b2 = True)
    os.chdir(path)
def fonk2(name, path):
    b3 = os.path.join(b1, path)
    fonk1(b3)
    b4 = cv2.VideoCapture(0)
    a1 = 0
    b5 = (100, 100)
    b6 = cv2.CascadeClassifier("C:/melfaiz/eigenfaces/haarcascade_frontalface_alt.xml")
    while True:
        ret, b7 = b4.read()
        if not ret:
            break
        b7 = cv2.flip(b7, 1)
        b8 = cv2.cvtColor(b7, cv2.COLOR_BGR2GRAY)
        fonk3(b7, a1)
        b9 = b6.detectMultiScale(b8, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in b9:
            fonk4(b7, x, y, w, h)
            b10 = fonk5(b7, x, y, w, h, b5)
        cv2.imshow("Training", b7)
        if fonk6(b4, b7, name, a1, b10):
            break
        a1 += 1
    b4.release()
    cv2.destroyAllWindows()
def fonk3(b7, a1):
    b11 = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(b7, f"Capture {a1}", (240, 50), b11, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
def fonk4(b7, x, y, w, h):
    cv2.rectangle(b7, (x, y), (x + w, y + h), (255, 0, 0), 2)
def fonk5(b7, x, y, w, h, b5):
    b10 = b7[y + 2:y + h - 2, x + 2:x + w - 2]
    return cv2.resize(b10, b5)
def fonk6(b4, b7, name, a1, b10):
    b12 = cv2.waitKey(1)
    if b12 % b13 = = 27 or cv2.getWindowProperty('Training', 0) < 0:
        print("Escape hit, closing...")
        return True
    elif b12 % b13 = = 32:
        fonk7(name, a1, b10)
    return False
def fonk7(name, a1, b10):
    b14 = f"{name}_{a1}.png"
    cv2.imwrite(b14, b10)
