import sys
from Node import Node
class MinQueue(object):
    def __init__(self, n):
        self.list = n[:]
    def __len__(self):
        return len(self.list)
    def contains(self, x):
        if x in self.list:
            return True
        return False
    def extractMin(self):
        min_val = sys.maxint
        min_node = None
        for node in self.list:
            if node.key < min_val:
                min_val = node.key
                min_node = node
        self.list.remove(min_node)
        return min_node.idx
