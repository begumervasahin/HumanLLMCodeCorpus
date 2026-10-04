import scipy.io as sio
import numpy as np
import heapq
def euclidean_dist(x, y):
    return np.linalg.norm(x - y)
def main():
    k = int(input("Please type a k for how many nearest neighbors you want to compute: "))
    num_training_pts = int(input("There are 10,000 pictures of numbers.\nHow many would you like to use as training data? "))
    data = sio.loadmat('ML_hw1data.mat')
    training_pixels = data['X'][:num_training_pts]
    training_labels = data['Y'][:num_training_pts]
    test_pixels = data['X'][num_training_pts:]
    test_labels = data['Y'][num_training_pts:]
    correct_wrong_list = [0, 0]
    RIGHT, WRONG = 0, 1
    for test_idx in range(len(test_pixels)):
        knn = []
        for i in range(len(training_pixels)):
            curr_dist = euclidean_dist(training_pixels[i], test_pixels[test_idx])
            if len(knn) < k:
                heapq.heappush(knn, (curr_dist, i))
                heapq._heapify_max(knn)
            elif curr_dist < knn[0][0]:
                heapq.heappop(knn)
                heapq.heappush(knn, (curr_dist, i))
                heapq._heapify_max(knn)
        counts = [0] * 10
        for _, idx in knn:
            label = training_labels[idx][0]
            counts[label] += 1
        label_guess = np.argmax(counts)
        actual_label = test_labels[test_idx][0]
        if actual_label == label_guess:
            correct_wrong_list[RIGHT] += 1
        else:
            correct_wrong_list[WRONG] += 1
        print(f"Test image {num_training_pts + test_idx} was identified as {label_guess}")
        print(f"Actual label was {actual_label}")
    print(f"\nk was {k}")
    print(f"We used {num_training_pts} training data points")
    print("\nCorrect vs. wrong answers:")
    print(correct_wrong_list)
    print("\nPercentage correct:")
    accuracy = (correct_wrong_list[RIGHT] / sum(correct_wrong_list)) * 100
    print(f"{accuracy:.2f}%")
if __name__ == '__main__':
    main()