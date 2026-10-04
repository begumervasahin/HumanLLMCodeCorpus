import itertools
from sets import Set
def fonk1(current_size_list):
    b1 = []
    b2 = len(current_size_list)
    for i in range(b2):
        for j in range(i + 1, b2):
            if current_size_list[i][:-1] == current_size_list[j][:-1]:
                b3 = current_size_list[i][:]
                b3.append(current_size_list[j][-1])
                b1.append(b3)
            else:
                break
    return b1
def fonk2(itemset):
    return [itemset[:i] + itemset[i + 1:] for i in range(len(itemset))]
def fonk3(freqs_trie, curr_list):
    b4 = []
    for itemset in curr_list:
        b5 = fonk2(itemset)
        if all(freqs_trie.hasNode(subset) for subset in b5):
            b4.append(itemset)
    return b4
def fonk4(in_file, curr_list):
    b6 = [0] * len(curr_list)
    with open(in_file) as infp:
        for line in infp:
            b7 = Set(line.strip().split(","))
            for idx, b3 in enumerate(curr_list):
                if b7.issuperset(Set(b3)):
                    b6[idx] += 1
    return b6
def fonk5(freqs_trie, min_confidence):
    a1 = 0
    for itemset in freqs_trie.getItemSets([]):
        for j in range(1, len(itemset)):
            for subset in itertools.combinations(itemset, j):
                b8 = float(freqs_trie.getCount(itemset)) / float(freqs_trie.getCount(subset))
                if b8 >= min_confidence:
                    print(",".join(subset) + " => " + ",".join(set(itemset) - set(subset)))
                    a1 += 1
    return a1
