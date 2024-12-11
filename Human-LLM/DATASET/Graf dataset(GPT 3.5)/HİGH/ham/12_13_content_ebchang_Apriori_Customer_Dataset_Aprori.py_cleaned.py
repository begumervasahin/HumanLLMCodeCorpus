13. Repository: ebchang/Apriori_Customer_Dataset
   File: Aprori.py
   URL: https:
   Code Content:
def read (filename):
    b1 = open(filename)
    b2 = b1.readline()
    b3 = b1.readlines()
    b4 = {}
    b1.close()
    for i in range(len(b3)):
        b3[i] = b3[i].split(',')
    for t in range(len(b3)):
        b4.setdefault(b3[t][0],[]).append(b3[t][1])
    b3 = list(b4.values())
    return b3
def fonk1(filename):
    b1 = open(filename)
    b2 = b1.readline()
    b3 = b1.readlines()
    b4 = {}
    b1.close()
    for i in range(len(b3)):
        b3[i] = b3[i].split(",")
    for t in range(len(b3)):
        b4.setdefault(b3[t][0],[]).append(b3[t][1:])
    return b3
def fonk2(b3):
    b5 = []
    for c in b3:
        for b19 in c:
            if [b19] not in b5:
                b5.append([b19])
    b5.sort()
    return map(frozenset,b5)
b6 = list(fonk2(read("10000_dataset.txt")))
b3 = read("10000_dataset.txt")
b7 = map(set, b3)
b8 = len(list(map(set,b3)))
def fonk3(b7, b8, b6, min_support):
    "returns all b19 itemsets that meet min_support level"
    b9 = {}
    for item in b7:
        for can in b6:
            if can.issubset(item):
                b9.setdefault(can, 0)
                b9[can] += 1
    b10 = float(b8)
    b5 = []
    b11 = {}
    for key in b9:
        b12 = b9[key]/b10
        if b12 >= min_support:
            b5.insert(0,key)
        b11[key] = b12
    return b5, b11
def fonk4(b5, a1):
    b13 = []
    b14 = len(b5)
    for i in range(b14):
        for j in range(i +1, b14):
            b15 = list(b5[i])[:a1 -2]
            b16 = list(b5[j])[:a1 -2]
            b15.sort()
            b16.sort()
            if b15 = = b16:
                b13.append(b5[i] | b5[j])
    return  b13
def fonk5(b3, b17 = 0.05):
    b18 = list(fonk2(read("/Users/evanchang/Desktop/10000_dataset.txt")))
    b7 = map(set,b3)
    b8 = len(list(map(set,b3)))
    b15, b11 = fonk3(b7,b8 ,b18, b17)
    b5 = [b15]
    b7 = map(set,b3)
    a1 = 2
    while (len(b5[a1-2]) > 0):
        b19 = fonk4(b5[a1-2],a1)
        b7 = map(set,b3)
        lk, b20 = fonk3(b7,b8, b19 ,b17)
        b11.update(b20)
        b5.append(lk)
        a1 +=1
    return b5, b11
l , b11 = fonk5(b3, 0.5)
def fonk6(b5, b11, b21 = 0.9):
    b22 = []
    for i in range (1, len(b5)):
        for freqSet in b5[i]:
            b23 = [frozenset([item]) for item in freqSet]
            if (i> 1):
                fonk9(freqSet, b23, b11, b22, b21)
            else:
                fonk7(freqSet, b23, b11, b22, b21)
    return b22
def fonk7(freqSet, b23, b11, b22, b21):
    b24 = []
    for conseq in b23:
        b25 = b11[freqSet]/ b11[freqSet - conseq]
        if b25 >= b21:
            b22.append((freqSet-conseq, conseq, b25))
            b24.append(conseq)
    return b24
def fonk8(b5, b11):
    b22 = []
    for i in range (1, len(b5)):
        for freqSet in b5[i]:
            b23 = [frozenset([item]) for item in freqSet]
            if (i> 1):
                fonk11(freqSet, b23, b11, b22)
            else:
                fonk10(freqSet, b23, b11, b22)
    return b22
