import numpy as np
from sklearn.cluster import KMeans
def find_bounding_box(points):
    min_x = min(points, key=lambda a: a[0])[0]
    max_x = max(points, key=lambda a: a[0])[0]
    min_y = min(points, key=lambda a: a[1])[1]
    max_y = max(points, key=lambda a: a[1])[1]
    return (min_x, max_x), (min_y, max_y)
def calculate_compactness(data, centers, labels):
    sum_squared_distances = 0.0
    for i in range(len(data)):
        cluster_num = labels.item(i)
        sum_squared_distances += np.linalg.norm(centers[cluster_num] - data[i])**2
    return sum_squared_distances
def gap_kmeans(data, k_range=30, sample_trials=10, print_results=True):
    num_data, num_features = data.shape
    extrema = [[min(data[:, dim]), max(data[:, dim])] for dim in range(num_features)]
    gap_values = np.zeros(k_range)
    s_values = np.zeros(k_range)
    for k in range(k_range):
        kmeans = KMeans(n_clusters=(k + 1))
        labels = kmeans.fit_predict(data)
        k_compactness = np.log(calculate_compactness(data, kmeans.cluster_centers_, labels))
        trial_compactness = np.zeros(sample_trials)
        for trial in range(sample_trials):
            samples = np.zeros((num_data, num_features))
            for sample in range(num_data):
                samples[sample] = [np.random.uniform(extrema[dim][0], extrema[dim][1]) for dim in range(num_features)]
            sample_labels = kmeans.fit_predict(samples)
            trial_compactness[trial] = np.log(calculate_compactness(samples, kmeans.cluster_centers_, sample_labels))
        gap_values[k] = sum(trial_compactness - k_compactness)**2 / sample_trials
        w_bar = sum(trial_compactness) / sample_trials
        sd = np.sqrt(sum((trial_compactness - w_bar)**2) / sample_trials)
        s_values[k] = np.sqrt(1 + 1/sample_trials) * sd
        if print_results and k > 0:
            print("Gap value at", k, "clusters:", gap_values[k - 1])
            print("Need to beat", gap_values[k] - s_values[k - 1])
        if k > 0 and gap_values[k - 1] > gap_values[k] - s_values[k - 1]:
            return labels
    return labels
if __name__ == "__main__":
    np.random.seed(0)
    data = np.random.rand(100, 2)
    labels = gap_kmeans(data)
    print("Final labels:", labels)