import cv2
import os
b1 = "C:\\melfaiz\\eigenfaces\\faces"
def fonk1(path):
    if not os.path.exists(path):
        os.makedirs(path)
def fonk2(b14, b16):
    fonk1(b16)
    b2 = cv2.VideoCapture(0)
    a1 = 0
    b3 = (100, 100)
    b4 = cv2.CascadeClassifier("C:\\melfaiz\\eigenfaces\\haarcascade_frontalface_alt.xml")
    while True:
        ret, b5 = b2.read()
        if not ret:
            break
        b5 = cv2.flip(b5, 1)
        b6 = cv2.cvtColor(b5, cv2.COLOR_BGR2GRAY)
        b7 = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(b5, f"Capture {a1}", (240, 50), b7, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        b8 = b4.detectMultiScale(b6, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in b8:
            cv2.rectangle(b5, (x, y), (x + w, y + h), (255, 0, 0), 2)
            b9 = b5[y+2:y+h-2, x+2:x+w-2]
            b10 = cv2.resize(b9, b3)
        cv2.imshow("Face Capture", b5)
        b11 = cv2.waitKey(1)
        if b11 % b12 = = 27 or cv2.getWindowProperty('Face Capture', 0) < 0:
            print("Escape hit, closing...")
            break
        elif b11 % b12 = = 32:
            b13 = f"{b14}_{a1}.png"
            cv2.imwrite(os.path.join(b16, b13), b10)
            a1 += 1
    b2.release()
    cv2.destroyAllWindows()
def fonk3():
    b14 = input("Enter the b14 for the new face: ")
    b15 = input("Enter the folder b14 to save images: ")
    b16 = os.path.join(b1, b15)
    fonk2(b14, b16)
if b17 = = "__main__":
    fonk3()