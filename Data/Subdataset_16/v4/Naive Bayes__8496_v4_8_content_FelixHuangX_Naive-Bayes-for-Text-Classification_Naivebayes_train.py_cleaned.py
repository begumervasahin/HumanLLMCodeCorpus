import numpy as np
from participle import fenci
import matplotlib.pyplot as plt
from wordcloud import WordCloud
def fonk1(raw_path, b16):
    result, b1 = fenci(raw_path, b16)
    return result, b1
def fonk2(dataset):
    b2 = {}
    for i, doc in enumerate(dataset):
        for word in doc:
            if word in b2:
                b2[word] += 1
            else:
                b2[word] = 1
        print(f"Processing document {i+1}/{len(dataset)}")
    b2 = {k: v for k, v in b2.items() if v > 50}
    b3 = sorted(b2.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in b3]
def fonk3(b20, input_doc):
    b4 = [0] * len(b20)
    for word in input_doc:
        if word in b20:
            b4[b20.index(word)] += 1
    return b4
def fonk4(b21, train_classes):
    b5 = len(b21)
    b6 = len(b21[0])
    b7 = set(train_classes)
    b8 = []
    b9 = []
    for cls in b7:
        b10 = train_classes.count(cls)
        b11 = b10 / float(b5)
        b8.append(b11)
        b12 = np.ones(b6)
        a1 = 2.0
        for i in range(b5):
            if train_classes[i] == cls:
                b12 += b21[i]
                a1 += sum(b21[i])
        print(f"Training class {cls}")
        b13 = np.log(b12 / a1)
        b9.append(b13)
    return b9, b8
if b14 = = "__main__":
    b15 = ['Sport', 'Entertainment', 'Household', 'House Property', 'Education', 'Fashion', 'Current Politics', 'Game', 'Science and Technology', 'Finance']
    b16 = './cnews/cnews.vocab.txt'
    b17 = './cnews/cnews.train.txt'
    b18 = './cnews/cnews.test.txt'
    raw_features, b19 = fonk1(b17, b16)
    b20 = fonk2(raw_features)
    b21 = []
    for i, single_features in enumerate(raw_features):
        b21.append(fonk3(b20, single_features))
        print(f"Vectorizing document {i+1}/{len(raw_features)}")
    p_vectors, b22 = fonk4(np.array(b21), b19)
    np.save('models/pos.npy', np.array(b22))
    with open('models/b20.txt', 'w') as file:
        for word in b20:
            file.write(f"{word}\n")
    np.save('models/p_vectors.npy', np.array(p_vectors))
    print("Model training completed and parameters saved.")