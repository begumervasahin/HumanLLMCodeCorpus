from sklearn.model_selection import train_test_split
from CreateBaseFromFile import CreateBaseFromFile
from PCA import PCA as PCAR
from PCA import PCA_SCORE as PCARS
from Base import Base
from classificadores import classicarKNN, naiveBayes, arvoreDecisao, dlFisher
from Grafico import GerarGrafico
if b1 = = '__main__':
    a1 = 100
    b2 = CreateBaseFromFile.createFromFile("Bases/climate", [20], [0, 1], 1, " ")
    b3 = CreateBaseFromFile.createFromFile("Bases/bankNote", [4], [])
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    for i in range(a1):
        train_atr, test_atr, train_classes, b4 = train_test_split(b2.atributos, b2.classes, test_size=0.5, random_state=i)
        a2 += classicarKNN(train_atr, train_classes, test_atr, b4)
        a3 += naiveBayes(train_atr, train_classes, test_atr, b4)
        a4 += arvoreDecisao(train_atr, train_classes, test_atr, b4)
        train_atr, test_atr, train_classes, b4 = train_test_split(b3.atributos, b3.classes, test_size=0.5, random_state=i)
        a5 += classicarKNN(train_atr, train_classes, test_atr, b4)
        a6 += naiveBayes(train_atr, train_classes, test_atr, b4)
        a7 += arvoreDecisao(train_atr, train_classes, test_atr, b4)
    print("WITHOUT PCA - Climate Dataset:")
    print("KNN Error:", 1 - a2 / a1)
    print("Naive Bayes Accuracy:", 1 - a3 / a1)
    print("Decision Tree Error:", 1 - a4 / a1)
    print()
    print("WITHOUT PCA - BankNote Dataset:")
    print("KNN Error:", 1 - a5 / a1)
    print("Naive Bayes Accuracy:", 1 - a6 / a1)
    print("Decision Tree Error:", 1 - a7 / a1)
    print()
    b5 = [[] for _ in range(4)]
    b6 = [[] for _ in range(4)]
    b7 = list(range(1, 19))
    for j in b7:
        b8 = [0] * 4
        b9 = [0] * 4
        for i in range(a1):
            b10 = PCAR()
            b11 = PCARS()
            train_atr, test_atr, train_classes, b4 = train_test_split(b2.atributos, b2.classes, test_size=0.5, random_state=i)
            b12 = Base(train_classes, train_atr)
            b10.fit(b12)
            b11.fit(b12)
            b13 = b10.run(Base(train_classes, train_atr), j)
            b14 = b10.run(Base(b4, test_atr), j)
            b15 = b11.run(Base(train_classes, train_atr), j)
            b16 = b11.run(Base(b4, test_atr), j)
            b8[0] += classicarKNN(b13.atributos, b13.classes, b14.atributos, b14.classes)
            b8[1] += naiveBayes(b13.atributos, b13.classes, b14.atributos, b14.classes)
            b8[2] += arvoreDecisao(b13.atributos, b13.classes, b14.atributos, b14.classes)
            b8[3] += dlFisher(b13.atributos, b13.classes, b14.atributos, b14.classes)
            b9[0] += classicarKNN(b15.atributos, b15.classes, b16.atributos, b16.classes)
            b9[1] += naiveBayes(b15.atributos, b15.classes, b16.atributos, b16.classes)
            b9[2] += arvoreDecisao(b15.atributos, b15.classes, b16.atributos, b16.classes)
            b9[3] += dlFisher(b15.atributos, b15.classes, b16.atributos, b16.classes)
        print("WITH PCA - Climate Dataset - Attributes:", j)
        print("KNN Accuracy:", 1 - b8[0] / a1)
        print("Naive Bayes Accuracy:", 1 - b8[1] / a1)
        print("Decision Tree Accuracy:", 1 - b8[2] / a1)
        print("Fisher Accuracy:", 1 - b8[3] / a1)
        print()
        print("WITH PCA Score - Climate Dataset - Attributes:", j)
        print("KNN Accuracy:", 1 - b9[0] / a1)
        print("Naive Bayes Accuracy:", 1 - b9[1] / a1)
        print("Decision Tree Accuracy:", 1 - b9[2] / a1)
        print("Fisher Accuracy:", 1 - b9[3] / a1)
        print()
        for i, e in enumerate(b8):
            b5[i].append(1 - e / a1)
            b6[i].append(1 - b9[i] / a1)
    b7 = list(range(1, 5))
    b5 = [[] for _ in range(4)]
    b6 = [[] for _ in range(4)]
    for j in b7:
        b8 = [0] * 4
        b9 = [0] * 4
        for i in range(100):
            b10 = PCAR()
            b11 = PCARS()
            train_atr, test_atr, train_classes, b4 = train_test_split(b3.atributos, b3.classes, test_size=0.5, random_state=i)
            b12 = Base(train_classes, train_atr)
            b10.fit(b12)
            b11.fit(b12)
            b13 = b10.run(Base(train_classes, train_atr), j)
            b14 = b10.run(Base(b4, test_atr), j)
            b15 = b11.run(Base(train_classes, train_atr), j)
            b16 = b11.run(Base(b4, test_atr), j)
            b8[0] += classicarKNN(b13.atributos, b13.classes, b14.atributos, b14.classes)
            b8[1] += naiveBayes(b13.atributos, b13.classes, b14.atributos, b14.classes)
            b8[2] += arvoreDecisao(b13.atributos, b13.classes, b14.atributos, b14.classes)
            b8[3] += dlFisher(b13.atributos, b13.classes, b14.atributos, b14.classes)
            b9[0] += classicarKNN(b15.atributos, b15.classes, b16.atributos, b16.classes)
            b9[1] += naiveBayes(b15.atributos, b15.classes, b16.atributos, b16.classes)
            b9[2] += arvoreDecisao(b15.atributos, b15.classes, b16.atributos, b16.classes)
            b9[3] += dlFisher(b15.atributos, b15.classes, b16.atributos, b16.classes)
        print("WITH PCA - Bank Dataset - Attributes:", j)
        print("KNN Accuracy:", 1 - b8[0] / a1)
        print("Naive Bayes Accuracy:", 1 - b8[1] / a1)
        print("Decision Tree Accuracy:", 1 - b8[2] / a1)
        print("Fisher Accuracy:", 1 - b8[3] / a1)
        print()
        print("WITH PCA Score - Bank Dataset - Attributes:", j)
        print("KNN Accuracy:", 1 - b9[0] / a1)
        print("Naive Bayes Accuracy:", 1 - b9[1] / a1)
        print("Decision Tree Accuracy:", 1 - b9[2] / a1)
        print("Fisher Accuracy:", 1 - b9[3] / a1)
        print()
        for i, e in enumerate(b8):
            b5[i].append(1 - e / a1)
            b6[i].append(1 - b9[i] / a1)
    print("\n")
    GerarGrafico.saveMultuplos(b7, [b5[0], b6[0]], "Accuracy with PCAs - KNN CLIMATE", "Number of attributes", "Accuracy", ["PCA", "PCA Score"])
    GerarGrafico.saveMultuplos(b7, [b5[1], b6[1]], "Accuracy with PCAs - Naive Bayes CLIMATE", "Number of attributes", "Accuracy", ["PCA", "PCA Score"])
    GerarGrafico.saveMultuplos(b7, [b5[2], b6[2]], "Accuracy with PCAs - Decision Tree CLIMATE", "Number of attributes", "Accuracy", ["PCA", "PCA Score"])
    GerarGrafico.saveMultuplos(b7, [b5[3], b6[3]], "Accuracy with PCAs - Fisher CLIMATE", "Number of attributes", "Accuracy", ["PCA", "PCA Score"])
    b7 = list(range(1, 5))
    GerarGrafico.saveMultuplos(b7, [b5[0], b6[0]], "Accuracy with PCAs - KNN BANK", "Number of attributes", "Accuracy", ["PCA", "PCA Score"], [0, 4], [0.9, 1.2])
    GerarGrafico.saveMultuplos(b7, [b5[1], b6[1]], "Accuracy with PCAs - Naive Bayes BANK", "Number of attributes", "Accuracy", ["PCA", "PCA Score"], [0, 4], [0.9, 1.2])
    GerarGrafico.saveMultuplos(b7, [b5[2], b6[2]], "Accuracy with PCAs - Decision Tree BANK", "Number of attributes", "Accuracy", ["PCA", "PCA Score"], [0, 4], [0.9, 1.2])
    GerarGrafico.saveMultuplos(b7, [b5[3], b6[3]], "Accuracy with PCAs - Fisher BANK", "Number of attributes", "Accuracy", ["PCA", "PCA Score"], [0, 4], [0.9, 1.2])