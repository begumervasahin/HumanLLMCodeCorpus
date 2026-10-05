import cv2
import os
b1 = "/b13"
b2 = "/b13/"+
def fonk1(image):
    b3 = "haarcascade_frontalface_alt.xml"
    b4 = cv2.CascadeClassifier(b3)
    b5 = cv2.imread(image)
    try:
        b6 = (b5.shape[1],b5.shape[0])
        b7 = cv2.resize(b5, b6)
        b8 = b4.detectMultiScale(b7)
        for f in b8:
            x, y, w, b9 = [ v for v in f ]
            cv2.rectangle(b5, (x,y), (x+w,y+b9), (0,255,0), 2)
            b10 = b5[y:y+b9, x:x+w]
            b11 = image.split('/')
            b11 = b11[-1]
            cv2.imwrite(b2 + b11, b10)
            print ("Writing: " + image)
    except:
        pass
if b12 = = '__main__':
    b13 = os.listdir(b1)
    a1 = 0
    for b5 in b13:
        b14 = b1 + b5
        print (a1)
        fonk1(b14)
        a1 += 1