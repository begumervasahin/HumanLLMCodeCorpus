import sys
import numpy as np
import cv2
from math import sqrt
import time
from operator import itemgetter
def fonk1(file_name,
                      b1 = 32,
                      b2 = 10,
                      b3 = 10,
                      b4 = 5,
                      b5 = 1,
                      b6 = 15,
                      b7 = False,
                      b8 = False,
                      b9 = False):
    b10 = cv2.imread(file_name)
    b11 = cv2.cvtColor(b10, cv2.COLOR_BGR2GRAY)
    b12 = cv2.GaussianBlur(b11, (5, 5), 0)
    b13 = cv2.adaptiveThreshold(b12, 255, 1, 1, 11, 2)
    b14 = b13.copy()
    contours, b15 = cv2.findContours(b14, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    b16 = filter(lambda contour: cv2.contourArea(contour) > b2 and cv2.boundingRect(contour)[3] > b3, contours)
    b17 = sorted(b16, b26=lambda contour: cv2.boundingRect(contour)[0] * b5 + cv2.boundingRect(contour)[1] * b6, reverse=False)
    b18 = np.empty((0, b1 ** 2))
    b19 = [i for i in range(48, 58)]
    b20 = [0, 0, 0, 0]
    a1 = 0
    for index, contour in enumerate(b17):
        [x, y, w, h] = cv2.boundingRect(contour)
        [x_ex, y_ex, w_ex, h_ex] = b20
        b21 = x - x_ex >= 0 and y - y_ex >= 0 and (x + w) - (x_ex + w_ex) <= 0 and (y + h) - (y_ex + h_ex) <= 0
        b22 = x - x_ex < 0 and abs(y - y_ex) < h * 0.8
        if not b21 and not b22:
            cv2.rectangle(b10, (x - b4, y - b4), (x + w + b4, y + h + b4), (0, 0, 255), 2)
            b23 = b14[y - b4:y + h + b4, x - b4:x + w + b4]
            b24 = cv2.resize(b23, (b1, b1))
            b25 = b24.reshape((1, b1 ** 2)).astype(bool)
            b18 = np.append(b18, b25, 0)
            if b7:
                cv2.imshow('norm', b10)
                b26 = cv2.waitKey(0)
                if b26 = = 27:
                    sys.exit()
                elif b26 in b19:
                    b25 = b24.reshape((1, b1 ** 2))
                    b18 = np.append(b18, b25, 0)
            b20 = [x, y, w, h]
            a1 += 1
    if b8:
        cv2.imshow('original', b10)
        print("Press ESC to continue")
        if cv2.waitKey(0) == 27:
            pass
    if b9:
        for b25 in b18:
            print("===================")
            for i in range(b1):
                for j in range(b1):
                    if b25[i * b1 + j]:
                        print("1", b27 = "")
                    else:
                        print("0", b27 = "")
                print("")
    return b18
def fonk2(capitals):
    b28 = []
    for capital in capitals:
        b28.append("train_image/" + capital + ".png")
    return b28
def fonk3(file_path, flag):
    b29 = fonk1(file_path,
                                    b6 = 9,
                                    b2 = 12,
                                    b3 = 12,
                                    b7 = False,
                                    b8 = False,
                                    b9 = False,
                                    b1 = 32)
    b28 = []
    b29 = b29.tolist()
    for vector in b29:
        b28.append([vector, flag])
    return b28
def fonk4(input_list):
    b30 = tuple(input_list)
    a2 = 0
    b31 = ""
    for elem in b30:
        a1 = input_list.a1(elem)
        if a1 > a2:
            a2 = a1
            b31 = elem
    return b31
def fonk5(trained_char_vec, input_char_vector):
    a3 = 0
    for i, px in enumerate(input_char_vector):
        a3 += abs(px - trained_char_vec[i])
    return sqrt(a3)
def fonk6(file_path, trained_list, k, b32 = False):
    b33 = fonk1(file_path, b7=False, b8=False).tolist()
    b34 = ""
    for input_char_vector in b33:
        b35 = []
        for trained_char in trained_list:
            b36 = fonk5(trained_char[0], input_char_vector)
            if len(b35) < k:
                b35.append([trained_char[-1], b36])
            else:
                b35 = sorted(b35, b26=lambda x: x[1])
                b35[-1] = [trained_char[-1], b36]
        b37 = [x[0] for x in b35]
        b38 = fonk4(b37)
        if b32:
            print(b38)
        b34 += b38
    return b34
if b39 = = '__main__':
    b40 = time.process_time()
    b41 = 'russell.png'
    b42 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    b43 = fonk2(b42)
    b44 = []
    for index, path in enumerate(b43):
        b44.extend(fonk3(path, b42[index]))
    b28 = fonk6("russell_short.png", b44, 10, b32=True)
    print(b28)
    b45 = time.process_time()
    print("Process time: " + str(b45 - b40))