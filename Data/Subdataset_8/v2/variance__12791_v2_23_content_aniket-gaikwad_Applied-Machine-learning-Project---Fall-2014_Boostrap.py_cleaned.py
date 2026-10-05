import sys
import random
inputData = []
SIGMA = 0.66
NO_OF_BOOTSTRAPS = int(sys.argv[1])
def bootstrapping(trainSet):
    bootstrap = []
    print("Number of Instances: %d" % len(trainSet))
    sizeOfBootstrap = len(trainSet)
    print("Size of One Bootstrap: %d" % sizeOfBootstrap)
    for i in range(NO_OF_BOOTSTRAPS):
        bootstrap_lst = []
        for j in range(sizeOfBootstrap):
            bootstrap_lst.append(random.choice(trainSet))
        bootstrap.append(bootstrap_lst)
    for i in range(NO_OF_BOOTSTRAPS):
        print("**********")
        print("Length: %d" % len(bootstrap[i]))
def generateTrainTestSample(inputData):
    trainSet = []
    testSet = []
    for line in inputData:
        if random.random() < SIGMA:
            trainSet.append(line)
        else:
            testSet.append(line)
    print("Train Set:")
    print(trainSet)
    print("Test Set:")
    print(testSet)
def main(inputSet):
    generateTrainTestSample(inputSet)
    bootstrapping(trainSet)
if __name__ == "__main__":
    main(inputData)