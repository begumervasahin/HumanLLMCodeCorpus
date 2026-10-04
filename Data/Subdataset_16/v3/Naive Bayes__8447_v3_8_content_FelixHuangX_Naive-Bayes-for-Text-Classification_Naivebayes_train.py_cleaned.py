import numpy as np
from participle import fenci
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
def fonk1(raw_path, b16):
    result, b1 = fenci(raw_path, b16)
    return result, b1
def fonk2(dataset, b2 = 50):
    b3 = {}
    for i, doc in enumerate(dataset):
        for word in doc:
            b3[word] = b3.get(word, 0) + 1
        print(f"Processing document {i}")
    b4 = {word: count for word, count in b3.items() if count > b2}
    b5 = sorted(b4.items(), key=lambda x: x[1], reverse=True)
    return [word for word, _ in b5]
def fonk3(b19, input_doc):
    b6 = [0] * len(b19)
    for word in input_doc:
        if word in b19:
            b6[b19.index(word)] += 1
    return b6
def fonk4(b20, train_class):
    b7 = len(b20)
    b8 = len(b20[0])
    b9 = set(train_class)
    b10 = []
    b11 = []
    for class_label in b9:
        b12 = train_class.count(class_label) / float(b7)
        b10.append(b12)
        b3 = np.ones(b8)
        a1 = 2.0
        for i in range(b7):
            if train_class[i] == class_label:
                b3 += b20[i]
                a1 += sum(b20[i])
        print(f"Training class {class_label}")
        b13 = np.log(b3 / a1)
        b11.append(b13)
    return b11, b10
def fonk5(b21, b19, b11, b14 = 'models'):
    if not os.path.exists(b14):
        os.makedirs(b14)
    np.save(os.path.join(b14, 'pos.npy'), np.array(b21))
    with open(os.path.join(b14, 'b19.txt'), 'w') as file:
        for word in b19:
            file.write(f"{word}\n")
    np.save(os.path.join(b14, 'b11.npy'), np.array(b11))
def fonk6():
    b15 = ['Sport', 'Entertainment', 'Household', 'House Property', 'Education', 'Fashion', 'Current Politics', 'Game', 'Science and Technology', 'Finance']
    b16 = './cnews/cnews.vocab.txt'
    b17 = './cnews/cnews.train.txt'
    raw_features, b18 = fonk1(b17, b16)
    b19 = fonk2(raw_features)
    b20 = [fonk3(b19, doc) for doc in raw_features]
    for i, single_features in enumerate(raw_features):
        print(f"Processed document {i}")
    b11, b21 = fonk4(np.array(b20), b18)
    fonk5(b21, b19, b11)
if b22 = = "__main__":
    fonk6()