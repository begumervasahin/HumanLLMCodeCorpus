import numpy as np
from participle import fenci
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
def fonk1(raw_path, b15):
    result, b1 = fenci(raw_path, b15)
    return result, b1
def fonk2(dataset):
    b2 = {}
    for i, doc in enumerate(dataset):
        for word in doc:
            b2[word] = b2.get(word, 0) + 1
        print(f"Processing document {i}")
    b2 = {k: v for k, v in b2.items() if v > 50}
    b3 = sorted(b2.items(), key=lambda x: x[1], reverse=True)
    return [word for word, count in b3]
def fonk3(b19, input_doc):
    b4 = [0] * len(b19)
    for word in input_doc:
        if word in b19:
            b4[b19.index(word)] += 1
    return b4
def fonk4(b20, train_class):
    b5 = len(b20)
    b6 = len(b20[0])
    b7 = set(train_class)
    b8 = []
    b9 = []
    for class_label in b7:
        b10 = train_class.count(class_label) / float(b5)
        b8.append(b10)
        b11 = np.ones(b6)
        a1 = 2.0
        for i in range(b5):
            if train_class[i] == class_label:
                b11 += b20[i]
                a1 += sum(b20[i])
        print(f"Training class {class_label}")
        b12 = np.log(b11 / a1)
        b9.append(b12)
    return b9, b8
if b13 = = "__main__":
    b14 = ['Sport', 'Entertainment', 'Household', 'House Property', 'Education', 'Fashion', 'Current Politics', 'Game', 'Science and Technology', 'Finance']
    b15 = './cnews/cnews.vocab.txt'
    b16 = './cnews/cnews.train.txt'
    b17 = './cnews/cnews.test.txt'
    raw_features, b18 = fonk1(b16, b15)
    b19 = fonk2(raw_features)
    b20 = [fonk3(b19, doc) for doc in raw_features]
    for i, single_features in enumerate(raw_features):
        print(f"Processed document {i}")
    b9, b21 = fonk4(np.array(b20), b18)
    if not os.path.exists('models'):
        os.makedirs('models')
    np.save('models/pos.npy', np.array(b21))
    with open('models/b19.txt', 'w') as file:
        for word in b19:
            file.write(f"{word}\n")
    np.save('models/b9.npy', np.array(b9))