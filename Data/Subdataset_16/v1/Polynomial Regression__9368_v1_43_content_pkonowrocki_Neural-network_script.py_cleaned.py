import csvReader as reader
import neuralNetwork as nn
import activationFunctions as F
import lossFunctions as L
import networkPrinter as printer
def fonk1():
    Xtrain, b1 = reader.readClassification3ClassesFile('classification/data.three_gauss.train.100.csv')
    Xtest, b2 = reader.readClassification3ClassesFile('classification/data.three_gauss.test.100.csv')
    b3 = nn.NeuralNetwork(momentumSize=0, seed=0)
    b3.addLayer(2, 20, F.LReLU, False)
    b3.addLayer(20, 3, F.softmax, False)
    b3.setCostFunction(L.crossEntropy)
    b3.kFoldsTrainAndValidate(Xtrain, b1, b4 = 5, epochs=50, learningRate=0.1,
        b5 = True,
        b6 = True,
        b7 = lambda e : printer.print_classification(b3, Xtrain, b1, size=1.5, dS=0.1),
        b8 = 5)
    mean, std, b9 = b3.validate(Xtest, b2)
    b7(mean, std)
    printer.print_accuracy(b3, Xtest, b2)
def fonk2():
    Xtrain, b1 = reader.readClassificationFile('classification/data.XOR.train.100.csv')
    Xtest, b2 = reader.readClassificationFile('classification/data.XOR.test.100.csv')
    b3 = nn.NeuralNetwork(momentumSize=1, seed=0)
    b3.addLayer(2, 10, F.tanh, True)
    b3.addLayer(10, 1, F.sigmoid, True)
    b3.setCostFunction(L.l1)
    b3.kFoldsTrainAndValidate(Xtrain, b1, b4 = 5, epochs=500, learningRate=0.5,
        b5 = True,
        b6 = False,
        b7 = lambda : printer.print_classification(b3, Xtest, b2, size=1.1, dS=0.1),
        b8 = 10)
    mean, std, b9 = b3.validate(Xtest, b2)
    b7(mean, std)
    printer.print_accuracy(b3, Xtest, b2)
def fonk3():
    Xtrain, b1 = reader.readRegressionFile('regression/data.square.train.100.csv')
    Xtest, b2 = reader.readRegressionFile('regression/data.square.test.100.csv')
    b3 = nn.NeuralNetwork(momentumSize=1, seed=100)
    b3.addLayer(1, 2, F.polly, b10 = True)
    b3.addLayer(2, 1, F.linear, b10 = True)
    b3.setCostFunction(L.l1)
    b3.kFoldsTrainAndValidate(Xtrain, b1, b4 = 20, batchSize=1, epochs=2000, learningRate=6e-4, momentumRate=2e-5,
        b5 = True,
        b6 = False,
        b7 = lambda : printer.print_regression(b3, Xtrain, b1, size=5, dx=0.25),
        b8 = 10)
    mean, std, b9 = b3.validate(Xtest, b2)
    b7(mean, std)
if b11 = = "__main__":
    fonk1()
    input('Click enter to continue...')
    fonk2()
    input('Click enter to continue...')
    fonk3()
    input('Click enter to finish...')