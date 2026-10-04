import itertools
from sets import Set
def fonk1(current_size_list):
    b1 = len(current_size_list)
    b2 = []
    a1 = 0
    while a1 < b1:
        b3 = a1 + 1
        while b3 < b1:
            if current_size_list[a1][:-1] == current_size_list[b3][:-1]:
                b4 = current_size_list[a1][:]
                b4.append(current_size_list[b3][-1])
                b2.append(b4)
                b3 += 1
            else:
                break
        a1 += 1
    return b2
def fonk2(itemset):
    return [itemset[:a1] + itemset[a1 + 1:] for a1 in range(len(itemset))]
def fonk3(freqs_trie, curr_list):
    b5 = []
    for itemset in curr_list:
        b6 = fonk2(itemset)
        if all(freqs_trie.hasNode(subset) for subset in b6):
            b5.append(itemset)
    return b5
def fonk4(in_file, curr_list):
    with open(in_file) as infp:
        b7 = [0] * len(curr_list)
        for line in infp:
            b8 = Set(line.strip().split(","))
            for idx, b4 in enumerate(curr_list):
                if b8.issuperset(Set(b4)):
                    b7[idx] += 1
    return b7
def fonk5(freqs_trie, min_confidence):
    a2 = 0
    for itemset in freqs_trie.getItemSets([]):
        for b3 in range(1, len(itemset)):
            for subset in itertools.combinations(itemset, b3):
                b9 = float(freqs_trie.getCount(itemset)) / float(freqs_trie.getCount(subset))
                if b9 >= min_confidence:
                    print(",".join(subset) + " => " + ",".join(set(itemset) - set(subset)))
                    a2 += 1
    return a2