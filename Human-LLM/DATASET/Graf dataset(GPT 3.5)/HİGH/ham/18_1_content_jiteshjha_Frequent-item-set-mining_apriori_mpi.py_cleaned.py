1. Repository: jiteshjha/Frequent-item-set-mining
   File: apriori_mpi.py
   URL: https:
   Code Content:
import csv
import sys
import operator
import time
from math import floor
from mpi4py import MPI
from os import getcwd, walk, system, path
b1 = MPI.COMM_WORLD
b2 = b1.Get_rank()
b3 = time.clock()
def fonk1(b17, b19):
    b4 = None
    b5 = {}
    with open(b17, 'rb') as f:
        b4 = csv.reader(f)
        for a1 in b4:
            for j in a1:
                if j in b5:
                    b5[j.strip()] += 1
                else:
                    b5[j.strip()] = 1
    for item in b5.copy():
        if b5[item] < b19:
            b5.pop(item, None)
    return sorted(b5.items(), b6 = operator.itemgetter(0))
def fonk2(s, a3):
    b7 = len(s)
    b8 = []
    b9 = None
    for a1 in range(1, 1 << b7):
        b9 = [s[j] for j in range(b7) if (a1 & (1 << j))]
        if len(b9) == a3:
            b8.append(b9)
    return b8
def fonk3(b16, b22, a3):
    b10 = fonk2(b16, a3)
    for subset in b10:
        b11 = False
        for item in b22:
            if set(subset) == set(item[0].split(",")):
                b11 = True
                break
        if b11 = = False:
            return False
    return True
def fonk4(b22, a3):
    b12 = []
    for l1 in b22:
        for l2 in b22:
            b13 = l1[0].split(",")
            b14 = l2[0].split(",")
            a1 = 0
            b15 = True
            while a1 <= a3-2-1:
                if b13[a1] != b14[a1]:
                    b15 = False
                    break
                a1 += 1
            if not b13[a3-1-1] < b14[a3-1-1]:
                b15 = False
            if b15 = = True:
                b16 = sorted(set(b13) | set(b14))
                if fonk3(b9(b16), b22, a3-1):
                    b12.append(",".join(b9(b16)))
    return b12
def fonk5(b5, b20, a2):
    if len(b5) < 2:
        print "No association rules"
    else:
        b17 = str(sys.argv[1])
        print "\nMinimum Confidence Threshold: ", b20*100, "%\n"
        print "Association rules:\n"
        for a3 in range(1, len(b5)):
            for pair in b5[a3]:
                for a1 in range(1, len(b5[a3][0][0].split(','))):
                    for item in fonk2(pair[0].split(','), a1):
                        b18 = None
                        for j in b5[a1-1]:
                            if j[0] == ",".join(item):
                                b18 = int(j[1])
                        if b18 is not None and pair[1]/float(b18) >= b20:
                                print ",".join(item), "=>", ",".join(b9(set(pair[0].split(',')) - set(item))), "Support: ", float("{0:.2f}".format(float(b18)/a2))*100, "%", "Confidence: ", float("{0:.2f}".format(pair[1]/float(b18)*100)), "%"
def fonk6(b17):
    b19 = float(sys.argv[2])
    b20 = float(sys.argv[3])
    a2 = 0
    with open(b17, 'rb') as f:
        b4 = csv.reader(f)
        a2 = sum(1 for row in b4)
    b19 = b19 * a2
    b20 = b20 * a2
    b21 = fonk1(b17, b19)
    b5 = [b21]
    a3 = 2
    while True:
        if not b5[a3-2]:
            break
        b12 = fonk4(b5[a3-2], a3)
        b22 = {}
        with open(b17, 'rb') as f:
            b4 = csv.reader(f)
            for t in b4:
                for b16 in b12:
                    if set(b16.split(",")).issubset(set(t)):
                        if b16 in b22:
                            b22[b16] += 1
                        else:
                            b22[b16] = 1
        for item in b22.copy():
            if b22[item] < b19:
                b22.pop(item, None)
        b5.append(sorted(b22.items(), b6 = operator.itemgetter(0)))
        a3 += 1
    b5.pop()
    return b5
if b23 = = "__main__":
    b24 = []
    if b2 = = 0:
        """
            Make a directory called "temp"
            to split given b4 with the number of processes
        """
        system("mkdir temp")
        b4 = str(sys.argv[1])
        b25 = b1.Get_size()
        b26 = int(floor(path.getsize(b4)/(float(1000000) * b25)))
        system("split --b27 = " + str(b26)+"M " + b4 + " temp/retail")
        b28 = getcwd()
        for (dirpath, dirnames, filenames) in walk(b28+"/temp"):
            b24.extend(filenames)
            break
    b4 = b1.scatter(b24, root=0)
    b5 = fonk6("temp/"+b4)
    b29 = b1.gather(b5, root=0)
    if b2 = = 0:
        b30 = []
        b31 = max([len(itemsets) for itemsets in b29])
        for a1 in xrange(0, b31):
            b32 = set()
            for j in xrange(0, b25):
                b33 = []
                if(a1 <= (len(b29[j])-1)):
                    for item in b29[j][a1]:
                        b33.append(b9(item)[0])
                    b32 = b32.union(b9(b33))
            b30.append(dict((a3,0) for a3 in b9(b32)))
        system("rm -rf temp")
        b17 = str(sys.argv[1])
        a2 = 0
        with open(b17, 'rb') as f:
            b4 = csv.reader(f)
            for t in b4:
                for b5 in b30:
                    for item in b5:
                        if set(item.split(",")).issubset(set(t)):
                            b5[item] += 1
                a2 += 1
        b19 = float(sys.argv[2])
        for b5 in b30:
            for item in b5.copy():
                if (b5[item]/float(a2)) < b19:
                    b5.pop(item, None)
        print "\nResultant Item sets:"
        a3 = 1
        for b5 in b30:
            if bool(b5):
                print "\n", a3, "-itemsets:\n"
                a3 += 1
                for item in b5:
                    print item, "| Support ", float("{0:.2f}".format(b5[item]/float(a2)))*100, "%"
        b34 = [(sorted(b5.items(), b6=operator.itemgetter(0))) for b5 in b30 if bool(b5)]
        b20 = float(sys.argv[3])
        fonk5(b34, b20, a2)
print "\nRank : ",b2, " - Program Execution Time: ",time.clock() - b3, " seconds"
   README Content:
Apriori algorithm for discovering frequent itemsets for mining Boolean association rules.
**Motivation** : http:
**Original Paper** :
> *Rakesh Agrawal and Ramakrishnan Srikant Fast algorithms for mining association rules in large databases. Proceedings of the 20th International Conference on Very Large Data Bases, VLDB, pages 487-499, Santiago, Chile, September 1994.*
The algorithm can be executed with (Both minimum support and minimum confidence lie between [0, 1]):
    python apriori.py <data_set> <minimum_support> <minimum_confidence>
Example:
    python apriori.py datasets/retail.csv 0.3 0.6
`retail.dat` contains the (anonymized) retail market basket data from an anonymous Belgian retail store(Source: http:
Additionally, `retail.dat` was converted into `retail.csv` using `dat2csv.py` provided in the repository
