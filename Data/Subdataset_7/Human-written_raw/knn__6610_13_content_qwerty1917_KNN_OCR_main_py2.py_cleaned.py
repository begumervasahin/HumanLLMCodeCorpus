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
    _, contours, b15 = cv2.findContours(b14, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    b16 = filter(lambda contour:cv2.contourArea(contour) > b2 and cv2.boundingRect(contour)[3] > b3, contours)
    b17 = sorted(b16, b26=lambda contour:cv2.boundingRect(contour)[0]*b5 + cv2.boundingRect(contour)[1]*b6, reverse=False)
    b18 = np.empty((0, b1**2))
    b19 = [i for i in range(48,58)]
    b20 = [0,0,0,0]
    a1 = 0
    for index, contour in enumerate(b17):
        [x, y, w, h] = cv2.boundingRect(contour)
        [x_ex, y_ex, w_ex, h_ex] = b20
        b21 = x-x_ex >= 0 and y-y_ex>=0 and (x+w)-(x_ex+w_ex) <= 0 and (y+h)-(y_ex+h_ex) <= 0
        b22 = x-x_ex < 0 and abs(y-y_ex) < h*0.8
        if not b21 and not b22:
            cv2.rectangle(b10, (x - b4, y - b4), (x + w + b4, y + h + b4), (0, 0, 255), 2)
            b23 = b14[y - b4:y + h + b4, x - b4:x + w + b4]
            b24 = cv2.resize(b23, (b1, b1))
            b25 = b24.reshape((1, b1**2)).astype(bool)
            b18 = np.append(b18, b25, 0)
            if b7:
                cv2.imshow('norm',b10)
                b26 = cv2.waitKey(0)
                if b26 = = b28:
                    sys.exit()
                elif b26 in b19:
                    b25 = b24.reshape((1,100))
                    b27 = np.append(b27,b25,0)
            b20 = [x, y, w, h]
            a1 += 1
    if b8:
        cv2.imshow('original', b10)
        print("print esc to continue")
        if b28 = = cv2.waitKey(0):
            pass
    if b9 = = True:
        for b25 in b18:
            print("===================")
            for i in range(b1):
                for j in range(b1):
                    if b25[i*b1+j] == True:
                        print("
                    else:
                        print(" ", b29 = "")
                print("")
    return b18
def fonk2(capitals):
    b30 = []
    for capital in capitals:
        b30.append("train_image/" + capital + ".png")
    return b30
def fonk3(file_path, flag):
    b31 = fonk1(file_path,
                                    b6 = 9,
                                    b2 = 12,
                                    b3 = 12,
                                    b7 = False,
                                    b8 = False,
                                    b9 = False,
                                    b1 = 32)
    b30 = []
    b31 = b31.tolist()
    for vector in b31:
        b30.append([vector, flag])
    return b30
def fonk4(input_list):
    b32 = tuple(input_list)
    a2 = 0
    b33 = ""
    for elem in b32:
        a1 = input_list.a1(elem)
        if a1 > a2:
            a2 = a1
            b33 = elem
    return b33
def fonk5(trained_char_vec, input_char_vector):
    a3 = 0
    for i, px in enumerate(input_char_vector):
        a3 += (abs(px-trained_char_vec[i]))
    return sqrt(a3)
def fonk6(file_path, trained_list, k, b34 = False):
    b35 = fonk1(file_path, b7=False, b8=False).tolist()
    b36 = ""
    for input_char_vector in b35:
        b37 = []
        for trained_char in trained_list:
            b38 = fonk5(trained_char[0], input_char_vector)
            if len(b37) < k:
                b37.append([trained_char[-1], b38])
            else:
                b37 = sorted(b37, b26=lambda x:x[1])
                b37[-1] = [trained_char[-1], b38]
        b39 = [x[0] for x in b37]
        b40 = fonk4(b39)
        if b34:
            print(b40)
        b36 += b40
    return b36
if b41 = = '__main__':
    b42 = time.process_time()
    b43 = 'russell.png'
    b44 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    b45 = fonk2(b44)
    b46 = []
    for index, path in enumerate(b45):
         b46.extend(fonk3(path, b44[index]))
    b30 = fonk6("russell_short.png", b46, 10, b34=True)
    print(b30)
    b47 = time.process_time()
    print("process time: " + str(b47-b42))