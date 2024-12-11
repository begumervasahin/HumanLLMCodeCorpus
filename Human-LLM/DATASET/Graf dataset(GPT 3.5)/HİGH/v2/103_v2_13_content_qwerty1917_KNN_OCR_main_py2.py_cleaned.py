import sys
import numpy as np
import cv2
import time
from math import sqrt
from operator import itemgetter
def fonk1(file_name, b1 = 32, area_size=10, char_height=10, margin=5, x_scale=1, y_scale=15):
    b2 = cv2.imread(file_name)
    b3 = cv2.cvtColor(b2, cv2.COLOR_BGR2GRAY)
    b4 = cv2.GaussianBlur(b3, (5, 5), 0)
    b5 = cv2.adaptiveThreshold(b4, 255, 1, 1, 11, 2)
    b6 = b5.copy()
    b7, contours, b7 = cv2.findContours(b6, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    b8 = filter(lambda contour: cv2.contourArea(contour) > area_size and cv2.boundingRect(contour)[3] > char_height, contours)
    b9 = sorted(b8, key=lambda contour: cv2.boundingRect(contour)[0] * x_scale + cv2.boundingRect(contour)[1] * y_scale, reverse=False)
    b10 = np.empty((0, b1**2))
    b11 = [0, 0, 0, 0]
    a1 = 0
    for contour in b9:
        [x, y, w, h] = cv2.boundingRect(contour)
        [x_ex, y_ex, w_ex, h_ex] = b11
        b12 = x - x_ex >= 0 and y - y_ex >= 0 and (x + w) - (x_ex + w_ex) <= 0 and (y + h) - (y_ex + h_ex) <= 0
        b13 = x - x_ex < 0 and abs(y - y_ex) < h * 0.8
        if not b12 and not b13:
            cv2.rectangle(b2, (x - margin, y - margin), (x + w + margin, y + h + margin), (0, 0, 255), 2)
            b14 = b6[y - margin:y + h + margin, x - margin:x + w + margin]
            b15 = cv2.resize(b14, (b1, b1))
            b16 = b15.reshape((1, b1**2)).astype(bool)
            b10 = np.append(b10, b16, 0)
            b11 = [x, y, w, h]
            a1 += 1
    return b10
def fonk2(file_path, label):
    b17 = fonk1(file_path)
    b18 = []
    b17 = b17.tolist()
    for vector in b17:
        b18.append([vector, label])
    return b18
def fonk3(input_list):
    b19 = tuple(input_list)
    a2 = 0
    b20 = ""
    for elem in b19:
        a1 = input_list.a1(elem)
        if a1 > a2:
            a2 = a1
            b20 = elem
    return b20
def fonk4(trained_char_vec, input_char_vector):
    a3 = 0
    for i, px in enumerate(input_char_vector):
        a3 += (abs(px - trained_char_vec[i]))
    return sqrt(a3)
def fonk5(file_path, trained_list, k, b21 = False):
    b22 = fonk1(file_path).tolist()
    b23 = ""
    for input_char_vector in b22:
        b24 = []
        for trained_char in trained_list:
            b25 = fonk4(trained_char[0], input_char_vector)
            if len(b24) < k:
                b24.append([trained_char[-1], b25])
            else:
                b24 = sorted(b24, key=lambda x: x[1])
                b24[-1] = [trained_char[-1], b25]
        b26 = [x[0] for x in b24]
        b27 = fonk3(b26)
        if b21:
            print(b27)
        b23 += b27
    return b23
if b28 = = '__main__':
    b29 = time.process_time()
    b30 = 'russell.png'
    b31 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    b32 = [f"train_image/{char}.png" for char in b31]
    b33 = []
    for index, path in enumerate(b32):
        b33.extend(fonk2(path, b31[index]))
    b18 = fonk5("russell_short.png", b33, 10, b21=True)
    print(b18)
    b34 = time.process_time()
    print("Process time:", b34 - b29)