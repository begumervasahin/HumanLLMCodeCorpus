import sys
def load_database(file_path):
    with open(file_path, "r") as file:
        return [[int(x) for x in line.split()] for line in file]
def clear_infrequent_items(table, min_support):
    to_delete = [k for k in table.keys() if table[k] < min_support]
    for key in to_delete:
        del table[key]
def can_combine(item1, item2):
    return item1[:-1] == item2[:-1] and item1[-1] < item2[-1]
def generate_candidates(table):
    candidates = {}
    keys = list(table.keys())
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            if can_combine(keys[i], keys[j]):
                candidate = keys[i] + (keys[j][-1],)
                candidates[candidate] = 0
    return candidates
def count_support(table, transactions):
    for transaction in transactions:
        transaction_set = set(transaction)
        for candidate in table.keys():
            if set(candidate).issubset(transaction_set):
                table[candidate] += 1
    return table
def powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]] + item
            yield item
def print_rule(antecedent, consequent, confidence):
    print(f"{antecedent} ==> {consequent} (confidence: {confidence:.2f})")
def generate_rules(item, support_data, min_confidence):
    item_support = support_data[item]
    for antecedent in powerset(list(item)):
        if antecedent and antecedent != list(item):
            consequent = [x for x in item if x not in antecedent]
            antecedent = tuple(antecedent)
            if antecedent in support_data:
                confidence = item_support / support_data[antecedent]
                if confidence >= min_confidence:
                    print_rule(antecedent, consequent, confidence)
def apriori(transactions, min_support, min_confidence):
    min_support_count = min_support * len(transactions)
    current_table = {}
    for transaction in transactions:
        for item in transaction:
            item_tuple = (item,)
            if item_tuple not in current_table:
                current_table[item_tuple] = 1
            else:
                current_table[item_tuple] += 1
    clear_infrequent_items(current_table, min_support_count)
    all_frequent_itemsets = [current_table]
    while current_table:
        current_table = generate_candidates(current_table)
        current_table = count_support(current_table, transactions)
        clear_infrequent_items(current_table, min_support_count)
        if current_table:
            all_frequent_itemsets.append(current_table)
    support_data = {}
    for table in all_frequent_itemsets:
        support_data.update(table)
    total_rules = 0
    for itemset in support_data.keys():
        if len(itemset) > 1:
            generate_rules(itemset, support_data, min_confidence)
            total_rules += 1
    print(f"Mined file {sys.argv[5]} and found a total of {total_rules} association rules")
if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python main.py --min_support <min_support> --min_confidence <min_confidence> <input_file>")
        sys.exit(1)
    min_support = float(sys.argv[2])
    min_confidence = float(sys.argv[4])
    input_file = sys.argv[5]
    transactions = load_database(input_file)
    apriori(transactions, min_support, min_confidence)