def fonk9(freqSet, b23, b11, b22, b21):
    b26 = len(b23[0])
    if (len(freqSet) > (b26+1)):
        b27 = fonk4(b23, b26+1)
        b27 = fonk7(freqSet, b27, b11, b22, b21)
        if len(b27) > 1:
            fonk9(freqSet, b27, b11, b22, b21)
def fonk10(freqSet, b23, b11, b22):
    b24 = []
    for conseq in b23:
        b28 = b11[freqSet]/ (b11[freqSet-conseq] * b11[freqSet])
        if b28 > 1:
            b22.append((freqSet-conseq, conseq, b28))
            b24.append(conseq)
    return b24
def fonk11(freqSet, b23, b11, b22):
    b26 = len(b23[0])
    if (len(freqSet) > (b26+1)):
        b27 = fonk4(b23, b26+1)
        b27 = fonk10(freqSet, b27, b11, b22)
        if len(b27) > 1:
            fonk11(freqSet, b27, b11, b22)
   README Content:
_NOTE_: The data for the examples below are from data1.txt
The Aprori function takes a b3 and a minimum b12.
This will give the frequent sets and the b11 along with the frequent sets.
b5, b11 = fonk5(b3, 0.5)
Then you can generate the b22 using GenerateRules to make b22 based on confidence or use GenerateRules_lift to make b22 based on b28.
Sample output for generateRules based on confidence.
[(frozenset({' White'}), frozenset({' United-States'}), 0.9307692307692308), (frozenset({' United-States'}), frozenset({' White'}), 0.8752260397830018), (frozenset({' White'}), frozenset({' Male'}), 0.7009615384615385), (frozenset({' Male'}), frozenset({' Wh
ite'}), 0.8868613138686132), (frozenset({' Private'}), frozenset({' <=50K\n'}), 0.7857948139797069), (frozenset({' <=50K\n'}), frozenset({' Private'}), 0.7667766776677668), (frozenset({' Private'}), frozenset({' White'}), 0.8602029312288613), (frozenset({' White'}), frozenset({' Private'}), 0.7336538461538461), (frozenset({' <=50K\n'}), frozenset({' United-States'}), 0.9086908690869087), (frozenset({' United-States'}), frozenset({' <=50K\n'}), 0.7468354430379747), (frozenset({' <=50K\n'}), frozenset({' White'}), 0.8426842684268426), (frozenset({' White'}), frozenset({' <=50K\n'}), 0.7365384615384615), (frozenset({' Private'}), frozenset({' United-States'}), 0.9098083427282976), (frozenset({' United-States'}), frozenset({' Private'}), 0.7296564195298373), (frozenset({' Male'}), frozenset({' United-States'}), 0.9172749391727494), (frozenset({' <=50K\n'}), frozenset({' White', ' United-States'}), 0.7766776677667766), (frozenset({' Private'}), frozenset({' United-States', ' <=50K\n'}), 0.7080045095828635), (frozenset({' Private'}), frozenset({' White', ' United-States'}), 0.7959413754227733), (frozenset({' Male'}), frozenset({' White', ' United-States'}), 0.8284671532846716)]
The frozen sets is the key and items and the number is the confidence calculated.
For generateRules_lift sample output will be:
[(frozenset({' White'}), frozenset({' United-States'}), 1.1625), (frozenset({' United-States'}), frozenset({' White'}), 1.093128390596745), (frozenset({' White'}), frozenset({' Male'}), 1.1625), (frozenset({' Male'}), frozenset({' White'}), 1.4708029197080292), (frozenset({' Private'}), frozenset({' <=50K\n'}), 1.363021420518602), (frozenset({' <=50K\n'}), frozenset({' Private'}), 1.33003300330033), (frozenset({' Private'}), frozenset({' White'}), 1.363021420518602), (frozenset({' White'}), frozenset({' Private'}), 1.1624999999999999), (frozenset({' <=50K\n'}), frozenset({' United-States'}), 1.33003300330033)
The frozen set are the items and the number after is the b28. It will give b22 where the b28 is greater than 1.
fonk3() Takes a set b3, the number of transactions, b6 list of 1 and the minimum_support threshold.
fonk4() will take the candidate sets of 1 and 2, which will join and append all the combination of data sets.
reference: Machine Learning in Action by Peter Harrington. Chapter 11
