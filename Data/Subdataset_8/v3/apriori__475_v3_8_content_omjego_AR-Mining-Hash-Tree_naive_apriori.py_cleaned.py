import itertools
import csv
class Parameters:
    SUPPORT = 30
    CONFIDENCE = 70
def load_data(filename, max_attr=100):
    with open(filename, 'r') as f:
        data = list(csv.reader(f, delimiter=','))
    transactions = []
    for row in data:
        attributes = [val.strip() for val in row[1:] if int(val.strip()) <= max_attr]
        if attributes:
            transactions.append(attributes)
    return transactions
def find_subsets(S, m):
    return set(itertools.combinations(S, m))
def has_infrequent_subset(dataset, prev_l, k):
    subsets = find_subsets(dataset, k)
    for item in subsets:
        s = sorted(item)
        if s not in prev_l:
            return True
    return False
def apriori(prev_l, k):
    result = []
    length = k
    for list1 in prev_l:
        for list2 in prev_l:
            count = 0
            c = []
            if list1 != list2:
                while count < length - 1:
                    if list1[count] != list2[count]:
                        break
                    count += 1
                else:
                    if list1[length - 1] < list2[length - 1]:
                        c.extend(list1)
                        c.append(list2[length - 1])
                        if not has_infrequent_subset(c, prev_l, k):
                            result.append(c)
    return result
def apply_support(data, singles, support):
    k = 2
    prev_l = singles
    L = []
    while prev_l:
        current = []
        for c in apriori(prev_l, k - 1):
            cnt = sum(1 for T in data if set(c).issubset(set(T)))
            if (100 * cnt / len(data)) >= support:
                c.sort()
                current.append(c)
        prev_l = current
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
            for count in range(1, len(itemset)):
                subsets = find_subsets(itemset, count)
                for item in subsets:
                    inc1 = sum(1 for T in data if set(item).issubset(set(T)))
                    inc2 = sum(1 for T in data if set(itemset).issubset(set(T)))
                    if 100 * inc2 / inc1 >= confidence:
                        s = ','.join(item)
                        m = ','.join(set(itemset) - set(item))
                        print(f"{s} ==> {m}")
                        result += 1
    print('Total rules generated:', result)
    return result
def main():
    data = load_data('1000-out1.csv')
    find_association_rules(data, Parameters.SUPPORT, Parameters.CONFIDENCE)
if __name__ == "__main__":
    main()