'''
Created on 15 de out de 2017
@author: raul
'''
from CreateBaseFromFile import CreateBaseFromFile
from sklearn.model_selection import train_test_split
from PCA import PCA as PCAR
from PCA import PCA_SCORE as PCARS
from PCA import FractionalPCA
from Base import Base
from Grafico import GerarGrafico
from classificadores import *
if b1 = = '__main__':
    a1 = 100
    b2 = CreateBaseFromFile.createFromFile("Bases/climate",[20],[0,1],1," ")
    b3 = CreateBaseFromFile.createFromFile("Bases/bankNote",[4],[])
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    for i in range(a1):
        train_atr, test_atr, train_classes, b4 = train_test_split(b2.atributos, b2.classes, test_size=0.5, random_state=i)
        b5 = len(b4)
        b6 = Base(train_classes,train_atr)
        a2 = classicarKNN(train_atr, train_classes, test_atr, b4) + a2
        a3 = naiveBayes(train_atr, train_classes, test_atr, b4) + a3
        a4 = arvoreDecisao(train_atr, train_classes, test_atr, b4) + a4
        train_atr, test_atr, train_classes, b4 = train_test_split(b3.atributos, b3.classes, test_size=0.5, random_state=i)
        b7 = len(b4)
        a5 = classicarKNN(train_atr, train_classes, test_atr, b4) + a5
        a6 = naiveBayes(train_atr, train_classes, test_atr, b4) + a6
        a7 = arvoreDecisao(train_atr, train_classes, test_atr, b4) + a7
    print("SEM PCA base Climate:\nerro KNN:%s\nacerto  NaiveBayes:%s\nerro arvore:%s\n"%(1-(a2/a1),1-(a3/a1),1-(a4/a1)))
    print("SEM PCA base BankNote:\nerro KNN:%s\nacerto  NaiveBayes:%s\nerro arvore:%s\n"%(1-(a5/a1),1-(a6/a1),1-(a7/a1)))
    b8 = [[],[],[],[]]
    b9 = [[],[],[],[]]
    b10 = list(range(1,19))
    for j in b10:
        b11 = [0]*4
        b12 = [0]*4
        for i in range(a1):
            b13 = PCAR()
            b14 = PCARS()
            train_atr, test_atr, train_classes, b4 = train_test_split(b2.atributos, b2.classes, test_size=0.5, random_state=i)
            b15 = Base(train_classes,train_atr)
            b13.fit(b15)
            b14.fit(b15)
            b16 = b13.run(Base(train_classes,train_atr), j)
            b17 = b13.run(Base(b4,test_atr),j)
            b18 = b14.run(Base(train_classes,train_atr), j)
            b19 = b14.run(Base(b4,test_atr),j)
            b5 = len(b4)
            b11[0] = classicarKNN(b16.atributos, b16.classes, b17.atributos, b17.classes) + b11[0]
            b11[1] = naiveBayes(b16.atributos, b16.classes, b17.atributos, b17.classes) + b11[1]
            b11[2] = arvoreDecisao(b16.atributos, b16.classes, b17.atributos, b17.classes) + b11[2]
            b11[3] = dlFisher(b16.atributos, b16.classes, b17.atributos, b17.classes) + b11[3]
            b12[0] = classicarKNN(b18.atributos, b18.classes, b19.atributos, b19.classes) + b12[0]
            b12[1] = naiveBayes(b18.atributos, b18.classes, b19.atributos, b19.classes) + b12[1]
            b12[2] = arvoreDecisao(b18.atributos, b18.classes, b19.atributos, b19.classes) + b12[2]
            b12[3] = dlFisher(b18.atributos, b18.classes, b19.atributos, b19.classes) + b12[3]
        print("COM PCA base Climate - atr:%s:\nacerto KNN:%s\nacerto NaiveBayes:%s\nacerto arvore:%s\nfisher:%s\n"%(j,1-(b11[0]/a1),1-(b11[2]/a1),1-(b11[2]/a1),1-(b11[3]/a1)))
        print("COM PCA Score base Climate - atr:%s:\nacerto KNN:%s\nacerto NaiveBayes:%s\nacerto arvore:%s\nfisher:%s\n"%(j,1-(b12[0]/a1),1-(b12[1]/a1),1-(b12[2]/a1),1-(b12[3]/a1)))
        for i,e in enumerate(b11):
            b8[i].append(1-e/a1)
            b9[i].append(1-b12[i]/a1)
    print("\n")
    GerarGrafico.saveMultuplos(b10, [b8[0],b9[0]], "taxa de acerto PCAs - KNN CLIMATE", "quantidade de atributos", "acerto", ["PCA","PCA Score"])
    GerarGrafico.saveMultuplos(b10, [b8[1],b9[1]], "taxa de acerto PCAs - Naive Bayes CLIMATE", "quantidade de atributos", "acerto", ["PCA","PCA Score"])
    GerarGrafico.saveMultuplos(b10, [b8[2],b9[2]], "taxa de acerto PCAs - Arvore CLIMATE", "quantidade de atributos", "acerto", ["PCA","PCA Score"])
    GerarGrafico.saveMultuplos(b10, [b8[3],b9[3]], "taxa de acerto PCAs - Fisher CLIMATE", "quantidade de atributos", "acerto", ["PCA","PCA Score"])
    b10 = list(range(1,5))
    b8 = [[],[],[],[]]
    b9 = [[],[],[],[]]
    for j in b10:
            b11 = [0]*4
            b12 = [0]*4
            for i in range(100):
                b13 = PCAR()
                b14 = PCARS()
                train_atr, test_atr, train_classes, b4 = train_test_split(b3.atributos, b3.classes, test_size=0.5, random_state=i)
                b15 = Base(train_classes,train_atr)
                b13.fit(b15)
                b14.fit(b15)
                b16 = b13.run(Base(train_classes,train_atr), j)
                b17 = b13.run(Base(b4,test_atr),j)
                b18 = b14.run(Base(train_classes,train_atr), j)
                b19 = b14.run(Base(b4,test_atr),j)
                b5 = len(b4)
                b11[0] = classicarKNN(b16.atributos, b16.classes, b17.atributos, b17.classes) + b11[0]
                b11[1] = naiveBayes(b16.atributos, b16.classes, b17.atributos, b17.classes) + b11[1]
                b11[2] = arvoreDecisao(b16.atributos, b16.classes, b17.atributos, b17.classes) + b11[2]
                b11[3] = dlFisher(b16.atributos, b16.classes, b17.atributos, b17.classes) + b11[3]
                b12[0] = classicarKNN(b18.atributos, b18.classes, b19.atributos, b19.classes) + b12[0]
                b12[1] = naiveBayes(b18.atributos, b18.classes, b19.atributos, b19.classes) + b12[1]
                b12[2] = arvoreDecisao(b18.atributos, b18.classes, b19.atributos, b19.classes) + b12[2]
                b12[3] = dlFisher(b18.atributos, b18.classes, b19.atributos, b19.classes) + b12[3]
            print("COM PCA base BANK - atr:%s:\nacerto KNN:%s\nacerto NaiveBayes:%s\nacerto arvore:%s\nfisher:%s\n"%(j,1-b11[0]/a1,1-b11[2]/a1,1-b11[2]/a1,1-b11[3]/a1))
            print("COM PCA Score base BANK - atr:%s:\nacerto KNN:%s\nacerto NaiveBayes:%s\nacerto arvore:%s\nfisher:%s\n"%(j,1-b12[0]/a1,1-b12[1]/a1,1-b12[2]/a1,1-b12[3]/a1))
            for i,e in enumerate(b11):
                b8[i].append(1-e/a1)
                b9[i].append(1-b12[i]/a1)
    print("\n")
    GerarGrafico.saveMultuplos(b10, [b8[0],b9[0]], "taxa de acerto PCAs - KNN BANK", "quantidade de atributos", "acerto", ["PCA","PCA Score"],[0,4],[0.9,1.2])
    GerarGrafico.saveMultuplos(b10, [b8[1],b9[1]], "taxa de acerto PCAs - Naive Bayes BANK", "quantidade de atributos", "acerto", ["PCA","PCA Score"],[0,4],[0.9,1.2])
    GerarGrafico.saveMultuplos(b10, [b8[2],b9[2]], "taxa de acerto PCAs - Arvore BANK", "quantidade de atributos", "acerto", ["PCA","PCA Score"],[0,4],[0.9,1.2])
    GerarGrafico.saveMultuplos(b10, [b8[3],b9[3]], "taxa de acerto PCAs - Fisher BANK", "quantidade de atributos", "acerto", ["PCA","PCA Score"],[0,4],[0.9,1.2])
    pass