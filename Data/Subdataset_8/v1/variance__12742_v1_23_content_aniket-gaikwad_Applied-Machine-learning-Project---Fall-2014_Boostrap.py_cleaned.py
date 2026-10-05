import sys
import random
inputData = []
SIGMA = 0.66
NO_OF_BOOTSTRAPS = int(sys.argv[1])
def bootstrapping(trainSet):
    bootstrap = []
    print("numberOfInstance : %d" % (len(trainSet)))
    sizeOfBootstrap = int(len(trainSet) / NO_OF_BOOTSTRAPS)
    print("One Bootstrap size : %d " % (sizeOfBootstrap))
    for i in range(NO_OF_BOOTSTRAPS):
        bootstrap_lst = []
        for j in range(sizeOfBootstrap):
            bootstrap_lst.append(random.choice(trainSet))
        bootstrap.append(bootstrap_lst)
    for i in range(NO_OF_BOOTSTRAPS):
        print("**********")
        print("length : %d" % (len(bootstrap[i])))
def generateTrainTestSample(inputData):
    trainSet = []
    testSet = []
    for line in range(len(inputData)):
        if random.random() < SIGMA:
            trainSet.append(inputData[line])
        else:
            testSet.append(inputData[line])
    print("Train : ")
    print(trainSet)
    print("Test :")
    print(testSet)
    noOfTestExamples = len(testSet)
def main(inputSet):
    generateTrainTestSample(inputSet)
    bootstrapping(trainSet)
if __name__ == "__main__":
    main(inputData)