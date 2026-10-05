import sys
def redirect_io_to_files(input_file='apriori.txt', output_file='output.txt'):
    sys.stdin = open(input_file, 'r')
    sys.stdout = open(output_file, 'w')
def generate_combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)
def is_item_present(item, transaction):
    return item in transaction
def calculate_item_counts(items, transactions):
    counts = {}
    for i in range(1, len(items) + 1):
        com = generate_combinations(items, i)
        for c in com:
            for j in range(0, len(transactions), 1):
                x = transactions[j].split()
                for i in c:
                    ans = is_item_present(i, x)
                    if not ans:
                        break
                if ans:
                    key = ','.join(c)
                    counts[key] = counts.get(key, 0) + 1
    return counts
def print_counts(counts_dictionary):
    for itemset, count in counts_dictionary.items():
        print(itemset, count)
        print(" ")
def generate_association_rules(item_counts):
    highest_length = max(len(itemset) for itemset in item_counts)
    while highest_length != 2:
        for itemset, count in item_counts.items():
            if len(itemset) == highest_length:
                subsets = [itemset[i:i + highest_length - 2] for i in range(len(itemset) - highest_length + 3)]
                for subset in subsets:
                    confidence = count / item_counts.get(subset, 1)
                    print(subset, "=>", itemset, confidence * 100, "% Chance")
                    print("")
        highest_length -= 2
def process_transactions():
    content = sys.stdin.readlines()
    transaction_count = int(content[0])
    minimum_support = int(content[-1])
    transactions = [content[i].strip() for i in range(1, transaction_count + 1)]
    items = sorted(set(item for transaction in transactions for item in transaction.split()))
    item_counts = calculate_item_counts(items, transactions)
    filtered_counts = {k: v for k, v in item_counts.items() if v >= minimum_support}
    generate_association_rules(filtered_counts)
def main():
    redirect_io_to_files()
    process_transactions()
if __name__ == "__main__":
    main()