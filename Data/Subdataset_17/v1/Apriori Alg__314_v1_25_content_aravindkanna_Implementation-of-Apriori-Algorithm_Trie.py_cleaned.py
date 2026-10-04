class TrieNode:
    def __init__(self, count=1, name="root"):
        self.child = {}
        self.count = count
        self.name = name
    def insertNode(self, itemset, count):
        f = self.child
        for i in itemset:
            if i in f:
                f = f[i].child
            else:
                temp = TrieNode(count, i)
                f[i] = temp
                f = temp.child
    def hasNode(self, itemset):
        f = self.child
        for i in itemset:
            if i in f:
                f = f[i].child
            else:
                return False
        return True
    def insertAll(self, FreqItemSets, counts):
        size = len(FreqItemSets)
        for i in range(size):
            self.insertNode(FreqItemSets[i], counts[i])
    def printAll(self, prevStr=""):
        for i in self.child:
            a = prevStr + i
            print(a)
            self.child[i].printAll(a + ",")
    def getItemSets(self, prevList=[]):
        for i in self.child:
            a = prevList + [i]
            yield a
            for j in self.child[i].getItemSets(a):
                yield j
    def getCount(self, itemSet):
        f = self.child
        for i in itemSet:
            fp = f[i]
            f = f[i].child
        return fp.count
if __name__ == "__main__":
    trie = TrieNode()
    freqItemSets = [['A'], ['B'], ['A', 'B']]
    counts = [3, 2, 1]
    trie.insertAll(freqItemSets, counts)
    print("All nodes in the Trie:")
    trie.printAll()
    print("\nDoes ['A'] exist in the Trie?", trie.hasNode(['A']))
    print("Does ['C'] exist in the Trie?", trie.hasNode(['C']))
    print("\nAll item sets in the Trie:")
    for itemset in trie.getItemSets():
        print(itemset)
    print("\nCount of ['A'] in the Trie:", trie.getCount(['A']))
    print("Count of ['A', 'B'] in the Trie:", trie.getCount(['A', 'B']))