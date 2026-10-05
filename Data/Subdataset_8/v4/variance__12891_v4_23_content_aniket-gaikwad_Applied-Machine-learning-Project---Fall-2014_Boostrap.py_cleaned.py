import sys
import random
__author__ = 'Aniket'
inputData = []
SIGMA = 0.66
NO_OF_BOOTSTRAPS = int(sys.argv[3])
def bootstrapping(trainSet):
    global bootstrap
    bootstrap = []
    print("Number of Instances: %d" % (len(trainSet)))
    sizeOfBootstrap = int(len(trainSet) / NO_OF_BOOTSTRAPS)
    print("One Bootstrap size: %d " % (sizeOfBootstrap))
    for i in range(NO_OF_BOOTSTRAPS):
        bootstrap_lst = []
        for j in range(sizeOfBootstrap):
            bootstrap_lst.append(random.choice(trainSet))
        bootstrap.append(bootstrap_lst)
    for i in range(NO_OF_BOOTSTRAPS):
        print("**********")
        print("Length: %d" % (len(bootstrap[i])))
def generateTrainTestSample(inputData):
    global trainSet, testSet
    trainSet = []
    testSet = []
    for line in range(len(inputData)):
        if random.random() < SIGMA:
            trainSet.append(inputData[line])
        else:
            testSet.append(inputData[line])
    print("Train Set:")
    print(trainSet)
    print("Test Set:")
    print(testSet)
    global noOfTestExamples
    noOfTestExamples = len(testSet)
def main(inputSet):
    global trainSet, testSet, bootstrap
    generateTrainTestSample(inputSet)
    bootstrapping(trainSet)
if __name__ == "__main__":
    main(inputData)