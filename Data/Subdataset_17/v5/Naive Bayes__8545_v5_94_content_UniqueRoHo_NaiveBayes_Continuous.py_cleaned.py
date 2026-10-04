
import numpy as np
from sklearn.model_selection import train_test_split
DATA_FILE = 'D:\\diabetes.csv'
data = np.loadtxt(open(DATA_FILE), delimiter=',', skiprows=1, encoding='utf8', dtype=float)
def calculate_mean_std(data):
    num_features = data.shape[1] - 1
    means = [np.mean(data[:, i]) for i in range(num_features)]
    stds = [np.std(data[:, i]) for i in range(num_features)]
    return means, stds, num_features
def gauss_probability(x, mean, std):
    exponent = np.exp(-((x - mean) ** 2) / (2 * (std ** 2)))
    return (1 / (np.sqrt(2 * np.pi) * std)) * exponent
def class_probability(test_data, means, stds):
    probability = 1.0
    for i in range(len(means)):
        probability *= gauss_probability(test_data[i], means[i], stds[i])
    return probability
def predict(train_data, test_data):
    means, stds, _ = calculate_mean_std(train_data)
    return class_probability(test_data, means, stds)
def main():
    train_data, test_data = train_test_split(data, test_size=0.10, random_state=42)
    class1 = np.array([row for row in train_data if row[-1] == 1.0])
    class2 = np.array([row for row in train_data if row[-1] == 0.0])
    correct_count = 0
    for test_instance in test_data:
        prob_class1 = predict(class1, test_instance)
        prob_class2 = predict(class2, test_instance)
        predicted_label = 1.0 if prob_class1 > prob_class2 else 0.0
        if predicted_label == test_instance[-1]:
            correct_count += 1
    accuracy = (correct_count / float(len(test_data))) * 100.0
    print(f"Accuracy: {accuracy:.2f}%")
if __name__ == "__main__":
    main()