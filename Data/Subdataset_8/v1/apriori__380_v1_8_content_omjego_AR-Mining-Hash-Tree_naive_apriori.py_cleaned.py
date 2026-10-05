import itertools
import csv
class Parameters:
    SUPPORT = 30
    CONFIDENCE = 70
def load_data(filename, max_attr=100):
    with open(filename, 'r') as f:
        data = list(csv.reader(f, delimiter=','))
    result = []
    for i in range(len(data)):
        attrbs = []
        for val in data[i][1:]:
            val = val.strip()
            if int(val) <= max_attr:
                attrbs.append(val)
        if len(attrbs) > 0:
            result.append(attrbs)
    return result
def solve(data, support, confidence):
    transactions = len(data)
    hashmap = {}
    for row in data:
        for word in row:
            if word not in hashmap:
                hashmap[word] = 1
            else:
                hashmap[word] += 1
    level = []
    for key in hashmap:
        if (100 * hashmap[key] / transactions) >= support:
            level.append([key])
    return find_association_rules(data, level, support, confidence)
def find_subsets(S, m):
    return set(itertools.combinations(S, m))
def has_infrequent_subset(dataset, prev_l, k):
    subsets = find_subsets(dataset, k)
    for item in subsets:
        s = []
        for l in item:
            s.append(l)
        s.sort()
        if s not in prev_l:
            return True
    return False
def apriori(prev_l, k):
    length = k
    result = []
    for list1 in prev_l:
        for list2 in prev_l:
            count = 0
            c = []
            if list1 != list2:
                while count < length - 1:
                    if list1[count] != list2[count]:
                        break
                    else:
                        count += 1
                else:
                    if list1[length - 1] < list2[length - 1]:
                        for item in list1:
                            c.append(item)
                        c.append(list2[length - 1])
                        if not has_infrequent_subset(c, prev_l, k):
                            result.append(c)
    return result
def apply_support(data, singles, support):
    k = 2
    prev_l = []
    L = []
    for item in singles:
        prev_l.append(item)
    while prev_l:
        current = []
        sets = apriori(prev_l, k - 1)
        for c in sets:
            cnt = 0
            trans = len(data)
            s = set(c)
            for T in data:
                t = set(T)
                if s.issubset(t):
                    cnt += 1
            if (100 * cnt / trans) >= support:
                c.sort()
                current.append(c)
        prev_l = []
        for l in current:
            prev_l.append(l)
        k += 1
        if current:
            L.append(current)
    return L
def find_association_rules(data, singles, support, confidence):
    num = 1
    L = apply_support(data, singles, support)
    result = 0
    for itemsets in L:
        for itemset in itemsets:
            length = len(itemset)
            count = 1
            while count < length:
                subsets = find_subsets(itemset, count)
                count += 1
                for item in subsets:
                    inc1 = 0
                    inc2 = 0
                    s = []
                    m = []
                    for i in item:
                        s.append(i)
                    for T in data:
                        if set(s).issubset(set(T)):
                            inc1 += 1
                        if set(itemset).issubset(set(T)):
                            inc2 += 1
                    if 100 * inc2 / inc1 >= confidence:
                        for index in itemset:
                            if index not in s:
                                m.append(index)
                        left = ','.join(s)
                        right = ','.join(set(itemset) - set(s))
                        print(' ==> '.join([left, right]))
                        result += 1
                        num += 1
    print('Total rules generated:', result)
    return result
def main():
    data = load_data('1000-out1.csv')
    solve(data, Parameters.SUPPORT, Parameters.CONFIDENCE)
if __name__ == "__main__":
    main()