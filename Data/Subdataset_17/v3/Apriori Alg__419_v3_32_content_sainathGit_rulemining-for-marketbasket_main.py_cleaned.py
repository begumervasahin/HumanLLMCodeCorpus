import sys
def load_transactions(input_file):
    transactions = []
    with open(input_file, "r") as file:
        for line in file:
            transactions.append([int(x) for x in line.split()])
    return transactions
def adjust_support(min_support, total_transactions):
    return min_support * total_transactions
def remove_infrequent_itemsets(itemset_counts, min_support):
    infrequent_keys = [k for k in itemset_counts.keys() if itemset_counts[k] < min_support]
    for key in infrequent_keys:
        del itemset_counts[key]
def get_combined_key(itemset1, itemset2):
    key = list(itemset1[:-1])
    key.extend([itemset1[-1], itemset2[-1]])
    return tuple(key)
def can_combine(itemset1, itemset2):
    return itemset1[:-1] == itemset2[:-1] and itemset1[-1] < itemset2[-1]
def generate_candidates(current_itemsets):
    new_itemsets = {}
    for itemset1 in current_itemsets.keys():
        for itemset2 in current_itemsets.keys():
            if can_combine(itemset1, itemset2):
                new_itemsets[get_combined_key(itemset1, itemset2)] = 0
    return new_itemsets
def count_support(itemsets, transactions):
    for itemset in itemsets.keys():
        for transaction in transactions:
            if set(itemset).issubset(transaction):
                itemsets[itemset] += 1
def generate_powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in generate_powerset(seq[1:]):
            yield [seq[0]] + item
            yield item
def print_association_rule(antecedent, consequent, confidence):
    print(f"{antecedent} ==> {consequent}    Confidence: {confidence:.2f}")
def generate_and_print_rules(itemset, itemset_supports):
    global rule_count
    for subset in generate_powerset(list(itemset)):
        if not subset or subset == list(itemset):
            continue
        remaining = [x for x in itemset if x not in subset]
        confidence = itemset_supports[itemset] / itemset_supports[tuple(subset)]
        if confidence >= MIN_CONFIDENCE:
            print_association_rule(subset, remaining, confidence)
            rule_count += 1
if __name__ == "__main__":
    MIN_SUPPORT = float(sys.argv[1])
    MIN_CONFIDENCE = float(sys.argv[2])
    INPUT_FILE = sys.argv[3]
    transactions = load_transactions(INPUT_FILE)
    MIN_SUPPORT = adjust_support(MIN_SUPPORT, len(transactions))
    itemset_supports = {}
    for transaction in transactions:
        for item in transaction:
            if (item,) not in itemset_supports:
                itemset_supports[(item,)] = 1
            else:
                itemset_supports[(item,)] += 1
    remove_infrequent_itemsets(itemset_supports, MIN_SUPPORT)
    itemsets_by_size = [itemset_supports]
    k = 1
    while len(itemsets_by_size[k-1]) != 0:
        itemset_supports = generate_candidates(itemsets_by_size[k-1])
        count_support(itemset_supports, transactions)
        remove_infrequent_itemsets(itemset_supports, MIN_SUPPORT)
        itemsets_by_size.append(itemset_supports)
        k += 1
    itemsets_by_size.pop()
    all_itemsets = {}
    for level in itemsets_by_size:
        all_itemsets.update(level)
    rule_count = 0
    for itemset in all_itemsets.keys():
        if len(itemset) > 1:
            generate_and_print_rules(itemset, all_itemsets)
    print(f"Mined file {INPUT_FILE}")
    print(f"Found a total of {rule_count} association rules")