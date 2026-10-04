class TrieNode:
    def __init__(self, count=1, name="root"):
        self.child = {}
        self.count = count
        self.name = name
    def insert_node(self, itemset, count):
        current_node = self.child
        for item in itemset:
            if item not in current_node:
                current_node[item] = TrieNode(count, item)
            current_node = current_node[item].child
    def has_node(self, itemset):
        current_node = self.child
        for item in itemset:
            if item in current_node:
                current_node = current_node[item].child
            else:
                return False
        return True
    def insert_all(self, freq_itemsets, counts):
        for itemset, count in zip(freq_itemsets, counts):
            self.insert_node(itemset, count)
    def print_all(self, prefix=""):
        for item in self.child:
            current_str = f"{prefix}{item}"
            print(current_str)
            self.child[item].print_all(f"{current_str},")
    def get_itemsets(self, prefix=[]):
        for item in self.child:
            current_list = prefix + [item]
            yield current_list
            yield from self.child[item].get_itemsets(current_list)
    def get_count(self, itemset):
        current_node = self.child
        for item in itemset:
            current_node = current_node[item].child
        return current_node.count
if __name__ == "__main__":
    trie = TrieNode()
    freq_itemsets = [['A'], ['B'], ['A', 'B']]
    counts = [3, 2, 1]
    trie.insert_all(freq_itemsets, counts)
    print("All nodes in the Trie:")
    trie.print_all()
    print("\nDoes ['A'] exist in the Trie?", trie.has_node(['A']))
    print("Does ['C'] exist in the Trie?", trie.has_node(['C']))
    print("\nAll item sets in the Trie:")
    for itemset in trie.get_itemsets():
        print(itemset)
    print("\nCount of ['A'] in the Trie:", trie.get_count(['A']))
    print("Count of ['A', 'B'] in the Trie:", trie.get_count(['A', 'B']))