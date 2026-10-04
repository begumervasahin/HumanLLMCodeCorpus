import sys
import numpy as np
import cv2
from math import sqrt
import time
from operator import itemgetter
def image2vector_list(file_name, resolution=32, area_size=10, char_height=10, margin=5, x_scale=1, y_scale=15, show_loop=False, show_recognized=False, show_vectors=False):
    image = cv2.imread(file_name)
    image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_blur = cv2.GaussianBlur(image_bw, (5, 5), 0)
    image_thresh = cv2.adaptiveThreshold(image_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    cleaned = image_thresh.copy()
    contours, hierarchy = cv2.findContours(cleaned, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours_filtered = [contour for contour in contours if cv2.contourArea(contour) > area_size and cv2.boundingRect(contour)[3] > char_height]
    contours_sorted = sorted(contours_filtered, key=lambda contour: cv2.boundingRect(contour)[0] * x_scale + cv2.boundingRect(contour)[1] * y_scale)
    vectors = np.empty((0, resolution ** 2))
    keys = list(range(48, 58))
    ex = [0, 0, 0, 0]
    for index, contour in enumerate(contours_sorted):
        x, y, w, h = cv2.boundingRect(contour)
        x_ex, y_ex, w_ex, h_ex = ex
        nested = x - x_ex >= 0 and y - y_ex >= 0 and (x + w) - (x_ex + w_ex) <= 0 and (y + h) - (y_ex + h_ex) <= 0
        go_back = x - x_ex < 0 and abs(y - y_ex) < h * 0.8
        if not nested and not go_back:
            cv2.rectangle(image, (x - margin, y - margin), (x + w + margin, y + h + margin), (0, 0, 255), 2)
            roi = cleaned[y - margin:y + h + margin, x - margin:x + w + margin]
            roismall = cv2.resize(roi, (resolution, resolution))
            sample = roismall.reshape((1, resolution ** 2)).astype(bool)
            vectors = np.append(vectors, sample, 0)
            if show_loop:
                cv2.imshow('norm', image)
                key = cv2.waitKey(0)
                if key == 27:
                    sys.exit()
                elif key in keys:
                    sample = roismall.reshape((1, 100))
                    samples = np.append(samples, sample, 0)
            ex = [x, y, w, h]
    if show_recognized:
        cv2.imshow('original', image)
        print("Press ESC to continue")
        if cv2.waitKey(0) == 27:
            pass
    if show_vectors:
        for sample in vectors:
            print("===================")
            for i in range(resolution):
                for j in range(resolution):
                    print("*" if sample[i * resolution + j] else " ", end="")
                print("")
    return vectors
def make_file_path_list(capitals):
    return [f"train_image/{capital}.png" for capital in capitals]
def make_train_set(file_path, flag):
    vector_list = image2vector_list(file_path, y_scale=9, area_size=12, char_height=12, show_loop=False, show_recognized=False, show_vectors=False, resolution=32)
    return [[vector.tolist(), flag] for vector in vector_list]
def most_common(input_list):
    return max(set(input_list), key=input_list.count)
def get_euclid(trained_char_vec, input_char_vector):
    return sqrt(sum(abs(px - trained_char_vec[i]) for i, px in enumerate(input_char_vector)))
def ocr(file_path, trained_list, k, show_progress=False):
    input_vectors = image2vector_list(file_path, show_loop=False, show_recognized=False).tolist()
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
        if show_progress:
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
    result = ocr("russell_short.png", trained, 10, show_progress=True)
    print(result)
    t2 = time.process_time()
    print(f"Process time: {t2 - t1}")