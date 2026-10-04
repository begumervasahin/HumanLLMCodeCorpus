
def load_data(file_path):
    with open(file_path, 'r') as file:
        dataset = file.read().splitlines()
    return dataset
def apriori_algorithm(dataset, min_support):
    C1 = {}
    C2 = {}
    C3 = {}
    L1 = []
    L2 = []
    L3 = []
    for transaction in dataset:
        items = transaction.split()
        for item in items:
            if item in C1:
                C1[item] += 1
            else:
                C1[item] = 1
    L1 = [item for item, count in C1.items() if count >= min_support]
    for i in range(len(L1)):
        for j in range(i + 1, len(L1)):
            C2[(L1[i], L1[j])] = 0
    for transaction in dataset:
        items = set(transaction.split())
        for itemset in C2:
            if set(itemset).issubset(items):
                C2[itemset] += 1
    L2 = [itemset for itemset, count in C2.items() if count >= min_support]
    for (a, b) in L2:
        for c in L1:
            if c != a and c != b:
                C3[(a, b, c)] = 0
    for transaction in dataset:
        items = set(transaction.split())
        for itemset in C3:
            if set(itemset).issubset(items):
                C3[itemset] += 1
    L3 = [itemset for itemset, count in C3.items() if count >= min_support]
    return L1, L2, L3
def main():
    file_path = 'browsingdata.txt'
    dataset = load_data(file_path)
    min_support = 3
    L1, L2, L3 = apriori_algorithm(dataset, min_support)
    print("Frequent itemsets of size 1:")
    for itemset in L1:
        print(itemset)
    print("\nFrequent itemsets of size 2:")
    for itemset in L2:
        print(itemset)
    print("\nFrequent itemsets of size 3:")
    for itemset in L3:
        print(itemset)
if __name__ == "__main__":
    main()