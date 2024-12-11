import CreateBaseFromFile
from sklearn.model_selection import train_test_split
from PCA import PCA as PCAR
from PCA import PCA_SCORE as PCARS
from Base import Base
from Grafico import GerarGrafico
from classificadores import *
if b1 = = '__main__':
    a1 = 100
    b2 = CreateBaseFromFile.createFromFile("Bases/climate", [20], [0, 1], 1, " ")
    b3 = CreateBaseFromFile.createFromFile("Bases/bankNote", [4], [])
    erroKNNCli, erroNaiveCli, b4 = 0, 0, 0
    erroKNNBank, erroNaiveBank, b5 = 0, 0, 0
    for i in range(a1):
        train_atr, test_atr, train_classes, b6 = train_test_split(b2.atributos, b2.classes, test_size=0.5, random_state=i)
        b7 = Base(train_classes, train_atr)
        erroKNNCli += classicarKNN(train_atr, train_classes, test_atr, b6)
        erroNaiveCli += naiveBayes(train_atr, train_classes, test_atr, b6)
        b4 += arvoreDecisao(train_atr, train_classes, test_atr, b6)
        train_atr, test_atr, train_classes, b6 = train_test_split(b3.atributos, b3.classes, test_size=0.5, random_state=i)
        erroKNNBank += classicarKNN(train_atr, train_classes, test_atr, b6)
        erroNaiveBank += naiveBayes(train_atr, train_classes, test_atr, b6)
        b5 += arvoreDecisao(train_atr, train_classes, test_atr, b6)
    print("WITHOUT PCA Climate Dataset:")
    print(f"KNN error: {1 - (erroKNNCli / a1)}")
    print(f"Naive Bayes accuracy: {1 - (erroNaiveCli / a1)}")
    print(f"Decision Tree error: {1 - (b4 / a1)}\n")
    print("WITHOUT PCA Banknote Dataset:")
    print(f"KNN error: {1 - (erroKNNBank / a1)}")
    print(f"Naive Bayes accuracy: {1 - (erroNaiveBank / a1)}")
    print(f"Decision Tree error: {1 - (b5 / a1)}\n")
    b8 = [[], [], [], []]
    b9 = [[], [], [], []]
    b10 = list(range(1, 19))
    for j in b10:
        b11 = [0] * 4
        b12 = [0] * 4
        for i in range(a1):
            b13 = PCAR()
            b14 = PCARS()
            train_atr, test_atr, train_classes, b6 = train_test_split(b2.atributos, b2.classes, test_size=0.5, random_state=i)
            b15 = Base(train_classes, train_atr)
            b13.fit(b15)
            b14.fit(b15)
            b16 = b13.run(Base(train_classes, train_atr), j)
            b17 = b13.run(Base(b6, test_atr), j)
            b18 = b14.run(Base(train_classes, train_atr), j)
            b19 = b14.run(Base(b6, test_atr), j)
            b11[0] += classicarKNN(b16.atributos, b16.classes, b17.atributos, b17.classes)
            b11[1] += naiveBayes(b16.atributos, b16.classes, b17.atributos, b17.classes)
            b11[2] += arvoreDecisao(b16.atributos, b16.classes, b17.atributos, b17.classes)
            b11[3] += dlFisher(b16.atributos, b16.classes, b17.atributos, b17.classes)
            b12[0] += classicarKNN(b18.atributos, b18.classes, b19.atributos, b19.classes)
            b12[1] += naiveBayes(b18.atributos, b18.classes, b19.atributos, b19.classes)
            b12[2] += arvoreDecisao(b18.atributos, b18.classes, b19.atributos, b19.classes)
            b12[3] += dlFisher(b18.atributos, b18.classes, b19.atributos, b19.classes)
        print(f"WITH PCA Climate Dataset - atr: {j}")
        print(f"KNN accuracy: {1 - (b11[0] / a1)}")
        print(f"Naive Bayes accuracy: {1 - (b11[1] / a1)}")
        print(f"Decision Tree accuracy: {1 - (b11[2] / a1)}")
        print(f"Fisher accuracy: {1 - (b11[3] / a1)}\n")
        print(f"WITH PCA Score Climate Dataset - atr: {j}")
        print(f"KNN accuracy: {1 - (b12[0] / a1)}")
        print(f"Naive Bayes accuracy: {1 - (b12[1] / a1)}")
        print(f"Decision Tree accuracy: {1 - (b12[2] / a1)}")
        print(f"Fisher accuracy: {1 - (b12[3] / a1)}\n")
        for i, e in enumerate(b11):
            b8[i].append(1 - e / a1)
            b9[i].append(1 - b12[i] / a1)
    print("\n")
    GerarGrafico.saveMultuplos(b10, [b8[0], b9[0]], "PCA Accuracy - KNN CLIMATE", "Number of Attributes", "Accuracy", ["PCA", "PCA Score"])
    GerarGrafico.saveMultuplos(b10, [b8[1], b9[1]], "PCA Accuracy - Naive Bayes CLIMATE", "Number of Attributes", "Accuracy", ["PCA", "PCA Score"])
    GerarGrafico.saveMultuplos(b10, [b8[2], b9[2]], "PCA Accuracy - Decision Tree CLIMATE", "Number of Attributes", "Accuracy", ["PCA", "PCA Score"])
    GerarGrafico.saveMultuplos(b10, [b8[3], b9[3]], "PCA Accuracy - Fisher CLIMATE", "Number of Attributes", "Accuracy", ["PCA", "PCA Score"])
    b10 = list(range(1, 5))
    b8 = [[], [], [], []]
    b9 = [[], [], [], []]
    for j in b10:
        b11 = [0] * 4
        b12 = [0] * 4
        for i in range(a1):
            b13 = PCAR()
            b14 = PCARS()
            train_atr, test_atr, train_classes, b6 = train_test_split(b3.atributos, b3.classes, test_size=0.5, random_state=i)
            b15 = Base(train_classes, train_atr)
            b13.fit(b15)
            b14.fit(b15)
            b16 = b13.run(Base(train_classes, train_atr), j)
            b17 = b13.run(Base(b6, test_atr), j)
            b18 = b14.run(Base(train_classes, train_atr), j)
            b19 = b14.run(Base(b6, test_atr), j)
            b11[0] += classicarKNN(b16.atributos, b16.classes, b17.atributos, b17.classes)
            b11[1] += naiveBayes(b16.atributos, b16.classes, b17.atributos, b17.classes)
            b11[2] += arvoreDecisao(b16.atributos, b16.classes, b17.atributos, b17.classes)
            b11[3] += dlFisher(b16.atributos, b16.classes, b17.atributos, b17.classes)
            b12[0] += classicarKNN(b18.atributos, b18.classes, b19.atributos, b19.classes)
            b12[1] += naiveBayes(b18.atributos, b18.classes, b19.atributos, b19.classes)
            b12[2] += arvoreDecisao(b18.atributos, b18.classes, b19.atributos, b19.classes)
            b12[3] += dlFisher(b18.atributos, b18.classes, b19.atributos, b19.classes)
        print(f"WITH PCA Banknote Dataset - atr: {j}")
        print(f"KNN accuracy: {1 - (b11[0] / a1)}")
        print(f"Naive Bayes accuracy: {1 - (b11[1] / a1)}")
        print(f"Decision Tree accuracy: {1 - (b11[2] / a1)}")
        print(f"Fisher accuracy: {1 - (b11[3] / a1)}\n")
        print(f"WITH PCA Score Banknote Dataset - atr: {j}")
        print(f"KNN accuracy: {1 - (b12[0] / a1)}")
        print(f"Naive Bayes accuracy: {1 - (b12[1] / a1)}")
        print(f"Decision Tree accuracy: {1 - (b12[2] / a1)}")
        print(f"Fisher accuracy: {1 - (b12[3] / a1)}\n")
        for i, e in enumerate(b11):
            b8[i].append(1 - e / a1)
            b9[i].append(1 - b12[i] / a1)
    print("\n")
    GerarGrafico.saveMultuplos(b10, [b8[0], b9[0]], "PCA Accuracy - KNN BANK", "Number of Attributes", "Accuracy", ["PCA", "PCA Score"], [0, 4], [0.9, 1.2])
    GerarGrafico.saveMultuplos(b10, [b8[1], b9[1]], "PCA Accuracy - Naive Bayes BANK", "Number of Attributes", "Accuracy", ["PCA", "PCA Score"], [0, 4], [0.9, 1.2])
    GerarGrafico.saveMultuplos(b10, [b8[2], b9[2]], "PCA Accuracy - Decision Tree BANK", "Number of Attributes", "Accuracy", ["PCA", "PCA Score"], [0, 4], [0.9, 1.2])
    GerarGrafico.saveMultuplos(b10, [b8[3], b9[3]], "PCA Accuracy - Fisher BANK", "Number of Attributes", "Accuracy", ["PCA", "PCA Score"], [0, 4], [0.9, 1.2])