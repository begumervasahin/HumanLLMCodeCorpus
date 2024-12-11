import numpy as np
from participle import fenci
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def fonk1(raw_path, b15):
    result, b1 = fenci(raw_path, b15)
    return result, b1
def fonk2(dataset):
    b2 = {}
    for data in dataset:
        for word in data:
            if word in b2:
                b2[word] += 1
            else:
                b2[word] = 1
    b2 = {k: v for k, v in b2.items() if v > 50}
    b3 = list(b2.keys())
    b3.sort(b4 = lambda x: b2[x], reverse=True)
    return b3
def fonk3(b19, input_doc):
    b5 = [0] * len(b19)
    for word in input_doc:
        if word in b19:
            b5[b19.index(word)] += 1
    return b5
def fonk4(b20, train_class):
    b6 = len(b20)
    b7 = len(b20[0])
    b8 = set(train_class)
    b9 = []
    b10 = []
    for cls in b8:
        b11 = train_class.count(cls) / float(b6)
        b9.append(b11)
        b12 = np.ones(b7)
        a1 = 2.0
        for j in range(b6):
            if train_class[j] == cls:
                b12 += b20[j]
                a1 += sum(b20[j])
        b10.append(np.log(b12 / a1))
    return b10, b9
if b13 = = "__main__":
    b14 = ['Sport', 'Entertainment', 'Household', 'House Property', 'Education', 'Fashion', 'Current Politics', 'Game', 'Science and Technology', 'Finance']
    b15 = r'./cnews/cnews.vocab.txt'
    b16 = r'./cnews/cnews.train.txt'
    b17 = r'./cnews/cnews.test.txt'
    raw_features, b18 = fonk1(b16, b15)
    b19 = fonk2(raw_features)
    b20 = [fonk3(b19, single_features) for single_features in raw_features]
    b10, b21 = fonk4(np.array(b20), b18)
    np.save('models/b21.npy', np.array(b21))
    with open('models/b19.txt', 'w') as file:
        for word in b19:
            file.write(word + '\n')
    np.save('models/pV.npy', np.array(b10))