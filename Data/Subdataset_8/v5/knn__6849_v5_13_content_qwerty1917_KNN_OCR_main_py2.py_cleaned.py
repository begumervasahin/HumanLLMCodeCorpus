import sys
import cv2
import numpy as np
import time
from math import sqrt
def image_to_vector_list(file_name, RESOLUTION=32, AREA_SIZE=10, CHAR_HEIGHT=10, MARGIN=5, X_SCALE=1, Y_SCALE=15, SHOW_LOOP=False, SHOW_RECOGNIZED=False, SHOW_VECTORS=False):
    image = cv2.imread(file_name)
    image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_blur = cv2.GaussianBlur(image_bw, (5, 5), 0)
    image_threshold = cv2.adaptiveThreshold(image_blur, 255, 1, 1, 11, 2)
    cleaned = image_threshold.copy()
    _, contours, _ = cv2.findContours(cleaned, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    filtered_contours = [contour for contour in contours if cv2.contourArea(contour) > AREA_SIZE and cv2.boundingRect(contour)[3] > CHAR_HEIGHT]
    sorted_contours = sorted(filtered_contours, key=lambda contour: cv2.boundingRect(contour)[0] * X_SCALE + cv2.boundingRect(contour)[1] * Y_SCALE, reverse=False)
    vectors = np.empty((0, RESOLUTION ** 2))
    for index, contour in enumerate(sorted_contours):
        [x, y, w, h] = cv2.boundingRect(contour)
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
            elif 48 <= key <= 57:
                sample = roismall.reshape((1, 100))
    if SHOW_RECOGNIZED:
        cv2.imshow('original', image)
        print("Press esc to continue")
        if cv2.waitKey(0) == 27:
            pass
    if SHOW_VECTORS:
        for sample in vectors:
            print("===================")
            for i in range(RESOLUTION):
                for j in range(RESOLUTION):
                    print("
                print("")
    return vectors
def make_file_path_list(capitals):
    return ["train_image/" + capital + ".png" for capital in capitals]
def make_training_set(file_path, flag):
    vector_list = image_to_vector_list(file_path, Y_SCALE=9, AREA_SIZE=12, CHAR_HEIGHT=12, SHOW_LOOP=False, SHOW_RECOGNIZED=False, SHOW_VECTORS=False, RESOLUTION=32)
    return [[vector.tolist(), flag] for vector in vector_list]
def most_common(input_list):
    return max(set(input_list), key=input_list.count)
def calculate_euclidean(trained_char_vec, input_char_vector):
    return sqrt(sum((abs(px - trained_char_vec[i]) for i, px in enumerate(input_char_vector))))
def ocr(file_path, trained_list, k, SHOW_PROGRESS=False):
    input_vectors = image_to_vector_list(file_path, SHOW_LOOP=False, SHOW_RECOGNIZED=False)
    result_str = ""
    for input_char_vector in input_vectors:
        proximate_k = []
        for trained_char in trained_list:
            euclid = calculate_euclidean(trained_char[0], input_char_vector)
            if len(proximate_k) < k:
                proximate_k.append([trained_char[-1], euclid])
            else:
                proximate_k = sorted(proximate_k, key=lambda x: x[1])
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
    chars = [chr(i) for i in range(65, 91)]
    training_file_path_list = make_file_path_list(chars)
    trained = []
    for index, path in enumerate(training_file_path_list):
        trained.extend(make_training_set(path, chars[index]))
    result = ocr("russell_short.png", trained, 10, SHOW_PROGRESS=True)
    print(result)
    t2 = time.process_time()
    print("process time: " + str(t2 - t1))