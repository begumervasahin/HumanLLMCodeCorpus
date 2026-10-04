
from itertools import combinations
def load_dataset(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()
def generate_C1(dataset):
    C1 = {}
    for line in dataset:
        items = line.split()
        for item in items:
            C1[item] = C1.get(item, 0) + 1
    return C1
def generate_L1(C1, min_support):
    return {item: count for item, count in C1.items() if count >= min_support}
def generate_C2(L1):
    C2 = {}
    items = list(L1.keys())
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            C2[(items[i], items[j])] = 0
    return C2
def count_support_C2(C2, dataset):
    for line in dataset:
        items = set(line.split())
        for pair in C2.keys():
            if set(pair).issubset(items):
                C2[pair] += 1
    return C2
def generate_L2(C2, min_support):
    return {pair: count for pair, count in C2.items() if count >= min_support}
def apriori(dataset, min_support):
    C1 = generate_C1(dataset)
    L1 = generate_L1(C1, min_support)
    print(f"Frequent 1-itemsets: {L1}")
    C2 = generate_C2(L1)
    C2 = count_support_C2(C2, dataset)
    L2 = generate_L2(C2, min_support)
    print(f"Frequent 2-itemsets: {L2}")
if __name__ == "__main__":
    dataset = load_dataset('browsingdata.txt')
    practice_data = dataset[:12]
    min_support = 4
    apriori(practice_data, min_support)