from collections import Counter
import argparse
import itertools
import sys
def apriori(source_file, minsup):
    with open(source_file) as file:
        transactions = [line.strip().split() for line in file.readlines()]
    minsup = float(minsup)
    num_transactions = len(transactions)
    initial_candidates = list(itertools.chain.from_iterable(transactions))
    item_counts = Counter(initial_candidates)
    frequent_items = sorted([item for item, count in item_counts.items() if count / num_transactions >= minsup])
    candidates = gen_candidate(transactions)
def gen_candidate(transactions):
    candidates = []
    transactions = sorted(ensure_list_of_lists(transactions))
    prefixes = sorted([list(x) for x in set(frozenset(item[:-1]) for item in transactions)])
    for prefix in prefixes:
        postfixes = [item[-1:] for item in transactions if item[:-1] == prefix]
        postfixes = list(itertools.chain.from_iterable(postfixes))
        combinations = list(itertools.combinations(postfixes, 2))
        for combination in combinations:
            candidates.append(prefix + list(combination))
    return candidates
def restricted_float(value):
    value = float(value)
    if value < 0.0 or value > 1.0:
        raise argparse.ArgumentTypeError(f"{value} not in range [0.0, 1.0]")
    return value
def ensure_list_of_lists(data):
    if not isinstance(data[0], list):
        return [[item] for item in data]
    else:
        return data
def main(argv):
    parser = argparse.ArgumentParser(description='Apriori algorithm implementation')
    parser.add_argument("source", help="Source transaction file location")
    parser.add_argument("minsup", help="Minimum support (0.0 - 1.0)", type=restricted_float)
    args = parser.parse_args()
    apriori(args.source, args.minsup)
if __name__ == "__main__":
    main(sys.argv[1:])