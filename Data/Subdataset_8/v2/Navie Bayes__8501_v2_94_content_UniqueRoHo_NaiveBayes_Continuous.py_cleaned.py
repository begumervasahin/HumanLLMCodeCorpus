import numpy as np
from sklearn.model_selection import train_test_split
data = np.loadtxt(open('D:\\diabetes.csv'), delimiter=',', skiprows=1, encoding='utf8', dtype=float)
def get_mean_std(data):
    feature_num = len(data[0]) - 1
    means = []
    stds = []
    for i in range(feature_num):
        feature_values = [row[i] for row in data]
        means.append(np.mean(feature_values))
        stds.append(np.std(feature_values))
    return means, stds, feature_num
def gauss(x, mean, stdev):
    exponent = np.exp(-(np.power(x - mean, 2)) / (2 * np.power(stdev, 2)))
    return (1 / (np.sqrt(2 * np.pi) * stdev)) * exponent
def kind_prob(test_data_point, mean, std):
    probability = 1
    for i in range(0, 8):
        probability *= gauss(test_data_point[i], mean[i], std[i])
    return probability
def predict(train_data, test_data_point):
    train_mean, train_std, train_feature_num = get_mean_std(train_data)
    probability = kind_prob(test_data_point, train_mean, train_std)
    return probability
train_data, test_data = train_test_split(data, test_size=0.10)
kind1 = [row for row in train_data if row[-1] == 1.0]
kind2 = [row for row in train_data if row[-1] == 0.0]
correct_count = 0
for test_point in test_data:
    probability1 = predict(kind1, test_point)
    probability2 = predict(kind2, test_point)
    predicted_label = 1 if probability1 > probability2 else 0
    if predicted_label == test_point[-1]:
        correct_count += 1
accuracy = (correct_count / float(len(test_data))) * 100.0
print("Accuracy:", accuracy)