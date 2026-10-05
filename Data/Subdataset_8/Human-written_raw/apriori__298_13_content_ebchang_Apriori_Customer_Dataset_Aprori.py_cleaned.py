13. Repository: ebchang/Apriori_Customer_Dataset
   File: Aprori.py
   URL: https:
   Code Content:
def read (filename):
    raw = open(filename)
    hold = raw.readline()
    dataset = raw.readlines()
    id_hold = {}
    raw.close()
    for i in range(len(dataset)):
        dataset[i] = dataset[i].split(',')
    for t in range(len(dataset)):
        id_hold.setdefault(dataset[t][0],[]).append(dataset[t][1])
    dataset = list(id_hold.values())
    return dataset
def read_data1(filename):
    raw = open(filename)
    hold = raw.readline()
    dataset = raw.readlines()
    id_hold = {}
    raw.close()
    for i in range(len(dataset)):
        dataset[i] = dataset[i].split(",")
    for t in range(len(dataset)):
        id_hold.setdefault(dataset[t][0],[]).append(dataset[t][1:])
    return dataset
def find_candidates(dataset):
    freq_sets = []
    for c in dataset:
        for freq in c:
            if [freq] not in freq_sets:
                freq_sets.append([freq])
    freq_sets.sort()
    return map(frozenset,freq_sets)
candidates = list(find_candidates(read("10000_dataset.txt")))
dataset = read("10000_dataset.txt")
D = map(set, dataset)
D_list = len(list(map(set,dataset)))
def find_freq(D, D_list, candidates, min_support):
    "returns all freq itemsets that meet min_support level"
    dict_holder = {}
    for item in D:
        for can in candidates:
            if can.issubset(item):
                dict_holder.setdefault(can, 0)
                dict_holder[can] += 1
    num_items = float(D_list)
    freq_sets = []
    support_data = {}
    for key in dict_holder:
        support = dict_holder[key]/num_items
        if support >= min_support:
            freq_sets.insert(0,key)
        support_data[key] = support
    return freq_sets, support_data
def joint_set(freq_sets, k):
    joint_freq = []
    lenlk = len(freq_sets)
    for i in range(lenlk):
        for j in range(i +1, lenlk):
            l1 = list(freq_sets[i])[:k -2]
            l2 = list(freq_sets[j])[:k -2]
            l1.sort()
            l2.sort()
            if l1 == l2:
                joint_freq.append(freq_sets[i] | freq_sets[j])
    return  joint_freq
def apriori(dataset, minsupport = 0.05):
    C1 = list(find_candidates(read("/Users/evanchang/Desktop/10000_dataset.txt")))
    D = map(set,dataset)
    D_list = len(list(map(set,dataset)))
    l1, support_data = find_freq(D,D_list ,C1, minsupport)
    freq_sets = [l1]
    D = map(set,dataset)
    k = 2
    while (len(freq_sets[k-2]) > 0):
        freq = joint_set(freq_sets[k-2],k)
        D = map(set,dataset)
        lk, supportK = find_freq(D,D_list, freq ,minsupport)
        support_data.update(supportK)
        freq_sets.append(lk)
        k +=1
    return freq_sets, support_data
l , support_data = apriori(dataset, 0.5)
def generateRules(freq_sets, support_data, min_confidence = 0.9):
    rules = []
    for i in range (1, len(freq_sets)):
        for freqSet in freq_sets[i]:
            h1 = [frozenset([item]) for item in freqSet]
            if (i> 1):
                rules_from_conseq(freqSet, h1, support_data, rules, min_confidence)
            else:
                calc_confidence(freqSet, h1, support_data, rules, min_confidence)
    return rules
def calc_confidence(freqSet, h1, support_data, rules, min_confidence):
    pruned_h = []
    for conseq in h1:
        conf = support_data[freqSet]/ support_data[freqSet - conseq]
        if conf >= min_confidence:
            rules.append((freqSet-conseq, conseq, conf))
            pruned_h.append(conseq)
    return pruned_h
def generateRules_lift(freq_sets, support_data):
    rules = []
    for i in range (1, len(freq_sets)):
        for freqSet in freq_sets[i]:
            h1 = [frozenset([item]) for item in freqSet]
            if (i> 1):
                rules_from_conseq_lift(freqSet, h1, support_data, rules)
            else:
                calc_lift(freqSet, h1, support_data, rules)
    return rules
