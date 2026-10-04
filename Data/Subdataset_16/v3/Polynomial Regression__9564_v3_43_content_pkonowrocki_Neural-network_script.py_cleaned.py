import csvReader as reader
import neuralNetwork as nn
import activationFunctions as F
import lossFunctions as L
import networkPrinter as printer
def fonk1():
    X_train, b1 = reader.readClassification3ClassesFile('classification/data.three_gauss.train.100.csv')
    X_test, b2 = reader.readClassification3ClassesFile('classification/data.three_gauss.test.100.csv')
    b3 = nn.NeuralNetwork(momentumSize=0, seed=0)
    b3.addLayer(b4 = 2, output_size=20, activation_function=F.LReLU, use_bias=False)
    b3.addLayer(b4 = 20, output_size=3, activation_function=F.softmax, use_bias=False)
    b3.setCostFunction(L.crossEntropy)
    b3.kFoldsTrainAndValidate(
        X_train, b1, b5 = 5, epochs=50, learning_rate=0.1,
        b6 = True,
        b7 = True,
        b8 = lambda e: printer.print_classification(b3, X_train, b1, size=1.5, dS=0.1),
        a1 = 5
    )
    mean, std, b9 = b3.validate(X_test, b2)
    b8(f'Mean: {mean}, Std: {std}, Error: {b9}')
    printer.print_accuracy(b3, X_test, b2)
def fonk2():
    X_train, b1 = reader.readClassificationFile('classification/data.XOR.train.100.csv')
    X_test, b2 = reader.readClassificationFile('classification/data.XOR.test.100.csv')
    b3 = nn.NeuralNetwork(momentumSize=1, seed=0)
    b3.addLayer(b4 = 2, output_size=10, activation_function=F.tanh, use_bias=True)
    b3.addLayer(b4 = 10, output_size=1, activation_function=F.sigmoid, use_bias=True)
    b3.setCostFunction(L.l1)
    b3.kFoldsTrainAndValidate(
        X_train, b1, b5 = 5, epochs=500, learning_rate=0.5,
        b6 = True,
        b7 = False,
        b8 = lambda: printer.print_classification(b3, X_test, b2, size=1.1, dS=0.1),
        a1 = 10
    )
    mean, std, b9 = b3.validate(X_test, b2)
    b8(f'Mean: {mean}, Std: {std}, Error: {b9}')
    printer.print_accuracy(b3, X_test, b2)
def fonk3():
    X_train, b1 = reader.readRegressionFile('regression/data.square.train.100.csv')
    X_test, b2 = reader.readRegressionFile('regression/data.square.test.100.csv')
    b3 = nn.NeuralNetwork(momentumSize=1, seed=100)
    b3.addLayer(b4 = 1, output_size=2, activation_function=F.polly, use_bias=True)
    b3.addLayer(b4 = 2, output_size=1, activation_function=F.linear, use_bias=True)
    b3.setCostFunction(L.l1)
    b3.kFoldsTrainAndValidate(
        X_train, b1, b5 = 20, batch_size=1, epochs=2000, learning_rate=6e-4, momentum_rate=2e-5,
        b6 = True,
        b7 = False,
        b8 = lambda: printer.print_regression(b3, X_train, b1, size=5, dx=0.25),
        a1 = 10
    )
    mean, std, b9 = b3.validate(X_test, b2)
    b8(f'Mean: {mean}, Std: {std}, Error: {b9}')
if b10 = = "__main__":
    fonk1()
    input('Click enter to continue...')
    fonk2()
    input('Click enter to continue...')
    fonk3()
    input('Click enter to finish...')