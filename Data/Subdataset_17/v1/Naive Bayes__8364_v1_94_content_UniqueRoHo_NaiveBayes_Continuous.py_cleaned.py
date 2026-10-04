
import numpy as np
from sklearn.model_selection import train_test_split
def load_data(filepath):
    return np.loadtxt(open(filepath), delimiter=',', skiprows=1, dtype=float)
def get_mean_std(data):
    feature_num = data.shape[1] - 1
    means = []
    stds = []
    for i in range(feature_num):
        feature_values = data[:, i]
        means.append(np.mean(feature_values))
        stds.append(np.std(feature_values))
    return means, stds, feature_num
def gauss_prob(x, mean, std):
    exponent = np.exp(-(np.power(x - mean, 2)) / (2 * np.power(std, 2)))
    return (1 / (np.sqrt(2 * np.pi) * std)) * exponent
def class_prob(test_data, means, stds):
    prob = 1
    for i in range(len(means)):
        prob *= gauss_prob(test_data[i], means[i], stds[i])
    return prob
def predict(train_data, test_data):
    means, stds, _ = get_mean_std(train_data)
    return class_prob(test_data, means, stds)
def main():
    data_filepath = 'D:\\diabetes.csv'
    data = load_data(data_filepath)
    train_data, test_data = train_test_split(data, test_size=0.10)
    kind1 = train_data[train_data[:, -1] == 1.0]
    kind2 = train_data[train_data[:, -1] == 0.0]
    correct_count = 0
    for test_instance in test_data:
        prob1 = predict(kind1, test_instance)
        prob2 = predict(kind2, test_instance)
        best_label = 1 if prob1 > prob2 else 0
        if best_label == test_instance[-1]:
            correct_count += 1
    accuracy = (correct_count / len(test_data)) * 100.0
    print(f'Accuracy: {accuracy:.2f}%')
if __name__ == "__main__":
    main()