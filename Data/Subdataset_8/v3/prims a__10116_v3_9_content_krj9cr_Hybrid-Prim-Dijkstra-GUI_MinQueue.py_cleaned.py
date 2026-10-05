import sys
class Node:
    def __init__(self, key, idx):
        self.key = key
        self.idx = idx
class MinQueue:
    def __init__(self, nodes):
        self.nodes = nodes[:]
    def __len__(self):
        return len(self.nodes)
    def contains(self, key):
        return any(node.key == key for node in self.nodes)
    def extractMin(self):
        min_node = min(self.nodes, key=lambda node: node.key)
        self.nodes.remove(min_node)
        return min_node.idx
if __name__ == "__main__":
    nodes = [Node(5, 0), Node(3, 1), Node(7, 2), Node(1, 3)]
    min_queue = MinQueue(nodes)
    print("Initial queue length:", len(min_queue))
    print("Does queue contain node with key 7?", min_queue.contains(7))
    print("Extracted minimum node index:", min_queue.extractMin())
    print("Queue length after extraction:", len(min_queue))