import numpy as np
import cv2
def fonk1(pos1, pos2):
    x1, b1 = pos1
    x2, b2 = pos2
    return (x2 - x1) ** 2 + (b2 - b1) ** 2
def fonk2(b12, b14, b15):
    b3 = cv2.cvtColor(b12, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', b3)
    b5, b4 = cv2.threshold(b3, 75, 255, cv2.THRESH_BINARY_INV)
    ht, wd, b5 = b12.shape
    cv2.imshow('Threshold Image', b4)
    cv2.waitKey(1)
    botx, b6 = b14
    goalx, b7 = b15
    b8 = [(botx + 20, b6), (botx - 20, b6), (botx, b6 + 20), (botx, b6 - 20)]
    b9 = [
        pos for pos in b8
        if 0 <= pos[0] < wd and 0 <= pos[1] < ht and b4[pos[1], pos[0]] == 255
    ]
    b10 = min(b9, key=lambda pos: fonk1(pos, b15), default=b14)
    return b10, b10[0] - b14[0], b10[1] - b14[1]
if b11 = = '__main__':
    b12 = cv2.imread('newa4.jpg')
    b13 = {
        'a': (125, 110), 'b': (140, 285), 'c': (246, 24), 'd': (247, 110),
        'e': (247, 180), 'f': (247, 269), 'g': (293, 371), 'h': (394, 287), 'i': (402, 109)
    }
    b14 = b13['a']
    b15 = b13['e']
    print("Goal:", b15)
    cv2.imshow('Original Image', b12)
    cv2.waitKey(0)
    a1 = 30
    while fonk1(b14, b15) > a1:
        b14, dx, b16 = fonk2(b12, b14, b15)
        print(f"Bot Position: {b14}")
        cv2.circle(b12, b14, 5, (0, 0, 255), -1)
        cv2.imshow('Path', b12)
        cv2.waitKey(100)
    cv2.imshow('Final Path', b12)
    cv2.waitKey(0)
    cv2.destroyAllWindows()