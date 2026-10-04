from itertools import combinations
def read_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]
def generate_single_candidates(dataset):
    candidates = set()
    for transaction in dataset:
        items = transaction.split(',')
        candidates.update(items)
    return list(candidates)
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
def filter_candidates_by_support(candidate_count, total_items, support_threshold):
    return {candidate: count / total_items for candidate, count in candidate_count.items() if count / total_items >= support_threshold}
def generate_frequent_pairs(frequent_items, dataset, support_threshold):
    pair_count = {}
    for transaction in dataset:
        items = transaction.split(',')
        for pair in combinations(items, 2):
            pair = tuple(sorted(pair))
            if pair in pair_count:
                pair_count[pair] += 1
            else:
                pair_count[pair] = 1
    total_transactions = len(dataset)
    return {pair: count / total_transactions for pair, count in pair_count.items() if count / total_transactions >= support_threshold}
def main():
    data_file = 'mushroom.data'
    support_threshold = 0.03
    dataset = read_file(data_file)
    single_candidates = generate_single_candidates(dataset)
    print("Single Candidates:", single_candidates)
    candidate_count = count_candidates(dataset, single_candidates)
    print("Candidate Counts:", candidate_count)
    total_items = calculate_total_items(dataset)
    print("Total Items:", total_items)
    frequent_candidates = filter_candidates_by_support(candidate_count, total_items, support_threshold)
    print("Frequent Candidates:", frequent_candidates)
    frequent_pairs = generate_frequent_pairs(single_candidates, dataset, support_threshold)
    print("Frequent Pairs:")
    for pair, support in frequent_pairs.items():
        print(f"{pair}: {support:.2f}")
if __name__ == "__main__":
    main()