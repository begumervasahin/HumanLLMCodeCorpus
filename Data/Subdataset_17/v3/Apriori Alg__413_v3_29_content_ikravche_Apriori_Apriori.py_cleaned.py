import itertools as it
MIN_SUPPORT = 3
MIN_CONFIDENCE = 0.7
combination_size = 1
support_counts = {}
transaction_list = [
    ['a', 'b'],
    ['a', 'c', 'd', 'e'],
    ['a', 'b', 'c', 'e'],
    ['c', 'd'],
    ['b', 'c', 'd', 'e'],
    ['a', 'd', 'e'],
    ['c', 'd', 'e']
]
product_set = set(item for sublist in transaction_list for item in sublist)
def has_sufficient_support():
    max_support = max((value for key, value in support_counts.items() if len(key) == combination_size - 1), default=0)
    return max_support >= MIN_SUPPORT or combination_size == 1
def generate_combinations():
    global combination_size
    if has_sufficient_support():
        combinations = list(it.combinations(product_set, combination_size))
        count_appearances(combinations)
    else:
        print_results()
def count_appearances(combinations):
    global combination_size
    for combination in combinations:
        for transaction in transaction_list:
            update_support_counts(combination, transaction)
    combination_size += 1
    generate_combinations()
def update_support_counts(combination, transaction):
    combination_str = ''.join(sorted(combination))
    transaction_str = ''.join(sorted(transaction))
    filtered_transaction = filter_transaction(combination_str, transaction_str)
    if combination_str in filtered_transaction:
        if combination_str in support_counts:
            support_counts[combination_str] += 1
        else:
            support_counts[combination_str] = 1
def filter_transaction(combination, transaction):
    return ''.join([char for char in transaction if char in combination])
def print_results():
    print("Frequent Itemsets:")
    for combination, support in support_counts.items():
        if support >= MIN_SUPPORT:
            print(f'Combination: {combination}, Support: {support}')
if __name__ == "__main__":
    generate_combinations()