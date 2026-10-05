import numpy as np
from sklearn.model_selection import train_test_split
data = np.loadtxt(open('D:\\diabetes.csv'), delimiter=',', skiprows=1, encoding='utf8', dtype=float)
def calculate_mean_std(data):
    means = np.mean(data, axis=0)
    stds = np.std(data, axis=0)
    return means[:-1], stds[:-1]
def gaussian_probability(x, mean, stdev):
    exponent = np.exp(-(np.power(x - mean, 2)) / (2 * np.power(stdev, 2)))
    return (1 / (np.sqrt(2 * np.pi) * stdev)) * exponent
def class_probability(test_data, means, stds):
    prob = 1
    for i in range(len(test_data) - 1):
        prob *= gaussian_probability(test_data[i], means[i], stds[i])
    return prob
def predict(train_data, test_data):
    train_means, train_stds = calculate_mean_std(train_data)
    prob1 = class_probability(test_data, train_means, train_stds)
    prob2 = class_probability(test_data, train_means, train_stds)
    return 1 if prob1 > prob2 else 0
train_data, test_data = train_test_split(data, test_size=0.10)
correct_count = sum(1 for test_instance in test_data if predict(train_data, test_instance) == int(test_instance[-1]))
accuracy = (correct_count / len(test_data)) * 100.0
print("Accuracy:", accuracy)