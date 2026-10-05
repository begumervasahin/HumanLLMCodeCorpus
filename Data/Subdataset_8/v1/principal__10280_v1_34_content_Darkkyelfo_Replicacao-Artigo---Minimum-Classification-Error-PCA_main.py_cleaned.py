from sklearn.model_selection import train_test_split
from CreateBaseFromFile import CreateBaseFromFile
from PCA import PCA as PCAR
from PCA import PCA_SCORE as PCARS
from Base import Base
from classificadores import classicarKNN, naiveBayes, arvoreDecisao, dlFisher
from Grafico import GerarGrafico
if __name__ == '__main__':
    hold = 100
    baseClimate = CreateBaseFromFile.createFromFile("Bases/climate", [20], [0, 1], 1, " ")
    baseBank = CreateBaseFromFile.createFromFile("Bases/bankNote", [4], [])
    erroKNNCli = 0
    erroNaiveCli = 0
    erroArvoreCli = 0
    erroKNNBank = 0
    erroNaiveBank = 0
    erroArvoreBank = 0
    for i in range(hold):
        train_atr, test_atr, train_classes, test_classes = train_test_split(baseClimate.atributos, baseClimate.classes, test_size=0.5, random_state=i)
        erroKNNCli += classicarKNN(train_atr, train_classes, test_atr, test_classes)
        erroNaiveCli += naiveBayes(train_atr, train_classes, test_atr, test_classes)
        erroArvoreCli += arvoreDecisao(train_atr, train_classes, test_atr, test_classes)
        train_atr, test_atr, train_classes, test_classes = train_test_split(baseBank.atributos, baseBank.classes, test_size=0.5, random_state=i)
        erroKNNBank += classicarKNN(train_atr, train_classes, test_atr, test_classes)
        erroNaiveBank += naiveBayes(train_atr, train_classes, test_atr, test_classes)
        erroArvoreBank += arvoreDecisao(train_atr, train_classes, test_atr, test_classes)
    print("SEM PCA base Climate:\nerro KNN:%s\nacerto NaiveBayes:%s\nerro arvore:%s\n" % (1 - erroKNNCli / hold, 1 - erroNaiveCli / hold, 1 - erroArvoreCli / hold))
    print("SEM PCA base BankNote:\nerro KNN:%s\nacerto NaiveBayes:%s\nerro arvore:%s\n" % (1 - erroKNNBank / hold, 1 - erroNaiveBank / hold, 1 - erroArvoreBank / hold))
    acertoPCA = [[] for _ in range(4)]
    acertoPCAS = [[] for _ in range(4)]
    extraido = list(range(1, 19))
    for j in extraido:
        erros = [0] * 4
        errosScore = [0] * 4
        for i in range(hold):
            pcaR = PCAR()
            pcaRS = PCARS()
            train_atr, test_atr, train_classes, test_classes = train_test_split(baseClimate.atributos, baseClimate.classes, test_size=0.5, random_state=i)
            b = Base(train_classes, train_atr)
            pcaR.fit(b)
            pcaRS.fit(b)
            baseTreino = pcaR.run(Base(train_classes, train_atr), j)
            baseTeste = pcaR.run(Base(test_classes, test_atr), j)
            baseTreinoS = pcaRS.run(Base(train_classes, train_atr), j)
            baseTesteS = pcaRS.run(Base(test_classes, test_atr), j)
            erros[0] += classicarKNN(baseTreino.atributos, baseTreino.classes, baseTeste.atributos, baseTeste.classes)
            erros[1] += naiveBayes(baseTreino.atributos, baseTreino.classes, baseTeste.atributos, baseTeste.classes)
            erros[2] += arvoreDecisao(baseTreino.atributos, baseTreino.classes, baseTeste.atributos, baseTeste.classes)
            erros[3] += dlFisher(baseTreino.atributos, baseTreino.classes, baseTeste.atributos, baseTeste.classes)
            errosScore[0] += classicarKNN(baseTreinoS.atributos, baseTreinoS.classes, baseTesteS.atributos, baseTesteS.classes)
            errosScore[1] += naiveBayes(baseTreinoS.atributos, baseTreinoS.classes, baseTesteS.atributos, baseTesteS.classes)
            errosScore[2] += arvoreDecisao(baseTreinoS.atributos, baseTreinoS.classes, baseTesteS.atributos, baseTesteS.classes)
            errosScore[3] += dlFisher(baseTreinoS.atributos, baseTreinoS.classes, baseTesteS.atributos, baseTesteS.classes)
        print("COM PCA base Climate - atr:%s:\nacerto KNN:%s\nacerto NaiveBayes:%s\nacerto arvore:%s\nfisher:%s\n" % (j, 1 - erros[0] / hold, 1 - erros[1] / hold, 1 - erros[2] / hold, 1 - erros[3] / hold))
        print("COM PCA Score base Climate - atr:%s:\nacerto KNN:%s\nacerto NaiveBayes:%s\nacerto arvore:%s\nfisher:%s\n" % (j, 1 - errosScore[0] / hold, 1 - errosScore[1] / hold, 1 - errosScore[2] / hold, 1 - errosScore[3] / hold))
        for i, e in enumerate(erros):
            acertoPCA[i].append(1 - e / hold)
            acertoPCAS[i].append(1 - errosScore[i] / hold)
    extraido = list(range(1, 5))
    acertoPCA = [[] for _ in range(4)]
    acertoPCAS = [[] for _ in range(4)]
    for j in extraido:
        erros = [0] * 4
        errosScore = [0] * 4
        for i in range(100):
            pcaR = PCAR()
            pcaRS = PCARS()
            train_atr, test_atr, train_classes, test_classes = train_test_split(baseBank.atributos, baseBank.classes, test_size=0.5, random_state=i)
            b = Base(train_classes, train_atr)
            pcaR.fit(b)
            pcaRS.fit(b)
            baseTreino = pcaR.run(Base(train_classes, train_atr), j)
            baseTeste = pcaR.run(Base(test_classes, test_atr), j)
            baseTreinoS = pcaRS.run(Base(train_classes, train_atr), j)
            baseTesteS = pcaRS.run(Base(test_classes, test_atr), j)
            erros[0] += classicarKNN(baseTreino.atributos, baseTreino.classes, baseTeste.atributos, baseTeste.classes)
            erros[1] += naiveBayes(baseTreino.atributos, baseTreino.classes, baseTeste.atributos, baseTeste.classes)
            erros[2] += arvoreDecisao(baseTreino.atributos, baseTreino.classes, baseTeste.atributos, baseTeste.classes)
            erros[3] += dlFisher(baseTreino.atributos, baseTreino.classes, baseTeste.atributos, baseTeste.classes)
            errosScore[0] += classicarKNN(baseTreinoS.atributos, baseTreinoS.classes, baseTesteS.atributos, baseTesteS.classes)
            errosScore[1] += naiveBayes(baseTreinoS.atributos, baseTreinoS.classes, baseTesteS.atributos, baseTesteS.classes)
            errosScore[2] += arvoreDecisao(baseTreinoS.atributos, baseTreinoS.classes, baseTesteS.atributos, baseTesteS.classes)
            errosScore[3] += dlFisher(baseTreinoS.atributos, baseTreinoS.classes, baseTesteS.atributos, baseTesteS.classes)
        print("COM PCA base BANK - atr:%s:\nacerto KNN:%s\nacerto NaiveBayes:%s\nacerto arvore:%s\nfisher:%s\n" % (j, 1 - erros[0] / hold, 1 - erros[1] / hold, 1 - erros[2] / hold, 1 - erros[3] / hold))
        print("COM PCA Score base BANK - atr:%s:\nacerto KNN:%s\nacerto NaiveBayes:%s\nacerto arvore:%s\nfisher:%s\n" % (j, 1 - errosScore[0] / hold, 1 - errosScore[1] / hold, 1 - errosScore[2] / hold, 1 - errosScore[3] / hold))
        for i, e in enumerate(erros):
            acertoPCA[i].append(1 - e / hold)
            acertoPCAS[i].append(1 - errosScore[i] / hold)
    print("\n")
    GerarGrafico.saveMultuplos(extraido, [acertoPCA[0], acertoPCAS[0]], "taxa de acerto PCAs - KNN CLIMATE", "quantidade de atributos", "acerto", ["PCA", "PCA Score"])
    GerarGrafico.saveMultuplos(extraido, [acertoPCA[1], acertoPCAS[1]], "taxa de acerto PCAs - Naive Bayes CLIMATE", "quantidade de atributos", "acerto", ["PCA", "PCA Score"])
    GerarGrafico.saveMultuplos(extraido, [acertoPCA[2], acertoPCAS[2]], "taxa de acerto PCAs - Arvore CLIMATE", "quantidade de atributos", "acerto", ["PCA", "PCA Score"])
    GerarGrafico.saveMultuplos(extraido, [acertoPCA[3], acertoPCAS[3]], "taxa de acerto PCAs - Fisher CLIMATE", "quantidade de atributos", "acerto", ["PCA", "PCA Score"])
    extraido = list(range(1, 5))
    GerarGrafico.saveMultuplos(extraido, [acertoPCA[0], acertoPCAS[0]], "taxa de acerto PCAs - KNN BANK", "quantidade de atributos", "acerto", ["PCA", "PCA Score"], [0, 4], [0.9, 1.2])
    GerarGrafico.saveMultuplos(extraido, [acertoPCA[1], acertoPCAS[1]], "taxa de acerto PCAs - Naive Bayes BANK", "quantidade de atributos", "acerto", ["PCA", "PCA Score"], [0, 4], [0.9, 1.2])
    GerarGrafico.saveMultuplos(extraido, [acertoPCA[2], acertoPCAS[2]], "taxa de acerto PCAs - Arvore BANK", "quantidade de atributos", "acerto", ["PCA", "PCA Score"], [0, 4], [0.9, 1.2])
    GerarGrafico.saveMultuplos(extraido, [acertoPCA[3], acertoPCAS[3]], "taxa de acerto PCAs - Fisher BANK", "quantidade de atributos", "acerto", ["PCA", "PCA Score"], [0, 4], [0.9, 1.2])