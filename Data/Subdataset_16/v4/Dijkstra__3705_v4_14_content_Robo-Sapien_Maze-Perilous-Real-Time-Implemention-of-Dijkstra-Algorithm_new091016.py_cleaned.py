import numpy as np
import cv2
def fonk1(pos1, pos2):
    x1, b1 = pos1
    x2, b2 = pos2
    return (x2 - x1) ** 2 + (b2 - b1) ** 2
def fonk2(b11, b13, b14):
    b3 = cv2.cvtColor(b11, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', b3)
    b5, b4 = cv2.threshold(b3, 75, 255, cv2.THRESH_BINARY_INV)
    ht, wd, b5 = b11.shape
    cv2.imshow('Threshold Image', b4)
    cv2.waitKey(1)
    botx, b6 = b13
    goalx, b7 = b14
    b8 = [(botx + 20, b6), (botx - 20, b6), (botx, b6 + 20), (botx, b6 - 20)]
    b9 = [
        pos for pos in b8
        if 0 <= pos[0] < ht and 0 <= pos[1] < wd and b4[pos[1], pos[0]] == 255
    ]
    b10 = min(b9, key=lambda pos: fonk1(pos, b14), default=b13)
    return b10, b10[0] - b13[0], b10[1] - b13[1]
def fonk3():
    b11 = cv2.imread('newa4.jpg')
    b12 = {
        'a': (125, 110), 'b': (140, 285), 'c': (246, 24), 'd': (247, 110),
        'e': (247, 180), 'f': (247, 269), 'g': (293, 371), 'h': (394, 287), 'i': (402, 109)
    }
    b13 = b12['a']
    b14 = b12['e']
    print("Goal:", b14)
    cv2.imshow('Original Image', b11)
    cv2.waitKey(0)
    a1 = 30
    while fonk1(b13, b14) > a1:
        b13, dx, b15 = fonk2(b11, b13, b14)
        print(f"Bot Position: {b13}")
        cv2.circle(b11, b13, 5, (0, 0, 255), -1)
        cv2.imshow('Path', b11)
        cv2.waitKey(100)
    cv2.imshow('Final Path', b11)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b16 = = '__main__':
    fonk3()