import numpy as np
from sklearn.model_selection import train_test_split
data = np.loadtxt(open('D:\\diabetes.csv'), delimiter=',', skiprows=1, encoding='utf8', dtype=float)
def calculate_mean_std(data):
    feature_num = len(data[0]) - 1
    means = []
    stds = []
    for i in range(feature_num):
        column_values = [row[i] for row in data]
        means.append(np.mean(column_values))
        stds.append(np.std(column_values))
    return means, stds, feature_num
def gaussian_probability(x, mean, stdev):
    exponent = np.exp(-(np.power(x - mean, 2)) / (2 * np.power(stdev, 2)))
    gauss_prob = (1 / (np.sqrt(2 * np.pi) * stdev)) * exponent
    return gauss_prob
def class_probability(test_data, mean, std):
    prob = 1
    for i in range(0, 8):
        prob *= gaussian_probability(test_data[i], mean[i], std[i])
    return prob
def predict(train_data, test_data):
    train_mean, train_std, train_feature_num = calculate_mean_std(train_data)
    test_prob = class_probability(test_data, train_mean, train_std)
    return test_prob
train_data, test_data = train_test_split(data, test_size=0.10)
class1 = [tip for tip in train_data if tip[-1] == 1.0]
class2 = [tip for tip in train_data if tip[-1] != 1.0]
correct_count = 0
for test_instance in test_data:
    prob1 = predict(class1, test_instance)
    prob2 = predict(class2, test_instance)
    if prob1 > prob2:
        best_label = 1
        if best_label == test_instance[-1]:
            correct_count += 1
    else:
        best_label = 0
        if best_label == test_instance[-1]:
            correct_count += 1
accuracy = (correct_count / float(len(test_data))) * 100.0
print("Accuracy:", accuracy)