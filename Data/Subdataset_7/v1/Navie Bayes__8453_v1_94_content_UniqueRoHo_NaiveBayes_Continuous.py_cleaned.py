import numpy as np
from sklearn.model_selection import train_test_split
b1 = np.loadtxt(open('D:\\diabetes.csv'), delimiter=',', skiprows=1, encoding='utf8', dtype=float)
def fonk1(data1):
    b2 = len(data1[0]) - 1
    b3 = locals()
    b4 = []
    b5 = []
    for i in range(b2):
        b3['mean%s' % i] = []
        for j in data1:
            b3['mean%s' % i].append(j[i])
    for i in range(b2):
        b4.append(np.mean(b3['mean%s' % i]))
        b5.append(np.std(b3['mean%s' % i]))
    return b4, b5, b2
def fonk2(x, mean, stdev):
    b6 = np.exp(-(np.power(x-mean, 2))/(2*np.power(stdev, 2)))
    b7 = (1/(np.sqrt(2*np.pi)*stdev)) * b6
    return b7
def fonk3(test_data_tip, mean, std):
    a1 = 1
    for i in range(0, 8):
        a1 *= fonk2(test_data_tip[i], mean[i], std[i])
    return a1
def fonk4(train_data, b12):
    train_mean, train_std, b8 = fonk1(train_data)
    b9 = fonk3(b12, train_mean, train_std)
    return b9
b10 = []
b11 = []
train_data, b12 = train_test_split(b1, test_size=0.10)
for i in range(len(train_data)):
    b13 = train_data[i]
    if b13[-1] == 1.0:
        b10.append(train_data[i])
    else:
        b11.append(train_data[i])
a2 = 0
for i in b12:
    b14 = fonk4(b10, i)
    b15 = fonk4(b11, i)
    if b14 > b15:
        a3 = 1
        if a3 = = i[-1]:
            a2 += 1
    else:
        a3 = 0
        if a3 = = i[-1]:
            a2 += 1
b16 = (a2 / float(len(b12))) * 100.0
print(b16)