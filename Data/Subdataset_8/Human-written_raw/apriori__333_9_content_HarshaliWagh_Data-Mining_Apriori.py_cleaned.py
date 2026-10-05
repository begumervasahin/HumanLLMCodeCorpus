9. Repository: HarshaliWagh/Data-Mining
   File: Apriori.py
   URL: https:
   Code Content:
def candidate(freqitem, count):
    combination = []
    item = []
    for a in freqitem.keys():
        item.append(a)
    for i in range(0, len(freqitem)- 1, 1):
        for j in range(i+1, len(freqitem)):
            comb = []
            comb.append(item[i])
            comb.append(item[j])
            combination.append(comb)
    candi = []
    for i in range(len(combination)):
        p = []
        a = combination[i]
        b = ','.join(a)
        cand = b.split(',')
        for a in range(0, len(cand)):
            p.append(cand[a])
        candi.append(p)
    duplicatecand = []
    prunedcandi = []
    dell = []
    for i in range(0, len(candi)):
        p = set(candi[i])
        q = list(p)
        duplicatecand.append(q)
        if (len(duplicatecand[i]) == count):
           prunedcandi.append(duplicatecand[i])
        else:
            dell.append(duplicatecand[i])
    return(prunedcandi)
def support(can, data):
    supo = []
    w = []
    n = []
    for p in range(0, len(can)):
        a = set(can[p])
        z = set(a)
        w.append(z)
    for q in range(0, len(data)):
        b = set(data[q])
        o = set(b)
        n.append(o)
    for i in range(0, len(can)):
        counter = 0
        j=0
        for j in range(0, len(data)):
            if((w[i]).issubset(n[j])):
                counter = counter + 1
            j = j + 1
        supo.append(counter)
    return(supo)
def freqitemset(candidateg, sup, minsup):
    freq = {}
    for i in range(0, len(candidateg)):
        a = candidateg[i]
        b = ','.join(a)
        if(sup[i] >= minsup):
            freq[b] = sup[i]
    return(freq)
def freqlist(freqitemsetg, count):
    n = count - 1
    freqnew = []
    for x in freqitemsetg:
        a = x.split(',')
        freqnew.append(a)
    while(n !=0):
        for i in range(0, len(freqnew)):
            glue = []
            aso = association(freqnew[i], glue, n)
            print(aso)
            for j in range(0, len(aso)):
                dumpy = []
                for k in range(0, len(freqnew[i])):
                    if (freqnew[j][k] not in aso[j]):
                        dumpy.append(freqnew[i][k])
                        print(str(dumpy)+"--------->"+str(aso[j]))
        n = n - 1
    '''apriori = []
    supportx = []
    supportxy = []
    for trans in dataset:
        if set(dumpy[0]).issubset(set(trans)):
            supportx = supportx + 1
        if set(dumpy[0] + dumpy[i]).issubset(set(trans)):
            supportxy - supportxy + 1
        confidence = (supportxy / supportx) * 100
        if confidence >= minconf:
            print(confidence)'''
def association(freq, glue, n):
    if len(freq) == n:
        if glue.count(freq) == 0:
            glue.append(freq)
        return glue
    elif len(freq)!= n:
        for i in range(0,len(freq)):
            nextfreq = freq[i+1:] + freq[:i]
            glue = association(nextfreq, glue, n)
        return glue
dataset = []
print("Select the dataset:")
print("1 grocery")
print("2 clothing")
print("3 electronics")
print("4 utensils")
print("5 furniture")
finput = input("Enter number ")
minsup = int(input('Enter minimum Support: '))
minconf = int(input('Enter minimum Confidence: '))
fopen = ""
if finput == '1':
    fopen = "db1.txt"
elif finput == '2':
    fopen = "db2.txt"
elif finput == '3':
    fopen = "db3.txt"
elif finput == '4':
    fopen = "db4.txt"
else:
    fopen = "db5.txt"
fp = open(fopen, 'r')
while True:
    line = fp.readline()
    if not line :
        break;
    line = line.rstrip()
    dataset.append(line.split(", "))
itemdict = {}
for data in dataset:
    for item in data:
        if item in itemdict:
            itemdict[item] = itemdict[item] + 1
        else:
            itemdict[item] = 1
freq = {}
for i in range(0, len(itemdict)):
    for item, count in itemdict.items():
        if(count >= minsup):
            freq[item] = count
count = 2
candidateg = candidate(freq, count)
sup = support(candidateg, dataset)
freqitemsetg = freqitemset(candidateg, sup, minsup)
freqitemlist = freqlist(freqitemsetg, count)
temp = 0
count = 3
while(temp == 0):
    candidateg = candidate(freqitemsetg, count)
    sup = support(candidateg, dataset)
    freqitemsetg = freqitemset(candidateg, sup, minsup)
    freqitemlist = freqlist(freqitemsetg, count)
    count = count + 1
    for i in range(0, len(sup)):
        if(sup[i] >= minsup):
            temp = 0
            break
        else:
            temp = 1
            break
   README Content:
This code attempts to implements Apriori algorithm in Python from scratch.
List of Files -
1. Apriori.py
2 Dataset files - db1.txt, db2.txt, db3.txt, db4.txt, db5.txt
3 README file(this file)
