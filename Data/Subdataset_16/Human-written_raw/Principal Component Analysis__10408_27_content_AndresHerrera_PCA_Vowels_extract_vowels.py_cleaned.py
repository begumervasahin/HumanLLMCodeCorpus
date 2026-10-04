import os
import cv2
import numpy as np
a1 = 20
a2 = 20
a3 = 100
def fonk1():
    b1 = cv2.imread("raw_vowels.jpg")
    b2 = cv2.cvtColor(b1,cv2.COLOR_BGR2GRAY)
    b3 = cv2.GaussianBlur(b2,(5,5),0)
    b4 = cv2.adaptiveThreshold(b3,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    cv2.imshow("Threshold Image", b4)
    b5 = b4.copy()
    imgContours, npaContours, b6 = cv2.findContours(b5, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    a4 = 0
    for npaContour in npaContours:
        if cv2.contourArea(npaContour) > a3:
            [intX, intY, intW, intH] = cv2.boundingRect(npaContour)
            cv2.rectangle(b1,(intX, intY),(intX+intW,intY+intH),(0,0,255),2)
            b7 = b4[intY:intY+intH, intX:intX+intW]
            b8 = cv2.resize(b7,(a1,a2))
            cv2.imshow("Original File",b1)
            a4+=1
            cv2.imwrite('vowels/vowel_'+str(a4)+'.png',cv2.bitwise_not(b8))
    print (str(a4) + " files written into (vowels) folder !")
    print ("Notice: You have to arrange (vowels) files into (training) folder tree !")
    print ("in folder :  training/A  <-  store only A images")
    print ("in folder :  training/E  <-  store only E images")
    print ("in folder :  training/I  <-  store only I images")
    print ("in folder :  training/O  <-  store only O images")
    print ("in folder :  training/U  <-  store only U images")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b9 = = "__main__":
    fonk1()