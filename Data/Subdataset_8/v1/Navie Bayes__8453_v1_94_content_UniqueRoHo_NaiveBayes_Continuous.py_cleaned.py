import numpy as np
from sklearn.model_selection import train_test_split
data = np.loadtxt(open('D:\\diabetes.csv'), delimiter=',', skiprows=1, encoding='utf8', dtype=float)
def get_mean_std(data1):
    feature_num = len(data1[0]) - 1
    names = locals()
    c_mean = []
    c_std = []
    for i in range(feature_num):
        names['mean%s' % i] = []
        for j in data1:
            names['mean%s' % i].append(j[i])
    for i in range(feature_num):
        c_mean.append(np.mean(names['mean%s' % i]))
        c_std.append(np.std(names['mean%s' % i]))
    return c_mean, c_std, feature_num
def gauss(x, mean, stdev):
    exponent = np.exp(-(np.power(x-mean, 2))/(2*np.power(stdev, 2)))
    gauss_prob = (1/(np.sqrt(2*np.pi)*stdev)) * exponent
    return gauss_prob
def kind_prob(test_data_tip, mean, std):
    kinds_prob = 1
    for i in range(0, 8):
        kinds_prob *= gauss(test_data_tip[i], mean[i], std[i])
    return kinds_prob
def predict(train_data, test_data):
    train_mean, train_std, train_feature_num = get_mean_std(train_data)
    test_probility = kind_prob(test_data, train_mean, train_std)
    return test_probility
kind1 = []
kind2 = []
train_data, test_data = train_test_split(data, test_size=0.10)
for i in range(len(train_data)):
    tip = train_data[i]
    if tip[-1] == 1.0:
        kind1.append(train_data[i])
    else:
        kind2.append(train_data[i])
correct_count = 0
for i in test_data:
    probility1 = predict(kind1, i)
    probility2 = predict(kind2, i)
    if probility1 > probility2:
        best_label = 1
        if best_label == i[-1]:
            correct_count += 1
    else:
        best_label = 0
        if best_label == i[-1]:
            correct_count += 1
acc = (correct_count / float(len(test_data))) * 100.0
print(acc)