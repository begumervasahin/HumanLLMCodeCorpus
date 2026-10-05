import numpy as np
from sklearn.model_selection import train_test_split
data = np.loadtxt(open('D:\\diabetes.csv'), delimiter=',', skiprows=1, encoding='utf8', dtype=float)
def calculate_mean_std(data):
    means = np.mean(data, axis=0)
    stds = np.std(data, axis=0)
    return means[:-1], stds[:-1]
def gaussian_pdf(x, mean, std):
    exponent = np.exp(-(np.power(x - mean, 2)) / (2 * np.power(std, 2)))
    return (1 / (np.sqrt(2 * np.pi) * std)) * exponent
def class_probability(test_data_point, means, stds):
    probabilities = [gaussian_pdf(test_data_point[i], means[i], stds[i]) for i in range(len(means))]
    return np.prod(probabilities)
def predict(train_data, test_data_point):
    means, stds = calculate_mean_std(train_data)
    probability = class_probability(test_data_point[:-1], means, stds)
    return probability
train_data, test_data = train_test_split(data, test_size=0.10)
kind1 = train_data[train_data[:, -1] == 1]
kind2 = train_data[train_data[:, -1] == 0]
correct_count = 0
for test_point in test_data:
    probability1 = predict(kind1, test_point)
    probability2 = predict(kind2, test_point)
    predicted_label = 1 if probability1 > probability2 else 0
    if predicted_label == test_point[-1]:
        correct_count += 1
accuracy = (correct_count / len(test_data)) * 100.0
print("Accuracy:", accuracy)