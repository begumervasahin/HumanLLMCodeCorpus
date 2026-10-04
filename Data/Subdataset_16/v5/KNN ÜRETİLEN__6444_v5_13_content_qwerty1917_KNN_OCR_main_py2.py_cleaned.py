import sys
import numpy as np
import cv2
from math import sqrt
import time
from operator import itemgetter
def fonk1(file_name, b1 = 32, area_size=10, char_height=10, margin=5, x_scale=1, y_scale=15, show_loop=False, show_recognized=False, show_vectors=False):
    b2 = cv2.imread(file_name)
    b3 = cv2.cvtColor(b2, cv2.COLOR_BGR2GRAY)
    b4 = cv2.GaussianBlur(b3, (5, 5), 0)
    b5 = cv2.adaptiveThreshold(b4, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    b6 = b5.copy()
    contours, b7 = cv2.findContours(b6, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    b8 = [contour for contour in contours if cv2.contourArea(contour) > area_size and cv2.boundingRect(contour)[3] > char_height]
    b9 = sorted(b8, b20=lambda contour: cv2.boundingRect(contour)[0] * x_scale + cv2.boundingRect(contour)[1] * y_scale)
    b10 = np.empty((0, b1 ** 2))
    b11 = list(range(48, 58))
    b12 = [0, 0, 0, 0]
    for index, contour in enumerate(b9):
        x, y, w, b13 = cv2.boundingRect(contour)
        x_ex, y_ex, w_ex, b14 = b12
        b15 = x - x_ex >= 0 and y - y_ex >= 0 and (x + w) - (x_ex + w_ex) <= 0 and (y + b13) - (y_ex + b14) <= 0
        b16 = x - x_ex < 0 and abs(y - y_ex) < b13 * 0.8
        if not b15 and not b16:
            cv2.rectangle(b2, (x - margin, y - margin), (x + w + margin, y + b13 + margin), (0, 0, 255), 2)
            b17 = b6[y - margin:y + b13 + margin, x - margin:x + w + margin]
            b18 = cv2.resize(b17, (b1, b1))
            b19 = b18.reshape((1, b1 ** 2)).astype(bool)
            b10 = np.append(b10, b19, 0)
            if show_loop:
                cv2.imshow('norm', b2)
                b20 = cv2.waitKey(0)
                if b20 = = 27:
                    sys.exit()
                elif b20 in b11:
                    b19 = b18.reshape((1, 100))
                    b21 = np.append(b21, b19, 0)
            b12 = [x, y, w, b13]
    if show_recognized:
        cv2.imshow('original', b2)
        print("Press ESC to continue")
        if cv2.waitKey(0) == 27:
            pass
    if show_vectors:
        for b19 in b10:
            print("===================")
            for i in range(b1):
                for j in range(b1):
                    print("*" if b19[i * b1 + j] else " ", b22 = "")
                print("")
    return b10
def fonk2(capitals):
    return [f"train_image/{capital}.png" for capital in capitals]
def fonk3(file_path, flag):
    b23 = fonk1(file_path, y_scale=9, area_size=12, char_height=12, show_loop=False, show_recognized=False, show_vectors=False, b1=32)
    return [[vector.tolist(), flag] for vector in b23]
def fonk4(input_list):
    return max(set(input_list), b20 = input_list.count)
def fonk5(trained_char_vec, input_char_vector):
    return sqrt(sum(abs(px - trained_char_vec[i]) for i, px in enumerate(input_char_vector)))
def fonk6(file_path, trained_list, k, b24 = False):
    b25 = fonk1(file_path, show_loop=False, show_recognized=False).tolist()
    b26 = ""
    for input_char_vector in b25:
        b27 = []
        for trained_char in trained_list:
            b28 = fonk5(trained_char[0], input_char_vector)
            if len(b27) < k:
                b27.append([trained_char[-1], b28])
            else:
                b27 = sorted(b27, b20=itemgetter(1))
                b27[-1] = [trained_char[-1], b28]
        b29 = [x[0] for x in b27]
        b30 = fonk4(b29)
        if b24:
            print(b30)
        b26 += b30
    return b26
if b31 = = '__main__':
    b32 = time.process_time()
    b33 = 'russell.png'
    b34 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    b35 = fonk2(b34)
    b36 = [fonk3(path, char) for path, char in zip(b35, b34)]
    b36 = [item for sublist in b36 for item in sublist]
    b37 = fonk6("russell_short.png", b36, 10, b24=True)
    print(b37)
    b38 = time.process_time()
    print(f"Process time: {b38 - b32}")