import sys
import numpy as np
import cv2
import time
from math import sqrt
from operator import itemgetter
def preprocess_image(file_name, resolution=32, area_size=10, char_height=10, margin=5, x_scale=1, y_scale=15):
    image = cv2.imread(file_name)
    image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_blur = cv2.GaussianBlur(image_bw, (5, 5), 0)
    image_threshold = cv2.adaptiveThreshold(image_blur, 255, 1, 1, 11, 2)
    cleaned = image_threshold.copy()
    _, contours, _ = cv2.findContours(cleaned, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours_filtered = filter(lambda contour: cv2.contourArea(contour) > area_size and cv2.boundingRect(contour)[3] > char_height, contours)
    contours_sorted = sorted(contours_filtered, key=lambda contour: cv2.boundingRect(contour)[0] * x_scale + cv2.boundingRect(contour)[1] * y_scale, reverse=False)
    vectors = np.empty((0, resolution**2))
    ex = [0, 0, 0, 0]
    count = 0
    for contour in contours_sorted:
        [x, y, w, h] = cv2.boundingRect(contour)
        [x_ex, y_ex, w_ex, h_ex] = ex
        nested = x - x_ex >= 0 and y - y_ex >= 0 and (x + w) - (x_ex + w_ex) <= 0 and (y + h) - (y_ex + h_ex) <= 0
        go_back = x - x_ex < 0 and abs(y - y_ex) < h * 0.8
        if not nested and not go_back:
            cv2.rectangle(image, (x - margin, y - margin), (x + w + margin, y + h + margin), (0, 0, 255), 2)
            roi = cleaned[y - margin:y + h + margin, x - margin:x + w + margin]
            roismall = cv2.resize(roi, (resolution, resolution))
            sample = roismall.reshape((1, resolution**2)).astype(bool)
            vectors = np.append(vectors, sample, 0)
            ex = [x, y, w, h]
            count += 1
    return vectors
def make_training_set(file_path, label):
    vector_list = preprocess_image(file_path)
    result = []
    vector_list = vector_list.tolist()
    for vector in vector_list:
        result.append([vector, label])
    return result
def most_common(input_list):
    elems = tuple(input_list)
    biggest_count = 0
    most_common_elem = ""
    for elem in elems:
        count = input_list.count(elem)
        if count > biggest_count:
            biggest_count = count
            most_common_elem = elem
    return most_common_elem
def get_euclidean_distance(trained_char_vec, input_char_vector):
    ssq = 0
    for i, px in enumerate(input_char_vector):
        ssq += (abs(px - trained_char_vec[i]))
    return sqrt(ssq)
def ocr(file_path, trained_list, k, show_progress=False):
    input_vectors = preprocess_image(file_path).tolist()
    result_str = ""
    for input_char_vector in input_vectors:
        proximate_k = []
        for trained_char in trained_list:
            euclid = get_euclidean_distance(trained_char[0], input_char_vector)
            if len(proximate_k) < k:
                proximate_k.append([trained_char[-1], euclid])
            else:
                proximate_k = sorted(proximate_k, key=lambda x: x[1])
                proximate_k[-1] = [trained_char[-1], euclid]
        votes = [x[0] for x in proximate_k]
        elect = most_common(votes)
        if show_progress:
            print(elect)
        result_str += elect
    return result_str
if __name__ == '__main__':
    t1 = time.process_time()
    image_file = 'russell.png'
    chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    training_file_path_list = [f"train_image/{char}.png" for char in chars]
    trained = []
    for index, path in enumerate(training_file_path_list):
        trained.extend(make_training_set(path, chars[index]))
    result = ocr("russell_short.png", trained, 10, show_progress=True)
    print(result)
    t2 = time.process_time()
    print("Process time:", t2 - t1)