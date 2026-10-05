import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
import warnings
def euclidean_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))
def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn("k is too small")
    distances = [(group, euclidean_distance(features, predict))
                 for group, features_list in data.items()
                 for features in features_list]
    sorted_distances = sorted(distances, key=lambda x: x[1])
    top_nearest = [group for group, _ in sorted_distances[:k]]
    group_res = Counter(top_nearest).most_common(1)[0][0]
    confidence = Counter(top_nearest).most_common(1)[0][1] * 1.0 / k
    return group_res, confidence
if __name__ == '__main__':
    dataset = {'black': [[1, 2], [2, 3], [3, 1]], 'red': [[6, 5], [7, 7], [8, 6]]}
    new_features = [3.5, 5.2]
    for group, features_list in dataset.items():
        for features in features_list:
            plt.scatter(features[0], features[1], s=50, color=group)
    which_group, confidence = k_nearest_neighbors(dataset, new_features, k=3)
    print(f"Predicted group: {which_group}, Confidence: {confidence}")
    plt.scatter(new_features[0], new_features[1], s=300, color=which_group)
    plt.show()