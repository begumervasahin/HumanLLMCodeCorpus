import itertools
def generate(currentSizeList):
    size = len(currentSizeList)
    nextSizeList = []
    i = 0
    while i < size:
        j = i + 1
        while j < size:
            if currentSizeList[i][:-1] == currentSizeList[j][:-1]:
                a = currentSizeList[i][:]
                a.append(currentSizeList[j][-1])
                nextSizeList.append(a)
                j += 1
            else:
                break
        i += 1
    return nextSizeList
def oneLessSubsets(itemset):
    allSubsets = []
    size = len(itemset)
    for i in range(size):
        s = itemset[:i] + itemset[i+1:]
        allSubsets.append(s)
    return allSubsets
def prune(FreqsTrie, currList):
    prunedList = []
    for i in currList:
        allSubsets = oneLessSubsets(i)
        flag = True
        for j in allSubsets:
            if not FreqsTrie.hasNode(j):
                flag = False
                break
        if flag:
            prunedList.append(i)
    return prunedList
def itemSetsCount(inFile, currList):
    counts = [0] * len(currList)
    with open(inFile, 'r') as infp:
        for line in infp:
            line = line.strip()
            itemList = line.split(",")
            currTransaction = set(itemList)
            currSize = len(currTransaction)
            for i, itemset in enumerate(currList):
                if currSize < len(itemset):
                    continue
                if currTransaction.issuperset(set(itemset)):
                    counts[i] += 1
    return counts
def printAssociateRules(FreqsTrie, mincon):
    count = 0
    for i in FreqsTrie.getItemSets([]):
        for j in range(1, len(i)):
            for k in itertools.combinations(i, j):
                if float(FreqsTrie.getCount(i)) / float(FreqsTrie.getCount(k)) >= mincon:
                    print(",".join(k) + " => " + ",".join(set(i) - set(k)))
                    count += 1
    return count
class FreqsTrie:
    def __init__(self):
        self.trie = {}
    def hasNode(self, node):
        current = self.trie
        for item in node:
            if item in current:
                current = current[item]
            else:
                return False
        return True
    def getItemSets(self, prefix):
        return [['A', 'B', 'C'], ['A', 'C'], ['B', 'C']]
    def getCount(self, itemset):
        return 10
if __name__ == "__main__":
    freqs_trie = FreqsTrie()
    min_confidence = 0.5
    in_file = 'data.csv'
    current_size_list = [['A', 'B'], ['A', 'C'], ['B', 'C']]
    next_size_list = generate(current_size_list)
    print("Next size list:", next_size_list)
    pruned_list = prune(freqs_trie, current_size_list)
    print("Pruned list:", pruned_list)
    itemset_counts = itemSetsCount(in_file, current_size_list)
    print("Itemset counts:", itemset_counts)
    assoc_rule_count = printAssociateRules(freqs_trie, min_confidence)
    print("Number of association rules:", assoc_rule_count)