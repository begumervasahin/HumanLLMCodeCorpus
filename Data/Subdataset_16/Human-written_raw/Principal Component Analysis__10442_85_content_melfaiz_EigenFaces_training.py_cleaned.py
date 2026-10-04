import cv2
import matplotlib.pylab as plt
import sys
import os
from PIL import Image
b1 = "C:\melfaiz\eigenfaces\\faces"
def fonk1(name,b2):
    b2 = os.b2.join(b1, b2)
    os.chdir(b2)
    b3 = cv2.VideoCapture(0)
    a1 = 0
    b4 = []
    b5 = (100,100)
    b6 = int(b3.get(3))
    b7 = int(b3.get(4))
    H,b8 = [],[]
    while True:
        ret, b9 = b3.read()
        b9 = cv2.flip( b9, 1 )
        b10 = cv2.cvtColor(b9, cv2.COLOR_BGR2GRAY)
        b11 = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(b9, "Capture "+str(a1), (240, 50), b11, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        b12 = cv2.CascadeClassifier("C:\melfaiz\eigenfaces\\haarcascade_frontalface_alt.xml")
        b13 = b12.detectMultiScale(b10,scaleFactor=1.1, minNeighbors=5)
        for (x,y,b6,b7) in b13:
            H,b8 = H+[b7],b8+[b6]
            cv2.rectangle(b9,(x,y),(x+b6,y+b7),(255,0,0),2)
            b14 = b9[y+2:y+b7-2, x+2:x+b6-2]
            b14 = cv2.resize(b14,(b5[0],b5[1]))
        cv2.imshow("training", b9)
        if not ret:
            break
        b15 = cv2.waitKey(1)
        if b15%b16 = = 27 or cv2.getWindowProperty('training', 0) < 0:
            print("Escape hit, closing...")
            break
        else :
            if b15%b16 = = 32:
                b17 = "opencv_frame_{}.png".format(a1)
                b4.append(b14)
                b18 = name+ " " + str(a1)+".png"
                cv2.imwrite(b18,b14)
                a1 += 1
    b3.release()
    cv2.destroyAllWindows()