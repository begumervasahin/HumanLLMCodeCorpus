import numpy as np
import operator
def main():
    features, labels = loadDataSet()
    testFeatures = np.zeros((30, 4))
    testLabels = np.zeros(30)
    trainFeatures = np.zeros((120, 4))
    trainLabels = np.zeros(120)
    for i in range(3):
        testFeatures[i * 10: i * 10 + 10] = features[i * 50: i * 50 + 10]
        testLabels[i * 10: i * 10 + 10] = labels[i * 50: i * 50 + 10]
        trainFeatures[i * 10 * 4: i * 10 * 4 + 40] = features[i * 50 + 10: i * 50 + 50]
        trainLabels[i * 10 * 4: i * 10 * 4 + 40] = labels[i * 50 + 10: i * 50 + 50]
    errorCount = 0
    for i in range(30):
        classifierResult = classifierKNN(testFeatures[i], trainFeatures, trainLabels, 5)
        print(f"The classifier came back with: {classifierResult}, the real answer is: {testLabels[i]}")
        if classifierResult != testLabels[i]:
            errorCount += 1
    print(f"The total error rate is: {errorCount / float(30):.2f}")
def loadDataSet():
    iris = np.loadtxt(open("./Iris.csv", "rb"), delimiter=",", skiprows=1)
    features = iris[:, 1:5]
    labels = iris[:, 5].astype(int)
    return features, labels
def classifierKNN(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndices = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
if __name__ == "__main__":
    main()