2. Repository: adwansyed/Market-Basket-Analysis-Apriori
   File: bruteforce_marketbasketanalysis.py
   URL: https:
   Code Content:
import time
def frequentTriples(dataset, tHold):
    myFile = open(dataset)
    triplesTable = {}
    lines = myFile.readlines()
    for line in lines:
        for item1 in line.split():
            for item2 in line.split():
                for item3 in line.split():
                    if (item1 < item2 and item2 < item3):
                        if (item1 +','+ item2 +','+ item3) not in triplesTable:
                            triplesTable[item1 +','+ item2 +','+ item3] = 1
                        else:
                            triplesTable[item1 +','+ item2 +','+ item3] += 1
    ordered = []
    for i in triplesTable:
        if triplesTable[i] > (len(lines) * tHold):
            ordered.append([triplesTable[i], i])
    ordered.sort(reverse=True)
    tot = 0
    for i in ordered:
        tot += 1
        print(tot, ')', i[1], ':', i[0])
def frequentDoubles(dataset, tHold):
    myFile = open(dataset)
    pairsTable = {}
    lines = myFile.readlines()
    pairsTable = {}
    for line in lines:
        for item1 in line.split():
            for item2 in line.split():
                if (item1 < item2):
                    if (item1 +','+ item2) not in pairsTable:
                        pairsTable[item1 +','+ item2] = 1
                    else:
                        pairsTable[item1 +','+ item2] += 1
    ordered2 = []
    for i in pairsTable:
        if pairsTable[i] > (len(lines) * tHold):
            ordered2.append([pairsTable[i], i])
    ordered2.sort(reverse=True)
    tot = 0
    for i in ordered2:
        tot += 1
        print(tot, ')', i[1], ':', i[0])
print('------------------------------------------------------------------------')
print('Running...')
print('Done!')
threshold = 0.03
start = time.time()
frequentDoubles('movies.dat',threshold)
end = time.time()
print('Time taken in seconds for frequent doubles:', end - start)
print('Done!')
print('------------------------------------------------------------------------')
print('Running...')
print('Done!')
start = time.time()
frequentTriples('movies.dat',threshold)
end = time.time()
print('Time taken in seconds for frequent triples:', end - start)
print('Done!')
   README Content:
Market basket analysis of retail and movie datasets.
Market basket analysis was performed using two methods:
- Brute force algorithm
- Apriori algorithm (performance enhancement using pruning technique)
