import numpy as np
import cv2
def fonk1(pos1, pos2):
    x1, b1 = pos1
    x2, b2 = pos2
    return (x2 - x1) ** 2 + (b2 - b1) ** 2
def fonk2(b10, b12, b13):
    b3 = cv2.cvtColor(b10, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', b3)
    b5, b4 = cv2.threshold(b3, 75, 255, cv2.THRESH_BINARY_INV)
    ht, wd, b5 = b10.shape
    cv2.imshow('Threshold Image', b4)
    cv2.waitKey(1)
    botx, b6 = b12
    b7 = [
        (botx + 20, b6), (botx - 20, b6),
        (botx, b6 + 20), (botx, b6 - 20)
    ]
    b8 = [
        pos for pos in b7
        if 0 <= pos[0] < ht and 0 <= pos[1] < wd and b4[pos[1], pos[0]] == 255
    ]
    b9 = min(b8, key=lambda pos: fonk1(pos, b13), default=b12)
    return b9, b9[0] - b12[0], b9[1] - b12[1]
def fonk3():
    b10 = cv2.imread('newa4.jpg')
    b11 = {
        'a': (125, 110), 'b': (140, 285), 'c': (246, 24), 'd': (247, 110),
        'e': (247, 180), 'f': (247, 269), 'g': (293, 371), 'h': (394, 287), 'i': (402, 109)
    }
    b12 = b11['a']
    b13 = b11['e']
    print("Goal:", b13)
    cv2.imshow('Original Image', b10)
    cv2.waitKey(0)
    a1 = 30
    while fonk1(b12, b13) > a1:
        b12, dx, b14 = fonk2(b10, b12, b13)
        print(f"Bot Position: {b12}")
        cv2.circle(b10, b12, 5, (0, 0, 255), -1)
        cv2.imshow('Path', b10)
        cv2.waitKey(100)
    cv2.imshow('Final Path', b10)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b15 = = '__main__':
    fonk3()