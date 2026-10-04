26. Repository: RahulSingal/ProductRecommendations
   File: HW1.py
   URL: https:
   Code Content:
filename = open('browsingdata.txt', 'r')
dataset = filename.read().splitlines()
filename.close()
L1 = []
L2 = []
L3 = []
C1 = {}
C2 = {}
C3 = {}
practiceData = dataset[0:12]
for line in practiceData:
    while (len(line) > 0):
        if (line[0:8]) in C1:
            C1[line[0:8]] = C1[line[0:8]] + 1
        else:
            C1[line[0:8]] = 1
        line = line[9:]
for key in C1:
    if C1[key] > 3:
        L1.append(key)
i = 0
j = 0
for i in range (0, len(L1)):
    for j in range (i+1, len(L1)):
        C2[L1[i], L1[j]] = 0
count = 0
i = 0
j = 0
dict1 = {}
dict1['ELE17451'] = 1
dict1['ELE17451'] = dict1['ELE17451'] + 2
   README Content:
Market Basket Product Recommendations using the Apriori Algorithm
