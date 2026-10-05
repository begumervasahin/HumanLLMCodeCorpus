import CreateBaseFromFile
from sklearn.model_selection import train_test_split
from PCA import PCA as PCAR
from PCA import PCA_SCORE as PCARS
from Base import Base
from Grafico import GerarGrafico
from classificadores import *
def fonk1(base, a1, classifier_functions):
    b1 = [0] * len(classifier_functions)
    for i in range(a1):
        train_atr, test_atr, train_classes, b2 = train_test_split(base.atributos, base.classes, test_size=0.5, random_state=i)
        for idx, classifier_func in enumerate(classifier_functions):
            b1[idx] += classifier_func(train_atr, train_classes, test_atr, b2)
    return [(1 - (error / a1)) for error in b1]
def fonk2(base, a1, classifier_functions):
    b3 = []
    b4 = []
    b5 = list(range(1, len(base.atributos[0]) + 1))
    for num_attributes in b5:
        b1 = [0] * len(classifier_functions)
        b6 = [0] * len(classifier_functions)
        for i in range(a1):
            b7 = PCAR()
            b8 = PCARS()
            train_atr, test_atr, train_classes, b2 = train_test_split(base.atributos, base.classes, test_size=0.5, random_state=i)
            b9 = Base(train_classes, train_atr)
            b7.fit(b9)
            b8.fit(b9)
            b10 = b7.run(Base(train_classes, train_atr), num_attributes)
            b11 = b7.run(Base(b2, test_atr), num_attributes)
            b12 = b8.run(Base(train_classes, train_atr), num_attributes)
            b13 = b8.run(Base(b2, test_atr), num_attributes)
            for idx, classifier_func in enumerate(classifier_functions):
                b1[idx] += classifier_func(b10.atributos, b10.classes, b11.atributos, b11.classes)
                b6[idx] += classifier_func(b12.atributos, b12.classes, b13.atributos, b13.classes)
        b3.append([(1 - (error / a1)) for error in b1])
        b4.append([(1 - (error / a1)) for error in b6])
    return b3, b4
if b14 = = '__main__':
    a1 = 100
    b15 = CreateBaseFromFile.createFromFile("Bases/climate", [20], [0, 1], 1, " ")
    b16 = CreateBaseFromFile.createFromFile("Bases/bankNote", [4], [])
    b17 = [classicarKNN, naiveBayes, arvoreDecisao]
    b18 = fonk1(b15, a1, b17)
    b19 = fonk1(b16, a1, b17)
    print("WITHOUT PCA Climate Dataset:")
    print(f"KNN accuracy: {b18[0]}")
    print(f"Naive Bayes accuracy: {b18[1]}")
    print(f"Decision Tree accuracy: {b18[2]}\n")
    print("WITHOUT PCA Banknote Dataset:")
    print(f"KNN accuracy: {b19[0]}")
    print(f"Naive Bayes accuracy: {b19[1]}")
    print(f"Decision Tree accuracy: {b19[2]}\n")
    b17 = [classicarKNN, naiveBayes, arvoreDecisao, dlFisher]
    acerto_PCA_climate, b20 = fonk2(b15, a1, b17)
    acerto_PCA_bank, b21 = fonk2(b16, a1, b17)
    b22 = list(range(1, 19))
    b23 = list(range(1, 5))
    for idx, num_attributes in enumerate(b22):
        print(f"WITH PCA Climate Dataset - atr: {num_attributes}")
        print(f"KNN accuracy: {acerto_PCA_climate[idx][0]}")
        print(f"Naive Bayes accuracy: {acerto_PCA_climate[idx][1]}")
        print(f"Decision Tree accuracy: {acerto_PCA_climate[idx][2]}")
        print(f"Fisher accuracy: {acerto_PCA_climate[idx][3]}\n")
        print(f"WITH PCA Score Climate Dataset - atr: {num_attributes}")
        print(f"KNN accuracy: {b20[idx][0]}")
        print(f"Naive Bayes accuracy: {b20[idx][1]}")
        print(f"Decision Tree accuracy: {b20[idx][2]}")
        print(f"Fisher accuracy: {b20[idx][3]}\n")
    for idx, num_attributes in enumerate(b23):
        print(f"WITH PCA Banknote Dataset - atr: {num_attributes}")
        print(f"KNN accuracy: {acerto_PCA_bank[idx][0]}")
        print(f"Naive Bayes accuracy: {acerto_PCA_bank[idx][1]}")
        print(f"Decision Tree accuracy: {acerto_PCA_bank[idx][2]}")
        print(f"Fisher accuracy: {acerto_PCA_bank[idx][3]}\n")
        print(f"WITH PCA Score Banknote Dataset - atr: {num_attributes}")
        print(f"KNN accuracy: {b21[idx][0]}")
        print(f"Naive Bayes accuracy: {b21[idx][1]}")
        print(f"Decision Tree accuracy: {b21[idx][2]}")
        print(f"Fisher accuracy: {b21[idx][3]}\n")
    GerarGrafico.saveMultuplos(b22, [acerto_PCA_climate[i] for i in range(4)], "PCA Accuracy - Climate", "Number of Attributes", "Accuracy", ["KNN", "Naive Bayes", "Decision Tree", "Fisher"])
    GerarGrafico.saveMultuplos(b23, [acerto_PCA_bank[i] for i in range(4)], "PCA Accuracy - Banknote", "Number of Attributes", "Accuracy", ["KNN", "Naive Bayes", "Decision Tree", "Fisher"])
    GerarGrafico.saveMultuplos(b22, [b20[i] for i in range(4)], "PCA Score Accuracy - Climate", "Number of Attributes", "Accuracy", ["KNN", "Naive Bayes", "Decision Tree", "Fisher"])
    GerarGrafico.saveMultuplos(b23, [b21[i] for i in range(4)], "PCA Score Accuracy - Banknote", "Number of Attributes", "Accuracy", ["KNN", "Naive Bayes", "Decision Tree", "Fisher"])