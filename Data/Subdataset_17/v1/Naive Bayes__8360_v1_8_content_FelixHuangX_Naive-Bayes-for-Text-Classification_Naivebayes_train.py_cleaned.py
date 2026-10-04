import numpy as np
from participle import fenci
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
def loadDataSet(rawpath, stoppath):
    result, data_target = fenci(rawpath, stoppath)
    return result, data_target
def createUniqueSet(dataset):
    UniqueSet = {}
    for i, doc in enumerate(dataset):
        for word in doc:
            if word in UniqueSet:
                UniqueSet[word] += 1
            else:
                UniqueSet[word] = 1
        print(f"Processing document {i}")
    UniqueSet = {k: v for k, v in UniqueSet.items() if v > 50}
    items = list(UniqueSet.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return list(UniqueSet.keys())
def words2vec(UniquesetList, inputdoc):
    returnVec = [0] * len(UniquesetList)
    for word in inputdoc:
        if word in UniquesetList:
            returnVec[UniquesetList.index(word)] += 1
    return returnVec
def trainNaiveB(trainMat, trainClass):
    numTraindocs = len(trainMat)
    numWords = len(trainMat[0])
    dataclass = set(trainClass)
    ptarget = []
    PVec = []
    for i in range(len(dataclass)):
        posSampleRate = trainClass.count(i) / float(numTraindocs)
        ptarget.append(posSampleRate)
        pNum = np.ones(numWords)
        pSum = 2.0
        for j in range(numTraindocs):
            if trainClass[j] == i:
                pNum += trainMat[j]
                pSum += sum(trainMat[j])
        print(f"Training class {i}")
        pVec = np.log(pNum / pSum)
        PVec.append(pVec)
    return PVec, ptarget
if __name__ == "__main__":
    label = ['Sport', 'Entertainment', 'Household', 'House Property', 'Education', 'Fashion', 'Current Politics', 'Game', 'Science and Technology', 'Finance']
    stoppath = r'./cnews/cnews.vocab.txt'
    trainpath = r'./cnews/cnews.train.txt'
    testpath = r'./cnews/cnews.test.txt'
    rawfeatures, rawclasses = loadDataSet(trainpath, stoppath)
    UniquesetList = createUniqueSet(rawfeatures)
    trainmat = []
    for singlefeatures in rawfeatures:
        trainmat.append(words2vec(UniquesetList, singlefeatures))
        print(f"Processed document {rawfeatures.index(singlefeatures)}")
    pV, pos = trainNaiveB(np.array(trainmat), rawclasses)
    if not os.path.exists('models'):
        os.makedirs('models')
    np.save('models/pos.npy', np.array(pos))
    with open('models/UniquesetList.txt', 'w') as file:
        for word in UniquesetList:
            file.write(f"{word}\n")
    np.save('models/pV.npy', np.array(pV))