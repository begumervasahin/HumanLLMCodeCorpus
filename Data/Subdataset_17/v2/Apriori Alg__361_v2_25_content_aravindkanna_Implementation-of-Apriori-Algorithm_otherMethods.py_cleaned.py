import itertools
def generate_next_size_list(current_size_list):
    next_size_list = []
    size = len(current_size_list)
    for i in range(size):
        for j in range(i + 1, size):
            if current_size_list[i][:-1] == current_size_list[j][:-1]:
                new_itemset = current_size_list[i][:]
                new_itemset.append(current_size_list[j][-1])
                next_size_list.append(new_itemset)
            else:
                break
    return next_size_list
def generate_one_less_subsets(itemset):
    return [itemset[:i] + itemset[i+1:] for i in range(len(itemset))]
def prune_itemsets(freqs_trie, current_list):
    pruned_list = []
    for itemset in current_list:
        subsets = generate_one_less_subsets(itemset)
        if all(freqs_trie.has_node(subset) for subset in subsets):
            pruned_list.append(itemset)
    return pruned_list
def count_itemsets_in_transactions(file_path, current_list):
    counts = [0] * len(current_list)
    with open(file_path, 'r') as file:
        for line in file:
            transaction = set(line.strip().split(","))
            for idx, itemset in enumerate(current_list):
                if transaction.issuperset(itemset):
                    counts[idx] += 1
    return counts
def print_association_rules(freqs_trie, min_confidence):
    rule_count = 0
    for itemset in freqs_trie.get_itemsets([]):
        for length in range(1, len(itemset)):
            for subset in itertools.combinations(itemset, length):
                if freqs_trie.get_count(itemset) / freqs_trie.get_count(subset) >= min_confidence:
                    rule = f"{','.join(subset)} => {','.join(set(itemset) - set(subset))}"
                    print(rule)
                    rule_count += 1
    return rule_count
class FreqsTrie:
    def __init__(self):
        self.trie = {}
    def has_node(self, node):
        current = self.trie
        for item in node:
            if item in current:
                current = current[item]
            else:
                return False
        return True
    def get_itemsets(self, prefix):
        return [['A', 'B', 'C'], ['A', 'C'], ['B', 'C']]
    def get_count(self, itemset):
        return 10
if __name__ == "__main__":
    freqs_trie = FreqsTrie()
    min_confidence = 0.5
    in_file = 'data.csv'
    current_size_list = [['A', 'B'], ['A', 'C'], ['B', 'C']]
    next_size_list = generate_next_size_list(current_size_list)
    print("Next size list:", next_size_list)
    pruned_list = prune_itemsets(freqs_trie, current_size_list)
    print("Pruned list:", pruned_list)
    itemset_counts = count_itemsets_in_transactions(in_file, current_size_list)
    print("Itemset counts:", itemset_counts)
    assoc_rule_count = print_association_rules(freqs_trie, min_confidence)
    print("Number of association rules:", assoc_rule_count)