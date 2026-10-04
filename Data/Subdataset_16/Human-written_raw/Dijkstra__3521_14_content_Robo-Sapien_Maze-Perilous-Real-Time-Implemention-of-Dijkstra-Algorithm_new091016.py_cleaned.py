import numpy as np
import cv2
def fonk1((x1,y1),(x2,y2)):
    return ((x2-x1)**2+(y2-y1)**2)
def fonk2(b11,b14,b15):
    b1 = cv2.cvtColor(b11,cv2.COLOR_BGR2GRAY)
    cv2.imshow('b1',b1)
    ret,b2 = cv2.threshold(b1,75,255,cv2.THRESH_BINARY_INV)
    ht,wd,b3 = b11.shape
    cv2.imshow('thresh',b2)
    cv2.waitKey(1)
    botx,b4 = b14[0],b14[1]
    goalx,b5 = b15[0],b15[1]
    b6 = [(botx+20,b4),(botx-20,b4),(botx,b4+20),(botx,b4-20)]
    b7 = []
    for f in b6:
        if(f[0]<ht and f[1]<wd):
            if(b2[f[1],f[0]]==255):
                b7.append(f)
    a1 = 99999999999
    b8 = b14
    for a in b7:
        b9 = fonk1(a,b15)
        if(b9<a1):
            a1 = b9
            b8 = a
    return (b8,b8[0]-b14[0],b8[1]-b14[1])
if b10 = ='__main__':
    b11 = cv2.imread('newa4.jpg')
    b12 = {'a': (125, 110), 'c': (246, 24), 'b': (140, 285), 'e': (247, 180), 'd': (247, 110), 'g': (293, 371), 'f': (247, 269), 'i': (402, 109), 'h': (394, 287)}
    b13 = [(125,110),(140,285),(246,24),(247,110),(247,180),(247,269),(293,371),(394,287),(402,109)]
    b14 = b12['a']
    b15 = b12['e']
    print "b15 = ",b15
    cv2.imshow('image',b11)
    cv2.waitKey(0) & 0xFF
    b16 = b14
    a2 = 30
    cv2.imshow('image',b11)
    cv2.waitKey(100)
    cv2.imshow('final',b11)
    cv2.waitKey(0)