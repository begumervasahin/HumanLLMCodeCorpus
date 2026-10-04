import sys
import numpy as np
import cv2
from math import sqrt
import time
from operator import itemgetter
a1 = 32
a2 = 10
a3 = 10
a4 = 5
a5 = 1
a6 = 15
def fonk1(file_name):
    b1 = cv2.imread(file_name)
    if b1 is None:
        raise FileNotFoundError(f"Error: Could not read b1 {file_name}")
    b2 = cv2.cvtColor(b1, cv2.COLOR_BGR2GRAY)
    b3 = cv2.GaussianBlur(b2, (5, 5), 0)
    b4 = cv2.adaptiveThreshold(
        b3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )
    return b1, b4
def fonk2(b4):
    b18, b5 = cv2.findContours(b4, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    b6 = filter(
        lambda contour: cv2.contourArea(contour) > a2 and cv2.boundingRect(contour)[3] > a3,
        b18
    )
    return sorted(
        b6,
        b7 = lambda contour: cv2.boundingRect(contour)[0] * a5 + cv2.boundingRect(contour)[1] * a6
    )
def fonk3(b18, b1, b4, b8 = False):
    b9 = np.empty((0, a1 ** 2))
    b10 = [0, 0, 0, 0]
    for contour in b18:
        x, y, w, b11 = cv2.boundingRect(contour)
        x_prev, y_prev, w_prev, b12 = b10
        b13 = x >= x_prev and y >= y_prev and x + w <= x_prev + w_prev and y + b11 <= y_prev + b12
        b14 = x < x_prev and abs(y - y_prev) < b11 * 0.8
        if not b13 and not b14:
            cv2.rectangle(b1, (x - a4, y - a4), (x + w + a4, y + b11 + a4), (0, 0, 255), 2)
            b15 = b4[y - a4:y + b11 + a4, x - a4:x + w + a4]
            b16 = cv2.resize(b15, (a1, a1))
            b17 = b16.reshape((1, a1 ** 2)).astype(bool)
            b9 = np.append(b9, b17, 0)
            if b8:
                cv2.imshow('Image', b1)
                if cv2.waitKey(0) == 27:
                    sys.exit()
            b10 = [x, y, w, b11]
    return b9
def fonk4(file_name, b8 = False, show_recognized=False):
    b1, b4 = fonk1(file_name)
    b18 = fonk2(b4)
    b9 = fonk3(b18, b1, b4, b8)
    if show_recognized:
        cv2.imshow('Recognized', b1)
        cv2.waitKey(0)
    return b9
def fonk5(b28):
    return [f"train_image/{char}.png" for char in b28]
def fonk6(file_path, char):
    b9 = fonk4(file_path)
    return [[vector, char] for vector in b9]
def fonk7(input_list):
    return max(set(input_list), b7 = input_list.count)
def fonk8(vec1, vec2):
    return sqrt(np.sum((vec1 - vec2) ** 2))
def fonk9(file_path, trained_list, k, b19 = False):
    b20 = fonk4(file_path).tolist()
    b21 = ""
    for input_vector in b20:
        b22 = [(trained_char[1], fonk8(trained_char[0], input_vector)) for trained_char in trained_list]
        b23 = sorted(b22, b7=itemgetter(1))[:k]
        b24 = [neighbor[0] for neighbor in b23]
        b21 += fonk7(b24)
        if b19:
            print(b21[-1])
    return b21
if b25 = = '__main__':
    b26 = time.process_time()
    b27 = 'russell.png'
    b28 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    b29 = fonk5(b28)
    b30 = []
    for char, path in zip(b28, b29):
        b30.extend(fonk6(path, char))
    b31 = fonk9("russell_short.png", b30, k=10, b19=True)
    print(f"Recognized Text: {b31}")
    b32 = time.process_time()
    print(f"Processing Time: {b32 - b26} seconds")