from itertools import combinations
import sys
def file_input_output():
    sys.stdin = open('apriori.txt', 'r')
    sys.stdout = open('output.txt', 'w')
def is_item_in_transaction(item, transaction):
    return item in transaction
def calculate_itemset_counts(items, transactions):
    counts = {}
    for i in range(1, len(items) + 1):
        item_combinations = combinations(items, i)
        for combination in item_combinations:
            for transaction in transactions:
                transaction_items = transaction.split()
                all_items_present = True
                for item in combination:
                    if not is_item_in_transaction(item, transaction_items):
                        all_items_present = False
                        break
                if all_items_present:
                    key = ','.join(combination)
                    counts[key] = counts.get(key, 0) + 1
    return counts
def filter_itemset_counts(itemset_counts, minimum_support):
    filtered_counts = {}
    for key, value in itemset_counts.items():
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
def run_apriori():
    content = sys.stdin.readlines()
    transaction_count = int(content[0])
    minimum_support = int(content[-1])
    transactions = [content[i].split() for i in range(1, transaction_count + 1)]
    items = sorted(set(item for transaction in transactions for item in transaction))
    itemset_counts = calculate_itemset_counts(items, transactions)
    filtered_counts = filter_itemset_counts(itemset_counts, minimum_support)
    generate_association_rules(filtered_counts)
def main():
    file_input_output()
    run_apriori()
if __name__ == "__main__":
    main()