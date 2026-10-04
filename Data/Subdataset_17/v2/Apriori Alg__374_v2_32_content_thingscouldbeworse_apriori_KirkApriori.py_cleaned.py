import time
from itertools import combinations
start_time = time.time()
def read_file(filename):
    transactions = []
    with open(filename, 'r') as f:
        for line in f:
            transactions.append(line.strip())
    return transactions
def generate_single_candidates(dataset):
    single_items = set()
    for transaction in dataset:
        items = transaction.split(',')
        single_items.update(items)
    return list(single_items)
def count_candidates(dataset, candidates):
    candidate_count = {candidate: 0 for candidate in candidates}
    for transaction in dataset:
        items = transaction.split(',')
        for item in items:
            if item in candidate_count:
                candidate_count[item] += 1
    return candidate_count
def calculate_total_items(dataset):
    return sum(len(transaction.split(',')) for transaction in dataset)
def filter_candidates_by_support(total_items, candidate_count, support):
    return {candidate: count / total_items for candidate, count in candidate_count.items() if count / total_items >= support}
def get_frequent_candidates(total_items, candidate_count, support):
    return [candidate for candidate, count in candidate_count.items() if count / total_items >= support]
def generate_frequent_pairs(frequent_items, dataset, total_items, support):
    pair_count = defaultdict(int)
    for transaction in dataset:
        items = transaction.split(',')
        for pair in combinations(items, 2):
            if set(pair).issubset(set(frequent_items)):
                pair_count[pair] += 1
    return {pair: count / total_items for pair, count in pair_count.items() if count / total_items >= support}
if __name__ == "__main__":
    data_file = 'mushroom.data'
    support_threshold = 0.03
    data = read_file(data_file)
    single_candidates = generate_single_candidates(data)
    print("Single item candidates:", single_candidates)
    candidate_counts = count_candidates(data, single_candidates)
    print("Counts of single item candidates:", candidate_counts)
    total_item_count = calculate_total_items(data)
    print("Total number of items:", total_item_count)
    frequent_candidates = filter_candidates_by_support(total_item_count, candidate_counts, support_threshold)
    print("Frequent single item candidates:", frequent_candidates)
    frequent_candidate_counts = get_frequent_candidates(total_item_count, candidate_counts, support_threshold)
    print("Frequent single item candidates (counts):", frequent_candidate_counts)
    frequent_pairs = generate_frequent_pairs(frequent_candidate_counts, data, total_item_count, support_threshold)
    print("Frequent pairs:")
    for pair, support in frequent_pairs.items():
        print(f"{pair}: {support}")
    print("Time taken:", time.time() - start_time)