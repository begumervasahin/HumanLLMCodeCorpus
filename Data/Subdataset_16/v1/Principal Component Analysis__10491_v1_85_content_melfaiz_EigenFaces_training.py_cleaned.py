import cv2
import os
b1 = "C:\\melfaiz\\eigenfaces\\faces"
def fonk1(b16, b2):
    b2 = os.b2.join(b1, b2)
    if not os.b2.exists(b2):
        os.makedirs(b2)
    os.chdir(b2)
    b3 = cv2.VideoCapture(0)
    a1 = 0
    b4 = []
    b5 = (100, 100)
    b6 = cv2.CascadeClassifier("C:\\melfaiz\\eigenfaces\\haarcascade_frontalface_alt.xml")
    while True:
        ret, b7 = b3.read()
        if not ret:
            break
        b7 = cv2.flip(b7, 1)
        b8 = cv2.cvtColor(b7, cv2.COLOR_BGR2GRAY)
        b9 = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(b7, "Capture " + str(a1), (240, 50), b9, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        b10 = b6.detectMultiScale(b8, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in b10:
            cv2.rectangle(b7, (x, y), (x + w, y + h), (255, 0, 0), 2)
            b11 = b7[y+2:y+h-2, x+2:x+w-2]
            b11 = cv2.resize(b11, b5)
        cv2.imshow("training", b7)
        b12 = cv2.waitKey(1)
        if b12 % b13 = = 27 or cv2.getWindowProperty('training', 0) < 0:
            print("Escape hit, closing...")
            break
        elif b12 % b13 = = 32:
            b14 = "{}_{}.png".format(b16, a1)
            b4.append(b11)
            cv2.imwrite(b14, b11)
            a1 += 1
    b3.release()
    cv2.destroyAllWindows()
if b15 = = "__main__":
    b16 = input("Enter the b16 for the new face: ")
    b2 = input("Enter the folder b16 to save b4: ")
    fonk1(b16, b2)