import sys
from Node import Node
class MinQueue(object):
    def __init__(self, nodes):
        self.nodes = nodes[:]
    def __len__(self):
        return len(self.nodes)
    def contains(self, key):
        return any(node.key == key for node in self.nodes)
    def extractMin(self):
        min_key = sys.maxint
        min_node = None
        for node in self.nodes:
            if node.key < min_key:
                min_key = node.key
                min_node = node
        self.nodes.remove(min_node)
        return min_node.idx
