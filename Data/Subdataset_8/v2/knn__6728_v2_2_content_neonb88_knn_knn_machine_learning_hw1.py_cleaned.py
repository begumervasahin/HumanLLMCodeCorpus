import scipy.io as sio
import numpy as np
import heapq
def euclidean_dist(x, y):
    diff_vect = x - y
    return np.linalg.norm(diff_vect)
k = int(input("Please enter the number of nearest neighbors (k): "))
num_training_pts = int(input("Enter the number of pictures to use as training data (up to 10,000): "))
data = sio.loadmat('ML_hw1data.mat')
training_pixels = data['X'][:num_training_pts]
training_labels = data['Y'][:num_training_pts]
test_pixels = data['X'][num_training_pts:]
test_labels = data['Y'][num_training_pts:]
correct_count = 0
wrong_count = 0
for test_idx, test_img in enumerate(test_pixels):
    knn = []
    for i in range(100):
        img = training_pixels[i]
        curr_dist = euclidean_dist(img, test_img)
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
    label_guess = counts.index(max(counts))
    actual_label = test_labels[test_idx][0]
    if actual_label == label_guess:
        correct_count += 1
    else:
        wrong_count += 1
    print(f"Test image {num_training_pts + test_idx} was identified as {label_guess}")
    print(f"Actual label was {actual_label}")
total_count = correct_count + wrong_count
percentage_correct = (correct_count / total_count) * 100
print(f"K was {k} and we used {num_training_pts} training data points")
print("\nCorrect vs. wrong answers:")
print(f"Correct: {correct_count}, Wrong: {wrong_count}")
print("\nPercentage correct:")
print(percentage_correct)