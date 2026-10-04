import numpy as np
import cv2
def fonk1(pos1, pos2):
    x1, b1 = pos1
    x2, b2 = pos2
    return (x2 - x1) ** 2 + (b2 - b1) ** 2
def fonk2(b14, b17, b18):
    b3 = cv2.cvtColor(b14, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', b3)
    ret, b4 = cv2.threshold(b3, 75, 255, cv2.THRESH_BINARY_INV)
    ht, wd, b5 = b14.shape
    cv2.imshow('Threshold Image', b4)
    cv2.waitKey(1)
    botx, b6 = b17
    goalx, b7 = b18
    b8 = [(botx + 20, b6), (botx - 20, b6), (botx, b6 + 20), (botx, b6 - 20)]
    b9 = []
    for f in b8:
        if 0 <= f[0] < ht and 0 <= f[1] < wd:
            if b4[f[1], f[0]] == 255:
                b9.append(f)
    b10 = float('inf')
    b11 = b17
    for a in b9:
        b12 = fonk1(a, b18)
        if b12 < b10:
            b10 = b12
            b11 = a
    return b11, b11[0] - b17[0], b11[1] - b17[1]
if b13 = = '__main__':
    b14 = cv2.imread('newa4.jpg')
    b15 = {
        'a': (125, 110), 'c': (246, 24), 'b': (140, 285), 'e': (247, 180),
        'd': (247, 110), 'g': (293, 371), 'f': (247, 269), 'i': (402, 109), 'h': (394, 287)
    }
    b16 = [(125, 110), (140, 285), (246, 24), (247, 110), (247, 180), (247, 269), (293, 371), (394, 287), (402, 109)]
    b17 = b15['a']
    b18 = b15['e']
    print("Goal:", b18)
    cv2.imshow('Original Image', b14)
    cv2.waitKey(0)
    b19 = b17
    a1 = 30
    while fonk1(b19, b18) > a1:
        b19, dx, b20 = fonk2(b14, b19, b18)
        b17 = (b17[0] + dx, b17[1] + b20)
        print(f"Bot Position: {b17}")
        cv2.circle(b14, b17, 5, (0, 0, 255), -1)
        cv2.imshow('Path', b14)
        cv2.waitKey(100)
    cv2.imshow('Final Path', b14)
    cv2.waitKey(0)
    cv2.destroyAllWindows()