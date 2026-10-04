from queue import Queue
class TrieNode:
    def __init__(self, count=1, name="root"):
        self.child = {}
        self.count = count
        self.name = name
    def insert_node(self, itemset, count):
        current_node = self.child
        for item in itemset:
            if item in current_node:
                current_node = current_node[item].child
            else:
                new_node = TrieNode(count, item)
                current_node[item] = new_node
                current_node = new_node.child
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
        for item, node in self.child.items():
            current_str = prefix + item
            print(current_str)
            node.print_all(current_str + ",")
    def get_itemsets(self, prefix=None):
        if prefix is None:
            prefix = []
        for item, node in self.child.items():
            current_list = prefix + [item]
            yield current_list
            yield from node.get_itemsets(current_list)
    def get_count(self, itemset):
        current_node = self.child
        for item in itemset:
            current_node = current_node[item]
        return current_node.count
