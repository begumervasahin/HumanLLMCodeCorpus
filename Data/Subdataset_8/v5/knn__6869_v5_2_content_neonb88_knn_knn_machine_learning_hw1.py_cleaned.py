import scipy.io as sio
import numpy as np
import heapq
def load_data(file_path):
    data = sio.loadmat(file_path)
    return data['X'], data['Y']
def euclidean_dist(x, y):
    return np.linalg.norm(x - y)
def knn_classify(test_pixels, training_pixels, training_labels, k):
    correct = 0
    for test_idx, test_pixel in enumerate(test_pixels):
        knn = []
        for i, train_pixel in enumerate(training_pixels):
            dist = euclidean_dist(train_pixel, test_pixel)
            if len(knn) < k:
                heapq.heappush(knn, (dist, i))
            elif dist < knn[0][0]:
                heapq.heappop(knn)
                heapq.heappush(knn, (dist, i))
        counts = [0] * 10
        for _, idx in knn:
            label = training_labels[idx][0]
            counts[label] += 1
        predicted_label = max(range(10), key=lambda x: counts[x])
        actual_label = test_labels[test_idx][0]
        if actual_label == predicted_label:
            correct += 1
        print(f"Test image {len(training_pixels) + test_idx} was identified as {predicted_label}")
        print(f"Actual label was {actual_label}")
    return correct
def main():
    file_path = 'ML_hw1data.mat'
    k = int(input("Please enter the value of k for k-nearest neighbors: "))
    num_training_pts = int(input("How many images would you like to use as training data? (There are 10,000 images in total): "))
    training_pixels, training_labels = load_data(file_path)
    test_pixels, test_labels = training_pixels[num_training_pts:], training_labels[num_training_pts:]
    correct = knn_classify(test_pixels, training_pixels[:num_training_pts], training_labels[:num_training_pts], k)
    print(f"k was {k} and we used {num_training_pts} training data points")
    print("\nCorrect vs. wrong answers:")
    print([correct, len(test_pixels) - correct])
    print("\nPercentage correct:")
    print(correct / len(test_pixels))
if __name__ == "__main__":
    main()