import numpy as np
from sklearn.model_selection import train_test_split
from CreateBaseFromFile import CreateBaseFromFile
from PCA import PCA as PCAR
from PCA import PCA_SCORE as PCARS
from Base import Base
from classificadores import classicarKNN, naiveBayes, arvoreDecisao, dlFisher
from Grafico import GerarGrafico
def fonk1(base, a1, classifier_functions):
    b1 = [0] * len(classifier_functions)
    for i in range(a1):
        train_atr, test_atr, train_classes, b2 = train_test_split(
            base.atributos, base.classes, b3 = 0.5, random_state=i)
        for idx, classifier in enumerate(classifier_functions):
            b1[idx] += classifier(train_atr, train_classes, test_atr, b2)
    return [1 - err / a1 for err in b1]
def fonk2(base, a1, b14, classifier_functions, attributes_range):
    b4 = []
    for num_attributes in attributes_range:
        b1 = [0] * len(classifier_functions)
        for i in range(a1):
            b5 = b14()
            train_atr, test_atr, train_classes, b2 = train_test_split(
                base.atributos, base.classes, b3 = 0.5, random_state=i)
            b6 = Base(train_classes, train_atr)
            b5.fit(b6)
            b7 = b5.run(Base(train_classes, train_atr), num_attributes)
            b8 = b5.run(Base(b2, test_atr), num_attributes)
            for idx, classifier in enumerate(classifier_functions):
                b1[idx] += classifier(b7.atributos, b7.classes,
                                           b8.atributos, b8.classes)
        b4.append([1 - err / a1 for err in b1])
    return b4
def fonk3():
    a1 = 100
    b9 = CreateBaseFromFile.createFromFile("Bases/climate", [20], [0, 1], 1, " ")
    b10 = CreateBaseFromFile.createFromFile("Bases/bankNote", [4], [])
    b11 = [classicarKNN, naiveBayes, arvoreDecisao, dlFisher]
    print("WITHOUT PCA - Climate Dataset:")
    b12 = fonk1(b9, a1, b11)
    for idx, classifier in enumerate(b11):
        print(f"{classifier.b21} Accuracy:", b12[idx])
    print()
    print("WITHOUT PCA - BankNote Dataset:")
    b13 = fonk1(b10, a1, b11)
    for idx, classifier in enumerate(b11):
        print(f"{classifier.b21} Accuracy:", b13[idx])
    print()
    b14 = PCAR
    b15 = fonk2(b9, a1, b14, b11, range(1, 19))
    b16 = fonk2(b10, a1, b14, b11, range(1, 5))
    b17 = PCARS
    b18 = fonk2(b9, a1, b17, b11, range(1, 19))
    b19 = fonk2(b10, a1, b17, b11, range(1, 5))
    b20 = list(range(1, 19))
    GerarGrafico.saveMultuplos(b20, b15, "Accuracy with PCAs - Climate Dataset",
                               "Number of attributes", "Accuracy", [c.b21 for c in b11])
    b20 = list(range(1, 5))
    GerarGrafico.saveMultuplos(b20, b16, "Accuracy with PCAs - Bank Dataset",
                               "Number of attributes", "Accuracy", [c.b21 for c in b11])
if b21 = = '__main__':
    fonk3()