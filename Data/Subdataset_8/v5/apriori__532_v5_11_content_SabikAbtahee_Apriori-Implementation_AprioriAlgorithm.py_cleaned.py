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
def count_itemsets(items, transactions):
    counts = {}
    for i in range(1, len(items) + 1):
        com = generate_combinations(items, i)
        for c in com:
            for transaction in transactions:
                transaction_items = transaction.split()
                all_items_present = True
                for item in c:
                    if not is_item_present(item, transaction_items):
                        all_items_present = False
                        break
                if all_items_present:
                    key = ','.join(c)
                    counts[key] = counts.get(key, 0) + 1
    return counts
def filter_itemset_counts(counts_all, minimum_support):
    filtered_counts = {}
    for key, value in counts_all.items():
        if value >= minimum_support:
            filtered_counts[key] = value
    return filtered_counts
def generate_association_rules(itemset_counts):
    highest_length = max(len(itemset) for itemset in itemset_counts)
    while highest_length > 1:
        for key, value in itemset_counts.items():
            if len(key) == highest_length:
                subsets = [key[i:i + highest_length - 2] for i in range(len(key) - highest_length + 3)]
                for subset in subsets:
                    confidence = value / itemset_counts.get(subset, 1)
                    print(f"{subset} => {key} : {confidence}")
        highest_length -= 1
def process_transactions():
    content = sys.stdin.readlines()
    transaction_count = int(content[0])
    minimum_support = int(content[-1])
    transactions = [content[i].strip() for i in range(1, transaction_count + 1)]
    items = sorted(set(item for transaction in transactions for item in transaction.split()))
    itemset_counts = count_itemsets(items, transactions)
    filtered_counts = filter_itemset_counts(itemset_counts, minimum_support)
    generate_association_rules(filtered_counts)
def main():
    redirect_io_to_files()
    process_transactions()
if __name__ == "__main__":
    main()