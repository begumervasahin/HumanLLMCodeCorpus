from collections import defaultdict
def candidate(freqitem, count):
    combination = []
    item = list(freqitem.keys())
    for i in range(len(freqitem) - 1):
        for j in range(i + 1, len(freqitem)):
            comb = [item[i], item[j]]
            combination.append(comb)
    candi = [comb.split(',') for comb in [','.join(comb) for comb in combination]]
    duplicatecand = []
    prunedcandi = []
    for i in range(len(candi)):
        p = set(candi[i])
        q = list(p)
        duplicatecand.append(q)
        if len(duplicatecand[i]) == count:
            prunedcandi.append(duplicatecand[i])
    return prunedcandi
def support(can, data):
    supo = []
    w = [set(can[p]) for p in range(len(can))]
    n = [set(data[q]) for q in range(len(data))]
    for i in range(len(can)):
        counter = sum(1 for j in range(len(data)) if w[i].issubset(n[j]))
        supo.append(counter)
    return supo
def freqitemset(candidateg, sup, minsup):
    freq = {}
    for i in range(len(candidateg)):
        a = candidateg[i]
        b = ','.join(a)
        if sup[i] >= minsup:
            freq[b] = sup[i]
    return freq
def freqlist(freqitemsetg, count):
    n = count - 1
    freqnew = [x.split(',') for x in freqitemsetg]
    while n != 0:
        for i in range(len(freqnew)):
            glue = []
            aso = association(freqnew[i], glue, n)
            for j in range(len(aso)):
                dumpy = [freqnew[i][k] for k in range(len(freqnew[i])) if freqnew[j][k] not in aso[j]]
                print(str(dumpy) + "--------->" + str(aso[j]))
        n = n - 1
def association(freq, glue, n):
    if len(freq) == n:
        if glue.count(freq) == 0:
            glue.append(freq)
        return glue
    elif len(freq) != n:
        for i in range(len(freq)):
            nextfreq = freq[i+1:] + freq[:i]
            glue = association(nextfreq, glue, n)
        return glue
def main():
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
    with open(fopen, 'r') as fp:
        dataset = [line.strip().split(", ") for line in fp]
    itemdict = defaultdict(int)
    for data in dataset:
        for item in data:
            itemdict[item] += 1
    freq = {item: count for item, count in itemdict.items() if count >= minsup}
    count = 2
    candidateg = candidate(freq, count)
    sup = support(candidateg, dataset)
    freqitemsetg = freqitemset(candidateg, sup, minsup)
    freqitemlist = freqlist(freqitemsetg, count)
if __name__ == "__main__":
    main()