import sys
import numpy as np
import cv2
from math import sqrt
import time
from operator import itemgetter
def image2vector_list(file_name, RESOLUTION=32, AREA_SIZE=10, CHAR_HEIGHT=10, MARGIN=5, X_SCALE=1, Y_SCALE=15, SHOW_LOOP=False, SHOW_RECOGNIZED=False, SHOW_VECTORS=False):
    image = cv2.imread(file_name)
    image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_blur = cv2.GaussianBlur(image_bw, (5, 5), 0)
    image_threshhold = cv2.adaptiveThreshold(image_blur, 255, 1, 1, 11, 2)
    cleaned = image_threshhold.copy()
    contours, hierarchy = cv2.findContours(cleaned, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours_filtered = [contour for contour in contours if cv2.contourArea(contour) > AREA_SIZE and cv2.boundingRect(contour)[3] > CHAR_HEIGHT]
    contours_sorted = sorted(contours_filtered, key=lambda contour: cv2.boundingRect(contour)[0] * X_SCALE + cv2.boundingRect(contour)[1] * Y_SCALE)
    vectors = np.empty((0, RESOLUTION ** 2))
    keys = [i for i in range(48, 58)]
    ex = [0, 0, 0, 0]
    count = 0
    for index, contour in enumerate(contours_sorted):
        x, y, w, h = cv2.boundingRect(contour)
        x_ex, y_ex, w_ex, h_ex = ex
        nested = x - x_ex >= 0 and y - y_ex >= 0 and (x + w) - (x_ex + w_ex) <= 0 and (y + h) - (y_ex + h_ex) <= 0
        go_back = x - x_ex < 0 and abs(y - y_ex) < h * 0.8
        if not nested and not go_back:
            cv2.rectangle(image, (x - MARGIN, y - MARGIN), (x + w + MARGIN, y + h + MARGIN), (0, 0, 255), 2)
            roi = cleaned[y - MARGIN:y + h + MARGIN, x - MARGIN:x + w + MARGIN]
            roismall = cv2.resize(roi, (RESOLUTION, RESOLUTION))
            sample = roismall.reshape((1, RESOLUTION ** 2)).astype(bool)
            vectors = np.append(vectors, sample, 0)
            if SHOW_LOOP:
                cv2.imshow('norm', image)
                key = cv2.waitKey(0)
                if key == 27:
                    sys.exit()
                elif key in keys:
                    sample = roismall.reshape((1, 100))
                    samples = np.append(samples, sample, 0)
            ex = [x, y, w, h]
            count += 1
    if SHOW_RECOGNIZED:
        cv2.imshow('original', image)
        print("Press ESC to continue")
        if 27 == cv2.waitKey(0):
            pass
    if SHOW_VECTORS:
        for sample in vectors:
            print("===================")
            for i in range(RESOLUTION):
                for j in range(RESOLUTION):
                    if sample[i * RESOLUTION + j]:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print("")
    return vectors
def make_file_path_list(capitals):
    return [f"train_image/{capital}.png" for capital in capitals]
def make_train_set(file_path, flag):
    vector_list = image2vector_list(file_path, Y_SCALE=9, AREA_SIZE=12, CHAR_HEIGHT=12, SHOW_LOOP=False, SHOW_RECOGNIZED=False, SHOW_VECTORS=False, RESOLUTION=32)
    result = [[vector.tolist(), flag] for vector in vector_list]
    return result
def most_common(input_list):
    elems = tuple(input_list)
    return max(set(elems), key=input_list.count)
def get_euclid(trained_char_vec, input_char_vector):
    return sqrt(sum(abs(px - trained_char_vec[i]) for i, px in enumerate(input_char_vector)))
def ocr(file_path, trained_list, k, SHOW_PROGRESS=False):
    input_vectors = image2vector_list(file_path, SHOW_LOOP=False, SHOW_RECOGNIZED=False).tolist()
    result_str = ""
    for input_char_vector in input_vectors:
        proximate_k = []
        for trained_char in trained_list:
            euclid = get_euclid(trained_char[0], input_char_vector)
            if len(proximate_k) < k:
                proximate_k.append([trained_char[-1], euclid])
            else:
                proximate_k = sorted(proximate_k, key=itemgetter(1))
                proximate_k[-1] = [trained_char[-1], euclid]
        votes = [x[0] for x in proximate_k]
        elect = most_common(votes)
        if SHOW_PROGRESS:
            print(elect)
        result_str += elect
    return result_str
if __name__ == '__main__':
    t1 = time.process_time()
    image_file = 'russell.png'
    chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    training_file_path_list = make_file_path_list(chars)
    trained = [make_train_set(path, char) for path, char in zip(training_file_path_list, chars)]
    trained = [item for sublist in trained for item in sublist]
    result = ocr("russell_short.png", trained, 10, SHOW_PROGRESS=True)
    print(result)
    t2 = time.process_time()
    print(f"Process time: {t2 - t1}")