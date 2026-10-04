class Node:
    def __init__(self, xloc, yloc, kval, adjList):
        self.xloc = xloc
        self.yloc = yloc
        self.kval = kval
        self.adjList = adjList
    def __eq__(self, other):
        return self.xloc == other.xloc and self.yloc == other.yloc and self.kval == other.kval
if __name__ == "__main__":
    node1 = Node(1, 2, 3, [])
    node2 = Node(1, 2, 3, [])
    print(node1 == node2)
    node3 = Node(1, 2, 4, [])
    print(node1 == node3)
