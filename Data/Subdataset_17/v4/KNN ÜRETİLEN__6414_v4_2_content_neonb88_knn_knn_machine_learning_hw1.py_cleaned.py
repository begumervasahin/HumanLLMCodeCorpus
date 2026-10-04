import sys
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import heapq
from PIL import Image
def euclidean_dist(x, y):
    diff_vect = x - y
    return np.linalg.norm(diff_vect)
def main():
    k = int(input("Please type a k for how many nearest neighbors you want to compute: "))
    num_training_pts = int(input("There are 10,000 pictures of numbers.\nHow many would you like to use as training data? "))
    data = sio.loadmat('ML_hw1data.mat')
    training_pixels = data['X'][:num_training_pts]
    training_labels = data['Y'][:num_training_pts]
    test_pixels = data['X'][num_training_pts:]
    test_labels = data['Y'][num_training_pts:]
    correct_wrong_list = [0, 0]
    RIGHT = 0
    WRONG = 1
    for test_idx in range(len(test_pixels)):
        knn = []
        for i in range(num_training_pts):
            img = training_pixels[i]
            curr_dist = euclidean_dist(img, test_pixels[test_idx])
            if len(knn) < k:
                heapq.heappush(knn, (curr_dist, str(i)))
                heapq._heapify_max(knn)
            elif curr_dist < knn[0][0]:
                heapq.heappop(knn)
                heapq.heappush(knn, (curr_dist, str(i)))
                heapq._heapify_max(knn)
        counts = [0] * 10
        for pair in knn:
            idx = int(pair[1])
            label = training_labels[idx][0]
            counts[label] += 1
        label_guess = np.argmax(counts)
        actual_label = test_labels[test_idx][0]
        if actual_label == label_guess:
            correct_wrong_list[RIGHT] += 1
        else:
            correct_wrong_list[WRONG] += 1
        print(f"Test image {num_training_pts + test_idx} was identified as {label_guess}. Actual label was {actual_label}.")
    print(f"k: {k}")
    print(f"Number of training data points: {num_training_pts}")
    print("\nCorrect vs. wrong answers:")
    print(correct_wrong_list)
    print("\nPercentage correct:")
    accuracy = correct_wrong_list[RIGHT] / (correct_wrong_list[RIGHT] + correct_wrong_list[WRONG])
    print(f"{accuracy * 100:.2f}%")
if __name__ == '__main__':
    main()