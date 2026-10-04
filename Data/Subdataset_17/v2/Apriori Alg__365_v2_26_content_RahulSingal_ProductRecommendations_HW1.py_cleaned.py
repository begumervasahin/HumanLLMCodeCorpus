
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
    for line in dataset:
        items = line.split()
        for item in items:
            if item in C1:
                C1[item] += 1
            else:
                C1[item] = 1
    L1 = [key for key, count in C1.items() if count >= min_support]
    for i in range(len(L1)):
        for j in range(i + 1, len(L1)):
            C2[(L1[i], L1[j])] = 0
    for line in dataset:
        items = set(line.split())
        for key in C2:
            if set(key).issubset(items):
                C2[key] += 1
    L2 = [key for key, count in C2.items() if count >= min_support]
    for (a, b) in L2:
        for c in L1:
            if c != a and c != b:
                C3[(a, b, c)] = 0
    for line in dataset:
        items = set(line.split())
        for key in C3:
            if set(key).issubset(items):
                C3[key] += 1
    L3 = [key for key, count in C3.items() if count >= min_support]
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