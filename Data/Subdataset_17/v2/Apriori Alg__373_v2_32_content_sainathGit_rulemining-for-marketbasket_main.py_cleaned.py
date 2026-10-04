import sys
def load_transactions(input_file):
    transactions = []
    with open(input_file, "r") as file:
        for line in file:
            transactions.append([int(x) for x in line.split()])
    return transactions
def adjust_support(min_support, total_transactions):
    return min_support * total_transactions
def clear(table, min_support):
    infrequent_keys = [k for k in table.keys() if table[k] < min_support]
    for key in infrequent_keys:
        del table[key]
def get_key(l1, l2):
    key = list(l1[:-1])
    key.extend([l1[-1], l2[-1]])
    return tuple(key)
def can_mix(l1, l2):
    return l1[:-1] == l2[:-1] and l1[-1] < l2[-1]
def apriori_gen(table):
    new_table = {}
    for l1 in table.keys():
        for l2 in table.keys():
            if can_mix(l1, l2):
                new_table[get_key(l1, l2)] = 0
    return new_table
def count_values(table, db):
    for k in table.keys():
        for transaction in db:
            if set(k).issubset(transaction):
                table[k] += 1
def powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]] + item
            yield item
def print_rule(s, l_s, conf):
    print(f"{s} ==> {l_s}              {conf:.2f}")
def print_confs(item, L):
    global rule_count
    for s in powerset(list(item)):
        if not s or s == list(item):
            continue
        l_s = [x for x in item if x not in s]
        conf = L[item] / L[tuple(s)]
        if conf >= min_confidence:
            print_rule(s, l_s, conf)
            rule_count += 1
if __name__ == "__main__":
    min_support = float(sys.argv[1])
    min_confidence = float(sys.argv[2])
    input_file = sys.argv[3]
    transaction_list = load_transactions(input_file)
    min_support = adjust_support(min_support, len(transaction_list))
    l = []
    table = {}
    for transaction in transaction_list:
        for item in transaction:
            if (item,) not in table.keys():
                table[(item,)] = 1
            else:
                table[(item,)] += 1
    clear(table, min_support)
    l.append(table)
    k = 1
    while len(l[k-1]) != 0:
        table = apriori_gen(l[k-1])
        count_values(table, transaction_list)
        clear(table, min_support)
        l.append(table)
        k += 1
    l.pop()
    L = {}
    for level in l:
        L.update(level)
    rule_count = 0
    for item in L.keys():
        if len(item) > 1:
            print_confs(item, L)
    print(f"Mined file {input_file}")
    print(f"Found a total of {rule_count} association rules")