def rules_from_conseq(freqSet, h1, support_data, rules, min_confidence):
    m = len(h1[0])
    if (len(freqSet) > (m+1)):
        hmp1 = joint_set(h1, m+1)
        hmp1 = calc_confidence(freqSet, hmp1, support_data, rules, min_confidence)
        if len(hmp1) > 1:
            rules_from_conseq(freqSet, hmp1, support_data, rules, min_confidence)
def calc_lift(freqSet, h1, support_data, rules):
    pruned_h = []
    for conseq in h1:
        lift = support_data[freqSet]/ (support_data[freqSet-conseq] * support_data[freqSet])
        if lift > 1:
            rules.append((freqSet-conseq, conseq, lift))
            pruned_h.append(conseq)
    return pruned_h
def rules_from_conseq_lift(freqSet, h1, support_data, rules):
    m = len(h1[0])
    if (len(freqSet) > (m+1)):
        hmp1 = joint_set(h1, m+1)
        hmp1 = calc_lift(freqSet, hmp1, support_data, rules)
        if len(hmp1) > 1:
            rules_from_conseq_lift(freqSet, hmp1, support_data, rules)
   README Content:
_NOTE_: The data for the examples below are from data1.txt
The Aprori function takes a dataset and a minimum support.
This will give the frequent sets and the support_data along with the frequent sets.
freq_sets, support_data = apriori(dataset, 0.5)
Then you can generate the rules using GenerateRules to make rules based on confidence or use GenerateRules_lift to make rules based on lift.
Sample output for generateRules based on confidence.
[(frozenset({' White'}), frozenset({' United-States'}), 0.9307692307692308), (frozenset({' United-States'}), frozenset({' White'}), 0.8752260397830018), (frozenset({' White'}), frozenset({' Male'}), 0.7009615384615385), (frozenset({' Male'}), frozenset({' Wh
ite'}), 0.8868613138686132), (frozenset({' Private'}), frozenset({' <=50K\n'}), 0.7857948139797069), (frozenset({' <=50K\n'}), frozenset({' Private'}), 0.7667766776677668), (frozenset({' Private'}), frozenset({' White'}), 0.8602029312288613), (frozenset({' White'}), frozenset({' Private'}), 0.7336538461538461), (frozenset({' <=50K\n'}), frozenset({' United-States'}), 0.9086908690869087), (frozenset({' United-States'}), frozenset({' <=50K\n'}), 0.7468354430379747), (frozenset({' <=50K\n'}), frozenset({' White'}), 0.8426842684268426), (frozenset({' White'}), frozenset({' <=50K\n'}), 0.7365384615384615), (frozenset({' Private'}), frozenset({' United-States'}), 0.9098083427282976), (frozenset({' United-States'}), frozenset({' Private'}), 0.7296564195298373), (frozenset({' Male'}), frozenset({' United-States'}), 0.9172749391727494), (frozenset({' <=50K\n'}), frozenset({' White', ' United-States'}), 0.7766776677667766), (frozenset({' Private'}), frozenset({' United-States', ' <=50K\n'}), 0.7080045095828635), (frozenset({' Private'}), frozenset({' White', ' United-States'}), 0.7959413754227733), (frozenset({' Male'}), frozenset({' White', ' United-States'}), 0.8284671532846716)]
The frozen sets is the key and items and the number is the confidence calculated.
For generateRules_lift sample output will be:
[(frozenset({' White'}), frozenset({' United-States'}), 1.1625), (frozenset({' United-States'}), frozenset({' White'}), 1.093128390596745), (frozenset({' White'}), frozenset({' Male'}), 1.1625), (frozenset({' Male'}), frozenset({' White'}), 1.4708029197080292), (frozenset({' Private'}), frozenset({' <=50K\n'}), 1.363021420518602), (frozenset({' <=50K\n'}), frozenset({' Private'}), 1.33003300330033), (frozenset({' Private'}), frozenset({' White'}), 1.363021420518602), (frozenset({' White'}), frozenset({' Private'}), 1.1624999999999999), (frozenset({' <=50K\n'}), frozenset({' United-States'}), 1.33003300330033)
The frozen set are the items and the number after is the lift. It will give rules where the lift is greater than 1.
find_freq() Takes a set dataset, the number of transactions, candidates list of 1 and the minimum_support threshold.
joint_set() will take the candidate sets of 1 and 2, which will join and append all the combination of data sets.
reference: Machine Learning in Action by Peter Harrington. Chapter 11
