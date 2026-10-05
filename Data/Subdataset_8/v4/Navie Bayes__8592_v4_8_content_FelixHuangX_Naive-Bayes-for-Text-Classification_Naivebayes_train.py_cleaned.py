from numpy import *
from participle import *
import matplotlib.pyplot as plt
from wordcloud import WordCloud
def loadDataSet(rawpath, stoppath):
    result, data_target = fenci(rawpath, stoppath)
    return result, data_target
def createUniqueSet(dataset):
    UniqueSet = {}
    for i in range(len(dataset)):
        for word in dataset[i]:
            if word in UniqueSet:
                UniqueSet[word] += 1
            else:
                UniqueSet[word] = 1
        print(i)
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
        pNum = ones(numWords)
        pSum = 2.0
        for j in range(numTraindocs):
            if trainClass[j] == i:
                pNum += trainMat[j]
                pSum += sum(trainMat[j])
        print(i)
        pVec = log(pNum / pSum)
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
        print(rawfeatures.index(singlefeatures))
    pV, pos = trainNaiveB(array(trainmat), rawclasses)
    numpy_array1 = array(pos)
    save('models/pos.npy', numpy_array1)
    file = open('models/UniquesetList.txt', 'w')
    for i in range(len(UniquesetList)):
        file.write(UniquesetList[i])
        file.write('\n')
    file.close()
    numpy_array2 = array(pV)
    save('models/pV.npy', numpy_array2)