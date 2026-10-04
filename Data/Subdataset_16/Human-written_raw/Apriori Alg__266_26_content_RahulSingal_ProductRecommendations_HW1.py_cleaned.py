26. Repository: RahulSingal/ProductRecommendations
   File: HW1.py
   URL: https:
   Code Content:
b1 = open('browsingdata.txt', 'r')
b2 = b1.read().splitlines()
b1.close()
b3 = []
b4 = []
b5 = []
b6 = {}
b7 = {}
b8 = {}
b9 = b2[0:12]
for b10 in b9:
    while (len(b10) > 0):
        if (b10[0:8]) in b6:
            b6[b10[0:8]] = b6[b10[0:8]] + 1
        else:
            b6[b10[0:8]] = 1
        b10 = b10[9:]
for key in b6:
    if b6[key] > 3:
        b3.append(key)
a1 = 0
a2 = 0
for a1 in range (0, len(b3)):
    for a2 in range (a1+1, len(b3)):
        b7[b3[a1], b3[a2]] = 0
a3 = 0
a1 = 0
a2 = 0
b11 = {}
b11['ELE17451'] = 1
b11['ELE17451'] = b11['ELE17451'] + 2
   README Content:
Market Basket Product Recommendations using the Apriori Algorithm
