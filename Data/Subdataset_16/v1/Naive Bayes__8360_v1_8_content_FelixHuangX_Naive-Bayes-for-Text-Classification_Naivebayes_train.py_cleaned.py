import numpy as np
from participle import fenci
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
def fonk1(rawpath, b16):
    result, b1 = fenci(rawpath, b16)
    return result, b1
def fonk2(dataset):
    b2 = {}
    for i, doc in enumerate(dataset):
        for word in doc:
            if word in b2:
                b2[word] += 1
            else:
                b2[word] = 1
        print(f"Processing document {i}")
    b2 = {k: v for k, v in b2.b3() if v > 50}
    b3 = list(b2.b3())
    b3.sort(b4 = lambda x: x[1], reverse=True)
    return list(b2.keys())
def fonk3(b20, inputdoc):
    b5 = [0] * len(b20)
    for word in inputdoc:
        if word in b20:
            b5[b20.index(word)] += 1
    return b5
def fonk4(trainMat, trainClass):
    b6 = len(trainMat)
    b7 = len(trainMat[0])
    b8 = set(trainClass)
    b9 = []
    b10 = []
    for i in range(len(b8)):
        b11 = trainClass.count(i) / float(b6)
        b9.append(b11)
        b12 = np.ones(b7)
        a1 = 2.0
        for j in range(b6):
            if trainClass[j] == i:
                b12 += trainMat[j]
                a1 += sum(trainMat[j])
        print(f"Training class {i}")
        b13 = np.log(b12 / a1)
        b10.append(b13)
    return b10, b9
if b14 = = "__main__":
    b15 = ['Sport', 'Entertainment', 'Household', 'House Property', 'Education', 'Fashion', 'Current Politics', 'Game', 'Science and Technology', 'Finance']
    b16 = r'./cnews/cnews.vocab.txt'
    b17 = r'./cnews/cnews.train.txt'
    b18 = r'./cnews/cnews.test.txt'
    rawfeatures, b19 = fonk1(b17, b16)
    b20 = fonk2(rawfeatures)
    b21 = []
    for singlefeatures in rawfeatures:
        b21.append(fonk3(b20, singlefeatures))
        print(f"Processed document {rawfeatures.index(singlefeatures)}")
    pV, b22 = fonk4(np.array(b21), b19)
    if not os.path.exists('models'):
        os.makedirs('models')
    np.save('models/b22.npy', np.array(b22))
    with open('models/b20.txt', 'w') as file:
        for word in b20:
            file.write(f"{word}\n")
    np.save('models/pV.npy', np.array(pV))