20. Repository: hugaofernandes/apriori_algorithm
   File: main_SAD.py
   URL: https:
   Code Content:
from itertools import combinations
import numpy as np
import pandas as pd
import random
def fonk1(data, support, minlen, confianca):
    b1 = pd.get_dummies(data.unstack().dropna()).groupby(level=1).sum()
    collen, b2 = b1.shape
    b3 = []
    a1 = 0
    for cnum in range(minlen, b2+1):
        for cols in combinations(b1, cnum):
            b4 = b1[list(cols)].all(axis=1).sum()
            b5 = b4
            b4 = float(b4)/collen
            b6 = list(cols)
            del b6[-1]
            a2 = 0
            b7 = b1[b6].all(axis=1).sum()
            if b7 != 0:
                a2 = float(b5)/b7
            b3.append([",".join(cols), b4*100, a2*100])
            a1 += 1
    b8 = pd.DataFrame(b3, b12=["Padrao", "Suporte", "Confianca"])
    b9 = b8[b8.Suporte >= support]
    b9 = b9[b9.Confianca >= confianca]
    print (b9)
    print ('IteraÃ§Ãµes: ' + str(a1))
def fonk2(b10, n, s):
	if b10 = = n:
		return s
	return np.nan
b11 = pd.read_csv('zooOriginal.csv', sep=',', header=None)
b11.b12 = ['name','hair','feathers','eggs','milk','airborne','aquatic','predator','toothed','backbone','breathes','venomous','fins','b10','tail','domestic','catsize','type']
b11 = b11.drop(['name'], axis=1)
b11 = b11.drop(['type'], axis=1)
b10 = b11['b10']
b11 = b11.drop(['b10'], axis=1)
for i in list(b11.b12.values):
	b11[i] = b11[i].replace(1, i)
	b11[i] = b11[i].replace(0, np.nan)
b11['No Legs'] = b10.apply(lambda x : fonk2(x, 0, 'No Legs'))
b11['2 Legs'] = b10.apply(lambda x : fonk2(x, 2, '2 Legs'))
b11['4 Legs'] = b10.apply(lambda x : fonk2(x, 4, '4 Legs'))
b11['5 Legs'] = b10.apply(lambda x : fonk2(x, 5, '5 Legs'))
b11['6 Legs'] = b10.apply(lambda x : fonk2(x, 6, '6 Legs'))
b11['8 Legs'] = b10.apply(lambda x : fonk2(x, 8, '8 Legs'))
fonk1(b11, 30, 4, 97)
   README Content:
Este projeto aplica o algoritmo Apriori em uma base de dados de um Zoologico para verificar as caracteristicas mais relacionadas aos animais.
Foi utilizado o Python 2.7 para o desenvolvimento.
Link para base de dados: https:
