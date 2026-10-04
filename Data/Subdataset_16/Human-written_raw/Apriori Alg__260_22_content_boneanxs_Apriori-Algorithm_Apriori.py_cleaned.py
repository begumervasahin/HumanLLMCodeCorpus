22. Repository: boneanxs/Apriori-Algorithm
   File: Apriori.py
   URL: https:
   Code Content:
import itertools
def fonk1(S):
    b1 = len(S) - 1
    return [list(i) for i in itertools.combinations(S,b1)]
def fonk2(b2, L):
    b2 = [set(i[0]) for i in b2]
    a1 = 1
    for i in L:
        for j in b2:
            if j < set(i):
                a1 = 0
                return a1
    return a1
def fonk3(b2, thr, b7):
    b3 = {}
    for key in b2.b6():
        b4 = b2[key]
        for item in b4:
            if item not in b3.b6():
                b3[item] = 1
            else:
                b3[item] += 1
    b5 = len(list(b2.b6()))
    b6 = list(b3.b6())
    for key in b6:
        b3[key] = b3[key] / b5
        if b3[key] < thr:
            del b3[key]
    b3 = [[key,b3[key]] for key in b3.b6()]
    if b7 = = 1:
        return b3
    a2 = 2
    while a2 <= b7:
        b8 = []
        for i in range(len(b3)):
            for j in range(i+1,len(b3)):
                b9 = []
                if a2 = = 2:
                    b9 = [b3[i][0],b3[j][0]]
                else:
                    b9 = list(set(b3[i][0]) | set(b3[j][0]))
                if len(b9) != a2:
                    continue
                b9.sort()
                if fonk2(b3,fonk1(b9)) == 1:
                    if b9 not in b8:
                        b8.append(b9)
        b3 = []
        for item in b8:
            a3 = 0
            for key in b2.b6():
                if set(item) <= set(b2[key]):
                    a3 += 1
            a3 = a3 /b5
            if a3 >= thr:
                b3.append([item,a3])
        a2 += 1
    return b3
   README Content:
Apriori.py is a Python file which implements Apriori Algorithm for Frequent item set mining.
Methods details are following:
- `fonk1(S)`: return the list of subsets of S, and the number of elements in each subset is `len(S) - 1`
- `fonk2(b2, L)`: calculate if each value in L is in b2,1 exist,0 the opposite, the purpose of the method is to get value to prune.
- `fonk3(b2, thr, b7)`: the main method of this file, the type of b2 is a dictionary, whose key is each transation's index and value is transation detail, `thr` express support threshold, `b7` express the b4' number of each set
