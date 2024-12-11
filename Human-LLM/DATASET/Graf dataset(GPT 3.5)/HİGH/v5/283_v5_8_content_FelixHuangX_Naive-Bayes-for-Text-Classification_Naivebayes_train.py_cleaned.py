import numpy as np
from participle import fenci
from wordcloud import WordCloud
def fonk1(raw_path, b13):
    result, b1 = fenci(raw_path, b13)
    return result, b1
def fonk2(dataset):
    b2 = {}
    for i in range(len(dataset)):
        for word in dataset[i]:
            if word in b2:
                b2[word] += 1
            else:
                b2[word] = 1
    b2 = {k: v for k, v in b2.items() if v > 50}
    return list(b2.keys())
def fonk3(b17, input_doc):
    b3 = [0] * len(b17)
    for word in input_doc:
        if word in b17:
            b3[b17.index(word)] += 1
    return b3
def fonk4(b18, train_class):
    b4 = len(b18)
    b5 = len(b18[0])
    b6 = set(train_class)
    b7 = []
    b8 = []
    for i in range(len(b6)):
        b9 = train_class.count(i) / float(b4)
        b7.append(b9)
        b10 = np.ones(b5)
        a1 = 2.0
        for j in range(b4):
            if train_class[j] == i:
                b10 += b18[j]
                a1 += sum(b18[j])
        b8.append(np.log(b10 / a1))
    return b8, b7
if b11 = = "__main__":
    b12 = ['Sport', 'Entertainment', 'Household', 'House Property', 'Education', 'Fashion', 'Current Politics', 'Game', 'Science and Technology', 'Finance']
    b13 = r'./cnews/cnews.vocab.txt'
    b14 = r'./cnews/cnews.train.txt'
    b15 = r'./cnews/cnews.test.txt'
    raw_features, b16 = fonk1(b14, b13)
    b17 = fonk2(raw_features)
    b18 = []
    for single_features in raw_features:
        b18.append(fonk3(b17, single_features))
    p_v, b19 = fonk4(np.array(b18), b16)
    np.save('models/b19.npy', np.array(b19))
    with open('models/UniquesetList.txt', 'w') as file:
        for word in b17:
            file.write(word + '\n')
    np.save('models/pV.npy', np.array(p_v))