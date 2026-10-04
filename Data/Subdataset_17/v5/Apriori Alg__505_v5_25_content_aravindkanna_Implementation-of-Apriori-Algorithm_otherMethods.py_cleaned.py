import itertools
from sets import Set
def generate(current_size_list):
    next_size_list = []
    size = len(current_size_list)
    for i in range(size):
        for j in range(i + 1, size):
            if current_size_list[i][:-1] == current_size_list[j][:-1]:
                candidate = current_size_list[i][:]
                candidate.append(current_size_list[j][-1])
                next_size_list.append(candidate)
            else:
                break
    return next_size_list
def one_less_subsets(itemset):
    return [itemset[:i] + itemset[i + 1:] for i in range(len(itemset))]
def prune(freqs_trie, curr_list):
    pruned_list = []
    for itemset in curr_list:
        subsets = one_less_subsets(itemset)
        if all(freqs_trie.hasNode(subset) for subset in subsets):
            pruned_list.append(itemset)
    return pruned_list
def item_sets_count(in_file, curr_list):
    counts = [0] * len(curr_list)
    with open(in_file) as infp:
        for line in infp:
            transaction = Set(line.strip().split(","))
            for idx, candidate in enumerate(curr_list):
                if transaction.issuperset(Set(candidate)):
                    counts[idx] += 1
    return counts
def print_associate_rules(freqs_trie, min_confidence):
    count = 0
    for itemset in freqs_trie.getItemSets([]):
        for j in range(1, len(itemset)):
            for subset in itertools.combinations(itemset, j):
                confidence = float(freqs_trie.getCount(itemset)) / float(freqs_trie.getCount(subset))
                if confidence >= min_confidence:
                    print(",".join(subset) + " => " + ",".join(set(itemset) - set(subset)))
                    count += 1
    return count
