import cv2
import os
b1 = "C:\\melfaiz\\eigenfaces\\faces"
def fonk1(path):
    if not os.path.exists(path):
        os.makedirs(path)
def fonk2(b15, b17):
    fonk1(b17)
    b2 = cv2.VideoCapture(0)
    a1 = 0
    b3 = []
    b4 = (100, 100)
    b5 = cv2.CascadeClassifier("C:\\melfaiz\\eigenfaces\\haarcascade_frontalface_alt.xml")
    while True:
        ret, b6 = b2.read()
        if not ret:
            break
        b6 = cv2.flip(b6, 1)
        b7 = cv2.cvtColor(b6, cv2.COLOR_BGR2GRAY)
        b8 = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(b6, f"Capture {a1}", (240, 50), b8, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        b9 = b5.detectMultiScale(b7, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in b9:
            cv2.rectangle(b6, (x, y), (x + w, y + h), (255, 0, 0), 2)
            b10 = b6[y+2:y+h-2, x+2:x+w-2]
            b11 = cv2.resize(b10, b4)
        cv2.imshow("Face Capture", b6)
        b12 = cv2.waitKey(1)
        if b12 % b13 = = 27 or cv2.getWindowProperty('Face Capture', 0) < 0:
            print("Escape hit, closing...")
            break
        elif b12 % b13 = = 32:
            b14 = f"{b15}_{a1}.png"
            b3.append(b11)
            cv2.imwrite(b14, b11)
            a1 += 1
    b2.release()
    cv2.destroyAllWindows()
def fonk3():
    b15 = input("Enter the b15 for the new face: ")
    b16 = input("Enter the folder b15 to save b3: ")
    b17 = os.path.join(b1, b16)
    fonk2(b15, b17)
if b18 = = "__main__":
    fonk3()