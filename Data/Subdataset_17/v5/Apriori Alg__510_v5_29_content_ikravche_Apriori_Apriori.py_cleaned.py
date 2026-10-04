import itertools as it
MIN_SUPPORT = 3
MIN_CONFIDENCE = 0.7
combinations_counter = 1
frequent_itemsets = {}
transaction_list = [
    ['a', 'b'],
    ['a', 'c', 'd', 'e'],
    ['a', 'b', 'c', 'e'],
    ['c', 'd'],
    ['b', 'c', 'd', 'e'],
    ['a', 'd', 'e'],
    ['c', 'd', 'e']
]
products_set = set(item for sublist in transaction_list for item in sublist)
def check_last_max_support():
    max_value = 0
    for itemset, support in frequent_itemsets.items():
        if len(itemset) == combinations_counter - 1:
            if support > max_value:
                max_value = support
    return max_value >= MIN_SUPPORT or combinations_counter == 1
def generate_combinations():
    if check_last_max_support():
        combinations = list(it.combinations(products_set, combinations_counter))
        count_appearances(combinations)
    else:
        print_results()
def count_appearances(combinations):
    global combinations_counter
    for combination in combinations:
        for transaction in transaction_list:
            update_frequent_itemsets(combination, transaction)
    combinations_counter += 1
    generate_combinations()
def update_frequent_itemsets(combination, transaction):
    itemset_str = ''.join(sorted(combination))
    transaction_str = ''.join(sorted(transaction))
    filtered_transaction = filter_relevant_items(itemset_str, transaction_str)
    if itemset_str in filtered_transaction:
        if itemset_str in frequent_itemsets:
            frequent_itemsets[itemset_str] += 1
        else:
            frequent_itemsets[itemset_str] = 1
def filter_relevant_items(itemset, transaction):
    return ''.join([char for char in transaction if char in itemset])
def print_results():
    for itemset, support in frequent_itemsets.items():
        if support >= MIN_SUPPORT:
            print(f'Itemset: {itemset} Support: {support}')
if __name__ == "__main__":
    generate_combinations()