import numpy as np
from participle import fenci
import matplotlib.pyplot as plt
from wordcloud import WordCloud
def fonk1(raw_path, b17):
    return fenci(raw_path, b17)
def fonk2(dataset, b1 = 50):
    b2 = {}
    for i, doc in enumerate(dataset):
        for word in doc:
            b2[word] = b2.get(word, 0) + 1
        print(f"Processing document {i+1}/{len(dataset)}")
    b3 = {word: freq for word, freq in b2.items() if freq > b1}
    b4 = sorted(b3.items(), key=lambda x: x[1], reverse=True)
    return [word for word, _ in b4]
def fonk3(unique_words, input_doc):
    b5 = [0] * len(unique_words)
    for word in input_doc:
        if word in unique_words:
            b5[unique_words.index(word)] += 1
    return b5
def fonk4(b22, train_classes):
    b6 = len(b22)
    b7 = len(b22[0])
    b8 = set(train_classes)
    b9 = []
    b10 = []
    for cls in b8:
        b11 = train_classes.count(cls)
        b12 = b11 / float(b6)
        b9.append(b12)
        b13 = np.ones(b7)
        a1 = 2.0
        for i in range(b6):
            if train_classes[i] == cls:
                b13 += b22[i]
                a1 += sum(b22[i])
        print(f"Training class {cls}")
        b10.append(np.log(b13 / a1))
    return b10, b9
def fonk5(unique_words, b9, b10, b14 = 'models'):
    np.save(f'{b14}/pos.npy', np.array(b9))
    with open(f'{b14}/b21.txt', 'w') as file:
        for word in unique_words:
            file.write(f"{word}\n")
    np.save(f'{b14}/p_vectors.npy', np.array(b10))
if b15 = = "__main__":
    b16 = ['Sport', 'Entertainment', 'Household', 'House Property', 'Education', 'Fashion', 'Current Politics', 'Game', 'Science and Technology', 'Finance']
    b17 = './cnews/cnews.vocab.txt'
    b18 = './cnews/cnews.train.txt'
    b19 = './cnews/cnews.test.txt'
    raw_features, b20 = fonk1(b18, b17)
    b21 = fonk2(raw_features)
    b22 = [fonk3(b21, doc) for doc in raw_features]
    for i, _ in enumerate(b22):
        print(f"Vectorizing document {i+1}/{len(b22)}")
    p_vectors, b23 = fonk4(np.array(b22), b20)
    fonk5(b21, b23, p_vectors)
    print("Model training completed and parameters saved.")