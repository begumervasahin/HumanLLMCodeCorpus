2. Repository: adwansyed/Market-Basket-Analysis-Apriori
   File: bruteforce_marketbasketanalysis.py
   URL: https:
   Code Content:
import time
def fonk1(dataset, tHold):
    b1 = open(dataset)
    b2 = {}
    b3 = b1.readlines()
    for line in b3:
        for item1 in line.split():
            for item2 in line.split():
                for item3 in line.split():
                    if (item1 < item2 and item2 < item3):
                        if (item1 +','+ item2 +','+ item3) not in b2:
                            b2[item1 +','+ item2 +','+ item3] = 1
                        else:
                            b2[item1 +','+ item2 +','+ item3] += 1
    b4 = []
    for i in b2:
        if b2[i] > (len(b3) * tHold):
            b4.append([b2[i], i])
    b4.sort(b5 = True)
    a1 = 0
    for i in b4:
        a1 += 1
        print(a1, ')', i[1], ':', i[0])
def fonk2(dataset, tHold):
    b1 = open(dataset)
    b6 = {}
    b3 = b1.readlines()
    b6 = {}
    for line in b3:
        for item1 in line.split():
            for item2 in line.split():
                if (item1 < item2):
                    if (item1 +','+ item2) not in b6:
                        b6[item1 +','+ item2] = 1
                    else:
                        b6[item1 +','+ item2] += 1
    b7 = []
    for i in b6:
        if b6[i] > (len(b3) * tHold):
            b7.append([b6[i], i])
    b7.sort(b5 = True)
    a1 = 0
    for i in b7:
        a1 += 1
        print(a1, ')', i[1], ':', i[0])
print('------------------------------------------------------------------------')
print('Running...')
print('Done!')
a2 = 0.03
b8 = time.time()
fonk2('movies.dat',a2)
b9 = time.time()
print('Time taken in seconds for frequent doubles:', b9 - b8)
print('Done!')
print('------------------------------------------------------------------------')
print('Running...')
print('Done!')
b8 = time.time()
fonk1('movies.dat',a2)
b9 = time.time()
print('Time taken in seconds for frequent triples:', b9 - b8)
print('Done!')
   README Content:
Market basket analysis of retail and movie datasets.
Market basket analysis was performed using two methods:
- Brute force algorithm
- Apriori algorithm (performance enhancement using pruning technique)
