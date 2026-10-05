import sys
import random
import KNN
inputData = []
SIGMA = 0.66
NO_OF_BOOTSTRAPS = int(sys.argv[2])
bootstrap = []
def bootstrapping(trainSet):
    global bootstrap
    print("Number of Instances: %d" % len(trainSet))
    sizeOfBootstrap = int(len(trainSet) / NO_OF_BOOTSTRAPS)
    print("One Bootstrap size: %d" % sizeOfBootstrap)
    for i in range(NO_OF_BOOTSTRAPS):
        bootstrap_lst = []
        for j in range(sizeOfBootstrap):
            bootstrap_lst.append(random.choice(trainSet))
        bootstrap.append(bootstrap_lst)
    for i in range(NO_OF_BOOTSTRAPS):
        print("**********")
        print("Length: %d" % len(bootstrap[i]))
def generateTrainTestSample(inputFile):
    global trainSet, testSet
    trainSet = []
    testSet = []
    fin = open(inputFile, "r")
    for line in fin:
        newLine = line.strip()
        if random.random() < SIGMA:
            trainSet.append(newLine.split(','))
        else:
            testSet.append(newLine.split(','))
    fin.close()
def main():
    inputFile = sys.argv[1]
    generateTrainTestSample(inputFile)
    bootstrapping(trainSet)
    KNN.main(bootstrap[1], testSet, 3)
if __name__ == "__main__":
    main()